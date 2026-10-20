//"2026-10-20" -> "Oct 20, 2026". Adding T00:00 keeps it in local time
//otherwise the date is read as UTC and can show up a day early
export function formatDate(isoDate: string) {
  return new Date(`${isoDate}T00:00:00`).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}
