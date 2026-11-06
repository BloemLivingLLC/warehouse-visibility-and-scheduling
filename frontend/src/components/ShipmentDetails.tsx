import type { Shipment } from '../api/client'
import { formatDate } from '../utils/formatDate'

type ShipmentDetailsProps = {
  shipment: Shipment
  onClose: () => void
}

//side panel showing every field of one shipment.
export default function ShipmentDetails({ shipment, onClose }: ShipmentDetailsProps) {
  return (
    <aside className="details-panel">
      <div className="details-panel__header">
        <h2>{shipment.order_number}</h2>
        <button type="button" className="details-panel__close" onClick={onClose}>
          Close
        </button>
      </div>

      <span className={`status status--${shipment.status.toLowerCase()}`}>
        {shipment.status}
      </span>

      <dl className="details-list">
        <dt>Customer</dt>
        <dd>{shipment.customer || 'N/A'}</dd>
        <dt>Ship date</dt>
        <dd>{shipment.ship_date ? formatDate(shipment.ship_date) : 'N/A'}</dd>
        <dt>Carrier</dt>
        <dd>{shipment.carrier?.trim() || 'N/A'}</dd>
        <dt>Load ID</dt>
        <dd>{shipment.load_id || 'N/A'}</dd>
        <dt>Warehouse</dt>
        <dd>{shipment.warehouse || 'N/A'}</dd>
        <dt>Destination</dt>
        <dd>{shipment.destination || 'N/A'}</dd>
        <dt>Pallets</dt>
        <dd>{shipment.pallet_count ?? 'N/A'}</dd>
        <dt>Weight</dt>
        <dd>{shipment.weight_lbs != null ? `${shipment.weight_lbs.toLocaleString()} lbs` : 'N/A'}</dd>
      </dl>
    </aside>
  )
}
