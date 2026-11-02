# ICPC website

Source of [www.program-comprehension.org](https://www.program-comprehension.org), the site of
the steering committee of the IEEE International Conference on Program Comprehension (ICPC).
Built with [Astro](https://astro.build) and deployed to GitHub Pages by GitHub Actions.

## Editing content

Almost everything that changes from year to year lives in YAML under `src/content/`.
Edit the file, open a pull request, and the site rebuilds on merge.

| File | What it drives |
| --- | --- |
| `events.yaml` | Every edition since 1992: dates, location, website, proceedings, chairs. The home page and `/events` are generated from it. Add an `ends` date so an edition moves from "upcoming" to "past" on its own. |
| `committee.yaml` | Current steering committee members (with role, term and term end), the permanent member, and alumni. |
| `awards.yaml` | Most Influential Paper, Václav Rajlich Early Career Achievement Award, and distinguished paper recipients. |
| `documents.yaml` | Governance documents listed on `/governance`. The PDFs themselves live in `public/`. |
| `news.yaml` | Short dated announcements shown on the home page. |

Other content:

- `src/data/memoir.md` is Václav Rajlich's memoir shown on `/history`.
- `src/data/author-index.json` is the 1992 to 2006 author index, generated from `public/AuthorIndex.xml`.
- Page text that is not data (the hosting guide, the governance summary) is in `src/pages/*.astro`.
- `src/consts.ts` holds the site name, description, contact address and navigation.

## Local development

```sh
npm install
npm run dev       # http://localhost:4321
npm run build     # static output in dist/
npm run preview   # serve dist/
```

Node 20 or later.

## Design

The layout, type scale and components follow the [SAGE Lab site](https://sagelab.io) with an
ICPC-blue palette. Design tokens are in `src/styles/global.css`; light is the default and a
dark theme is available from the toggle in the navigation bar.

### Logo

`src/components/Logo.astro` currently renders a neutral placeholder mark. The candidate logos
from the community vote are in `brand/logo-options/` (light and dark variants of each mark and
lockup, plus the script that generated them). Once a direction is chosen, replace the SVG body in
`Logo.astro` and `public/favicon.svg` with the winning mark.

## Deployment

`.github/workflows/deploy.yml` builds the site on every push to `master` and publishes `dist/`
to GitHub Pages. The repository's Pages source must be set to **GitHub Actions** (Settings →
Pages → Build and deployment → Source). The custom domain is set in `public/CNAME`.

Old URLs from the previous site (`pastevents.html`, `steeringcommittee.html`, the per-letter
author index pages, …) redirect to their new locations; see `redirects` in `astro.config.mjs`.
PDFs keep their original paths.

## History of this repository

The previous site was hand-written HTML from 2014. Its files were removed in the Astro
rewrite but remain in the git history before the `astro-redesign` merge.
