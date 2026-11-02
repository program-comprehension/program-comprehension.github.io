// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// -----------------------------------------------------------------------------
// Deployment
//
// This repo is the GitHub *org page* for program-comprehension, served from the
// domain root via the custom domain in public/CNAME (www.program-comprehension.org),
// so no base path is needed. The site is built and deployed by
// .github/workflows/deploy.yml (GitHub Actions → Pages).
// -----------------------------------------------------------------------------
export default defineConfig({
  site: 'https://www.program-comprehension.org',
  // Astro's HTML compression drops line breaks next to inline elements,
  // gluing words together across the site.
  compressHTML: false,
  trailingSlash: 'ignore',
  integrations: [sitemap()],
  // Old .html URLs from the 2014 site are handled client-side in src/pages/404.astro.
  // Astro's `redirects` would emit e.g. history.html/index.html, which static hosts
  // resolve ahead of history/index.html for /history and then loop.

});
