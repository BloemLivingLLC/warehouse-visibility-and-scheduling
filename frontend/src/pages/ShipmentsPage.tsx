import { useEffect, useState } from 'react'
import { getShipments, type Shipment } from '../api/client'

//"2026-10-20" -> "Oct 20, 2026". Adding T00:00 keeps it in local time
//otherwise the date is read as UTC and can show up a day early
function formatDate(isoDate: string) {
  return new Date(`${isoDate}T00:00:00`).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}

export default function ShipmentsPage() {
  const [shipments, setShipments] = useState<Shipment[]>([])
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<string | null>(null)
  const [search, setSearch] = useState('')

  useEffect(() => {
    //runs once component shows up
    getShipments()
      .then((data) => {
        setShipments(data)
        setLoading(false)
      })
      .catch(() => {
        setError("Couldn't load shipments. Is the backend running?")
        setLoading(false)
      })
  }, [])

  if (loading) return <p>Loading shipments…</p>
  if (error) return <p>{error}</p>

  //recalculated on every render from shipments + search, so it never goes stale
  const query = search.trim().toLowerCase()
  const filteredShipments = shipments.filter(
    (s) =>
      s.order_number.toLowerCase().includes(query) ||
      s.customer.toLowerCase().includes(query) ||
      s.load_id.toLowerCase().includes(query) ||
      s.destination.toLowerCase().includes(query),
  )

  return (
    <section>
      <h1>Shipment Visibility</h1>

      <input
        type="search"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search order #, customer, load ID, destination…"
      />
      <p>
        {filteredShipments.length} of {shipments.length} shipments
      </p>

      <table>
        <thead>
          <tr>
            <th>Order #</th>
            <th>Customer</th>
            <th>Status</th>
            <th>Ship Date</th>
            <th>Carrier</th>
            <th>Load ID</th>
            <th>Warehouse</th>
            <th>Destination</th>
            <th>Pallets</th>
            <th>Weight (lbs)</th>
          </tr>
        </thead>
        <tbody>
          {filteredShipments.map((shipment) => (
            <tr key={shipment.orderkey}>
              <td>{shipment.order_number}</td>
              <td>{shipment.customer}</td>
              <td>{shipment.status}</td>
              <td>{formatDate(shipment.ship_date)}</td>
              <td>{shipment.carrier}</td>
              <td>{shipment.load_id}</td>
              <td>{shipment.warehouse}</td>
              <td>{shipment.destination}</td>
              <td>{shipment.pallet_count}</td>
              <td>{shipment.weight_lbs.toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {filteredShipments.length === 0 && <p>No shipments match "{search}".</p>}
    </section>
  )
}
