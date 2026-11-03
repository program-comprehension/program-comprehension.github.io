// Central site configuration. Edit values here to update them across all pages.

export const SITE = {
  name: 'ICPC',
  brand: 'ICPC',
  fullName: 'IEEE/ACM International Conference on Program Comprehension',
  title: 'ICPC — IEEE/ACM International Conference on Program Comprehension',
  description:
    'The IEEE/ACM International Conference on Program Comprehension (ICPC) is the premier ' +
    'venue for research on how people and tools understand software. This is the site ' +
    'of the ICPC steering committee: upcoming and past editions, governance, awards, ' +
    'and how to host a future ICPC.',
  sponsor: 'IEEE/ACM International Conference on Program Comprehension',
  tagline: 'Working Towards a Better Understanding of Software for Humans in the AI Era',
  // The steering committee's shared address. Written reversed in the source of
  // the old site to foil scrapers; shown here through the Obfuscated component.
  contactEmail: 'icpc-sc@googlegroups.com',
  github: 'https://github.com/program-comprehension/program-comprehension.github.io',
};

export const NAV: { label: string; href: string }[] = [
  { label: 'Home', href: '/' },
  { label: 'Events', href: '/events' },
  { label: 'Committee', href: '/committee' },
  { label: 'Governance', href: '/governance' },
  { label: 'Awards', href: '/awards' },
  { label: 'Host ICPC', href: '/hosting' },
  { label: 'History', href: '/history' },
  { label: 'Resources', href: '/resources' },
];
