# Projects

This site publishes a navigable documentation surface for the portfolio and Control Tower context.

## Stack

- Docusaurus
- Markdown docs generated from a CSV snapshot
- Static deployment on Vercel

## Local development

Install dependencies:

```bash
npm install
```

Run the dev server:

```bash
npm run start
```

## Build

```bash
npm run build
```

## Generated docs

Project context docs are materialized under:

```text
docs/control-tower/
```

These files are generated from a CSV snapshot using:

```bash
python build_control_tower_docs.py --csv portfolio_context.csv --docs-root docs
```

## Deployment

Production URL:

```text
https://projects.matuteiglesias.link
```

Recommended deployment target:

* Vercel
* Framework preset: Docusaurus
* Build command: `npm run build`
* Output directory: `build`

## Repository

```text
https://github.com/matuteiglesias/projects
```
