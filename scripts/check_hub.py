#!/usr/bin/env python3
"""Check public study-hub navigation and pairings without running deck builders."""

import ast
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', 'instructor-private', 'drafts', 'scratch', 'node_modules', '.venv', 'venv', '__pycache__'}


def public_files(pattern):
    return sorted(p for p in ROOT.rglob(pattern)
                  if not EXCLUDED.intersection(p.relative_to(ROOT).parts)
                  and not p.name.endswith('.draft.md'))


def visible_markdown(text):
    return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)


def heading_ids(text):
    counts = {}
    ids = set()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', visible_markdown(text), re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        slug = re.sub(r'[^\w\-\s]', '', heading.lower()).replace(' ', '-')
        duplicate = counts.get(slug, 0)
        counts[slug] = duplicate + 1
        ids.add(slug + (f'-{duplicate}' if duplicate else ''))
    return ids


def output_path(node, source):
    """Interpret only the existing builders' string/path syntax, never execute it."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name) and node.id == '__file__':
        return str(source)
    if isinstance(node, ast.Call):
        name = ast.unparse(node.func)
        args = [output_path(arg, source) for arg in node.args]
        if name == 'os.path.dirname' and len(args) == 1:
            return os.path.dirname(args[0])
        if name == 'os.path.join':
            return os.path.join(*args)
    raise ValueError('unsupported output-path expression')


def check():
    problems = []
    documents = public_files('*.md')
    anchors = {p.resolve(): heading_ids(p.read_text(encoding='utf-8-sig')) for p in documents}
    checked_links = 0
    for file in documents:
        text = file.read_text(encoding='utf-8-sig')
        label = file.relative_to(ROOT).as_posix()
        fences = re.findall(r'^```', text, re.M)
        if len(fences) % 2:
            problems.append(f'{label}: unclosed fenced code block')
        for raw in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', visible_markdown(text)):
            url = raw.split(' "')[0].strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', url) or url.startswith('//'):
                continue
            path, _, fragment = url.partition('#')
            target = (file.parent / unquote(path)).resolve() if path else file.resolve()
            checked_links += 1
            if EXCLUDED.intersection(target.parts):
                problems.append(f'{label}: public link points into an excluded area: {url}')
            elif not target.exists():
                problems.append(f'{label}: missing link target: {url}')
            elif fragment and target in anchors and unquote(fragment).lower() not in anchors[target]:
                problems.append(f'{label}: missing heading: {url}')

    modules = 0
    for course in sorted((ROOT / 'certifications').iterdir()):
        if not course.is_dir():
            continue
        module_files = sorted((course / 'modules').glob('[0-9]*.md'))
        for module in module_files:
            modules += 1
            expected_quiz = course / 'quizzes' / (module.stem + '-quiz.md')
            expected_deck = course / 'lectures' / (module.stem + '.pptx')
            orientation = course.name == 'saa-c03-solutions-architect-associate' and module.name.startswith('01-')
            if not orientation and not expected_quiz.is_file():
                problems.append(f'{module.relative_to(ROOT)}: paired quiz missing')
            if not expected_deck.is_file():
                problems.append(f'{module.relative_to(ROOT)}: paired slide deck missing')
            if '[Course index](../README.md)' not in module.read_text(encoding='utf-8-sig'):
                problems.append(f'{module.relative_to(ROOT)}: course-index navigation missing')
        for quiz in sorted((course / 'quizzes').glob('[0-9]*.md')):
            module = course / 'modules' / (quiz.stem.removesuffix('-quiz') + '.md')
            if not module.is_file():
                problems.append(f'{quiz.relative_to(ROOT)}: paired module missing')

    builders = 0
    for source in public_files('*.py'):
        try:
            tree = ast.parse(source.read_text(encoding='utf-8-sig'), filename=str(source))
        except SyntaxError as error:
            problems.append(f'{source.relative_to(ROOT)}: invalid Python syntax: {error.msg}')
            continue
        if not source.name.startswith('build-'):
            continue
        builders += 1
        assignments = [node.value for node in tree.body if isinstance(node, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id == 'OUT' for t in node.targets)]
        if len(assignments) != 1:
            problems.append(f'{source.relative_to(ROOT)}: expected one OUT destination')
            continue
        try:
            destination = Path(output_path(assignments[0], source)).resolve()
            if ROOT not in destination.parents or 'lectures' not in destination.parts:
                problems.append(f'{source.relative_to(ROOT)}: destination outside a lecture folder')
            elif not destination.is_file():
                problems.append(f'{source.relative_to(ROOT)}: destination does not match an existing deck')
        except ValueError as error:
            problems.append(f'{source.relative_to(ROOT)}: {error}')

    print(f'Checked {len(documents)} public Markdown files, {checked_links} local links, '
          f'{modules} modules, and {builders} slide-builder destinations.')
    if problems:
        for problem in problems:
            print(f'ERROR: {problem}')
        return 1
    print('All local navigation, pairing, code-fence, and destination checks passed.')
    print('External websites, factual currency, and rendered slide layouts were not checked.')
    return 0


if __name__ == '__main__':
    sys.exit(check())
