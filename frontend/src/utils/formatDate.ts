//"2026-10-20" or "2026-10-20T14:10:34.000+00:00" -> "Oct 20, 2026"
//plain dates get T00:00 so they stay in local time instead of shifting a day early;
//timestamps already include a time and timezone, so they're used as-is
export function formatDate(isoDate: string) {
  const date = isoDate.includes('T') ? new Date(isoDate) : new Date(`${isoDate}T00:00:00`)
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}