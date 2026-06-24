# Inglês para a Austrália — Plano de Estudos

Site estático (MkDocs Material) com o currículo de inglês **do zero ao IELTS** (A0 → C1): 73 lições organizadas por nível (N0–N5), com dependências entre os temas.

🌐 **Ao vivo:** https://ingles.rtfinfo.com (Cloudflare Pages)

> ⚠️ **Repositório público.** Contém **apenas** material de estudo de inglês — **sem dados pessoais** (auditado: nada de TFN, passaporte, ABN, endereço, finanças). Não adicionar aqui nada de outras frentes (visto, finanças, documentos).

Este repo é a **fonte única** do conteúdo (antes vivia no repo privado; foi movido pra cá).

---

## Estrutura

- `docs/` — as 73 lições em Markdown. `index.md` é o mapa do currículo. **Edite aqui** — é a fonte.
- `mkdocs.yml` — config do site (tema Material, navegação por nível, busca PT).
- `requirements.txt` — dependências (MkDocs Material).

## Pré-visualizar localmente

```bash
pip install -r requirements.txt        # ou: pipx install mkdocs && pipx inject mkdocs mkdocs-material
mkdocs serve                           # http://127.0.0.1:8000
```

## Editar o conteúdo

Edite os `.md` em `docs/` direto. Pra adicionar uma lição nova, crie o arquivo e inclua no `nav:` do `mkdocs.yml`. Depois:

```bash
git add -A && git commit -m "update lessons" && git push    # Cloudflare Pages refaz o deploy sozinho
```

---

## Deploy (Cloudflare Pages → `ingles.rtfinfo.com`)

Conectado ao GitHub: cada `git push` na branch `main` redeploya automático.

**Build settings (no projeto Pages):**

| Campo | Valor |
|---|---|
| Framework preset | None |
| Build command | `pip install -r requirements.txt && mkdocs build` |
| Build output directory | `site` |
| Env var | `PYTHON_VERSION` = `3.12` |

**Custom domain:** Pages → Custom domains → `ingles.rtfinfo.com` (CNAME automático; HTTPS automático).
