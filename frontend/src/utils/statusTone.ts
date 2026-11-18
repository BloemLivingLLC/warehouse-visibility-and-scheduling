export type StatusTone = 'open' | 'active' | 'shipped' | 'problem'

//groups Infor's 20 status codes into 4 color families.
//the badge text shows the exact label; the color only shows the stage.
export function statusTone(code: string): StatusTone {
  if (code === '95') return 'shipped'
  if (['00', '06', '99'].includes(code)) return 'problem'
  if (Number(code) >= 14) return 'active'
  return 'open'
}