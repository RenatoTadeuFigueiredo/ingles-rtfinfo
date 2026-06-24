# Inglês para a Austrália — Plano de Estudos (site público)

Site estático (MkDocs Material) com o currículo de inglês **do zero ao IELTS** (A0 → C1), 73 lições organizadas por nível (N0–N5) com dependências entre temas.

🌐 **Destino:** `https://ingles.rtfinfo.com` (Cloudflare Pages)

> ⚠️ **Privacidade:** este repositório é **público** e contém **apenas** o material de estudo de inglês. O conteúdo foi auditado: **sem dados pessoais** (TFN, passaporte, ABN, endereço, finanças). Os exemplos usam só os primeiros nomes Giovanna/Renato. **Nunca** adicionar aqui nada das outras frentes do projeto (visto, finanças, documentos) — elas ficam no repositório privado.

---

## Conteúdo

- `docs/` — as 73 lições em Markdown (`index.md` é o mapa do currículo) — **cópia** vinda do repo privado `Australia/09-ingles/plano-estudos/`.
- `mkdocs.yml` — config do site (tema, navegação por nível, busca em PT).
- `requirements.txt` — dependências (MkDocs Material).
- `build_from_private.py` — regenera `docs/` + `mkdocs.yml` a partir do repo privado (rodar quando as lições mudarem).

## Pré-visualizar localmente

```bash
pip install -r requirements.txt        # ou: pipx install mkdocs && pipx inject mkdocs mkdocs-material
mkdocs serve                           # abre http://127.0.0.1:8000
```

## Atualizar o conteúdo (quando editar as lições no repo privado)

```bash
python3 build_from_private.py          # recopia as lições e regenera a navegação
git add -A && git commit -m "update lessons" && git push
```

---

## Deploy no Cloudflare Pages (recomendado — auto-deploy a cada push)

1. **Criar um repositório PÚBLICO no GitHub** e subir este projeto:
   ```bash
   gh repo create ingles-rtfinfo --public --source=. --remote=origin --push
   ```
   *(ou criar pelo site do GitHub e `git remote add origin … && git push -u origin main`)*

2. **Cloudflare Dashboard → Workers & Pages → Create → Pages → Connect to Git** → escolher o repo `ingles-rtfinfo`.

3. **Build settings:**
   | Campo | Valor |
   |---|---|
   | Framework preset | None |
   | Build command | `pip install -r requirements.txt && mkdocs build` |
   | Build output directory | `site` |
   | Environment variable | `PYTHON_VERSION` = `3.12` |

4. **Save and Deploy.** Sai um endereço `*.pages.dev` funcionando.

5. **Subdomínio `ingles.rtfinfo.com`:** no projeto Pages → **Custom domains → Set up a custom domain** → digitar `ingles.rtfinfo.com`. Como `rtfinfo.com` já está na Cloudflare, o registro **CNAME** é criado automaticamente. Pronto em alguns minutos (HTTPS automático).

## Alternativa rápida (sem GitHub) — upload direto

```bash
mkdocs build
npx wrangler pages deploy site --project-name=ingles-rtfinfo
```
Depois associar o domínio `ingles.rtfinfo.com` em Custom domains (passo 5 acima).
