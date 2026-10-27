import { useState } from 'react'
import { useShipments } from '../hooks/useShipments'
import { formatDate } from '../utils/formatDate'

export default function ShipmentsPage() {
  const { shipments, loading, error } = useShipments()
  const [search, setSearch] = useState('')
  const [statusFilter, setStatusFilter] = useState('All')

  if (loading) return <p>Loading shipments…</p>
  if (error) return <p>{error}</p>

  //recalculated on every render from shipments + search, so it never goes stale
  const query = search.trim().toLowerCase()
  const filteredShipments = shipments.filter((s) => {
    const matchesStatus = statusFilter === 'All' || s.status === statusFilter
    const matchesSearch =
      (s.order_number ?? '').toLowerCase().includes(query) ||
      (s.customer ?? '').toLowerCase().includes(query) ||
      (s.load_id ?? '').toLowerCase().includes(query) ||
      (s.destination ?? '').toLowerCase().includes(query)
    return matchesStatus && matchesSearch
  })

  return (
    <section>
      <h1 className="page-title">Shipment Visibility</h1>

      <div className="toolbar">
        <input
          className="search-input"
          type="search"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Search order #, customer, load ID, destination…"
        />
        <select
          className="filter-select"
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
        >
          <option value="All">All statuses</option>
          {Array.from(new Set(shipments.map((s) => s.status)))
            .filter(Boolean)
            .sort()
            .map((status) => (
              <option key={status} value={status}>
                {status}
              </option>
            ))}
        </select>
        <p className="result-count">
          {filteredShipments.length} of {shipments.length} shipments
        </p>
      </div>

      <div className="table-wrap">
        <table className="shipments-table">
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
              <th className="num">Pallets</th>
              <th className="num">Weight (lbs)</th>
            </tr>
          </thead>
          <tbody>
            {filteredShipments.map((shipment) => (
              <tr key={shipment.orderkey}>
                <td className="order-number">{shipment.order_number}</td>
                <td>{shipment.customer || 'N/A'}</td>
                <td>
                  <span className={`status status--${shipment.status.toLowerCase()}`}>
                    {shipment.status}
                  </span>
                </td>
                <td>{shipment.ship_date ? formatDate(shipment.ship_date) : 'N/A'}</td>
                <td>{shipment.carrier || 'N/A'}</td>
                <td>{shipment.load_id || 'N/A'}</td>
                <td>{shipment.warehouse || 'N/A'}</td>
                <td>{shipment.destination || 'N/A'}</td>
                <td className="num">{shipment.pallet_count ?? 'N/A'}</td>
                <td className="num">{shipment.weight_lbs?.toLocaleString() ?? 'N/A'}</td>
              </tr>
            ))}
          </tbody>
        </table>

        {filteredShipments.length === 0 && (
          <p className="empty-state">No shipments match your filters.</p>
        )}
      </div>
    </section>
  )
}
