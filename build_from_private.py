#!/usr/bin/env python3
"""Scaffold an MkDocs Material site from the plano-estudos lessons.
Output goes to a separate dir (NOT the private repo)."""
import os, re, shutil, glob

SRC = "/Users/renato/Projects/pessoal/Australia/09-ingles/plano-estudos"
OUT = "/Users/renato/Projects/pessoal/ingles-rtfinfo"
DOCS = os.path.join(OUT, "docs")

# --- reset docs dir ---
if os.path.isdir(DOCS):
    shutil.rmtree(DOCS)
os.makedirs(DOCS)

# --- copy lessons; MAPA becomes index.md ---
files = sorted(glob.glob(os.path.join(SRC, "*.md")))
for f in files:
    base = os.path.basename(f)
    dest = "index.md" if base == "00-MAPA.md" else base
    shutil.copy(f, os.path.join(DOCS, dest))

def h1(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"#\s+(.*)", line.strip())
            if m:
                # strip leading "N0-01 — " style codes for a cleaner label
                t = m.group(1).strip()
                return t
    return os.path.basename(path)

# --- level group titles parsed from the MAPA (## N0 — Fundação (A0–A1)) ---
groups = {}
with open(os.path.join(SRC, "00-MAPA.md"), encoding="utf-8") as fh:
    for line in fh:
        m = re.match(r"##\s+(N\d)\s*[—-]\s*(.*)", line.strip())
        if m:
            groups[m.group(1)] = f"{m.group(1)} · {m.group(2).strip()}"

# --- build nav grouped by level ---
lessons = sorted(b for b in os.listdir(DOCS) if b.startswith("N") and b.endswith(".md"))
nav_lines = ["nav:", "  - Início (mapa do currículo): index.md"]
by_level = {}
for b in lessons:
    lvl = b[:2]
    by_level.setdefault(lvl, []).append(b)
for lvl in sorted(by_level):
    title = groups.get(lvl, lvl)
    nav_lines.append(f"  - \"{title}\":")
    for b in by_level[lvl]:
        label = h1(os.path.join(DOCS, b)).replace('"', "'")
        nav_lines.append(f"      - \"{label}\": {b}")
nav_yaml = "\n".join(nav_lines)

mkdocs_yml = f"""site_name: Inglês para a Austrália — Plano de Estudos
site_description: Currículo completo de inglês do zero ao IELTS (A0 → C1), com dependências entre temas.
site_url: https://ingles.rtfinfo.com/
site_author: rtfinfo

theme:
  name: material
  language: pt-BR
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.top
    - navigation.indexes
    - toc.follow
    - search.suggest
    - search.highlight
    - content.code.copy
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/weather-night
        name: Modo escuro
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/weather-sunny
        name: Modo claro

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.highlight
  - pymdownx.superfences
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg

plugins:
  - search:
      lang: pt

{nav_yaml}
"""

with open(os.path.join(OUT, "mkdocs.yml"), "w", encoding="utf-8") as fh:
    fh.write(mkdocs_yml)

with open(os.path.join(OUT, ".gitignore"), "w", encoding="utf-8") as fh:
    fh.write("site/\n__pycache__/\n.DS_Store\n")

print(f"Scaffolded {len(lessons)} lessons + index into {OUT}")
print(f"Levels: {', '.join(sorted(by_level))}")
