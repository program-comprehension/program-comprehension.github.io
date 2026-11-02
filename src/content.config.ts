import { defineCollection, z } from 'astro:content';
import { file } from 'astro/loaders';

// Every edition of WPC / IWPC / ICPC. Newest first in the file; pages sort by year.
const events = defineCollection({
  loader: file('src/content/events.yaml'),
  schema: z.object({
    number: z.number(),
    series: z.enum(['WPC', 'IWPC', 'ICPC']),
    year: z.number(),
    dates: z.string(),
    ends: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).optional(),
    location: z.string(),
    site: z.string().url().optional(),
    proceedings: z.string().optional(),
    colocated: z.string().optional(),
    generalChairs: z.array(z.string()).default([]),
    programChairs: z.array(z.string()).default([]),
  }),
});

// Steering committee: current members and alumni.
const committee = defineCollection({
  loader: file('src/content/committee.yaml'),
  schema: z.object({
    name: z.string(),
    affiliation: z.string().optional(),
    url: z.string().url().optional(),
    role: z.string().optional(), // "Chair", "Secretary"
    status: z.enum(['current', 'alumni', 'lifetime']).default('current'),
    term: z.number().optional(), // 1 or 2
    termEnds: z.number().optional(), // year the current term ends
    elected: z.number().optional(),
    order: z.number().default(0),
  }),
});

// Governance documents (PDFs under public/).
const documents = defineCollection({
  loader: file('src/content/documents.yaml'),
  schema: z.object({
    title: z.string(),
    version: z.string().optional(),
    adopted: z.string().optional(),
    file: z.string(),
    current: z.boolean().default(false),
    summary: z.string().optional(),
    order: z.number().default(0),
  }),
});

// Awards given at ICPC, grouped by `award`.
const awards = defineCollection({
  loader: file('src/content/awards.yaml'),
  schema: z.object({
    award: z.enum(['mip', 'rajlich', 'distinguished', 'reviewer']),
    year: z.number(),
    title: z.string().optional(), // paper title, or omitted for people awards
    recipients: z.array(z.string()),
    affiliation: z.string().optional(),
    originalYear: z.number().optional(), // MIP: year the paper appeared
    originalSeries: z.string().optional(),
    doi: z.string().optional(),
    url: z.string().url().optional(),
    note: z.string().optional(),
  }),
});

// Short dated announcements for the home page.
const news = defineCollection({
  loader: file('src/content/news.yaml'),
  schema: z.object({
    date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    title: z.string(),
    body: z.string().optional(),
    url: z.string().optional(),
  }),
});

export const collections = { events, committee, documents, awards, news };
