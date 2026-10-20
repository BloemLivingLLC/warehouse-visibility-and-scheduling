// Thin wrapper around fetch for talking to the backend REST API.
// All requests go to /api/*, which Vite proxies to the backend in development.

const API_BASE = '/api'

export class ApiError extends Error {
  status: number

  constructor(status: number, message: string) {
    super(message)
    this.status = status
  }
}

export async function apiGet<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { Accept: 'application/json' },
  })
  if (!res.ok) {
    throw new ApiError(res.status, `GET ${path} failed with ${res.status}`)
  }
  return res.json() as Promise<T>
}

export type HealthResponse = { status: string }

export function getHealth() {
  return apiGet<HealthResponse>('/health')
}

export type Shipment = {
  orderkey: number
  order_number: string
  status: string
  carrier: string
  ship_date: string
  load_id: string
  customer: string
  warehouse: string
  destination: string
  weight_lbs: number
  pallet_count: number
}

export function getShipments() {
  return apiGet<Shipment[]>('/shipments')
}