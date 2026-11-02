// Prefix an internal path with the configured base URL so links work whether the
// site is deployed at the domain root (org page) or under a subpath.
export function withBase(path: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  if (path === '/') return base || '/';
  return `${base}${path}`;
}

// 1 → "1st", 22 → "22nd", 33 → "33rd", 11 → "11th".
export function ordinal(n: number): string {
  const mod100 = n % 100;
  if (mod100 >= 11 && mod100 <= 13) return `${n}th`;
  switch (n % 10) {
    case 1: return `${n}st`;
    case 2: return `${n}nd`;
    case 3: return `${n}rd`;
    default: return `${n}th`;
  }
}

// Format an ISO date (YYYY-MM-DD) as "12 April 2026". Parsed by hand to avoid
// timezone drift from Date.
export function formatDate(iso: string): string {
  const [y, m, d] = iso.split('-').map(Number);
  const months = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'];
  return `${d} ${months[(m || 1) - 1]} ${y}`;
}

// The long name each edition carried at the time.
export function seriesName(series: string): string {
  switch (series) {
    case 'WPC': return 'Workshop on Program Comprehension';
    case 'IWPC': return 'International Workshop on Program Comprehension';
    default: return 'International Conference on Program Comprehension';
  }
}

// An edition is upcoming until the end of its last day. Editions without an
// explicit `ends` date count as upcoming for the whole of their year.
export function isUpcoming(e: { year: number; ends?: string }, now = new Date()): boolean {
  const end = e.ends ? new Date(`${e.ends}T23:59:59Z`) : new Date(`${e.year}-12-31T23:59:59Z`);
  return end.getTime() >= now.getTime();
}
