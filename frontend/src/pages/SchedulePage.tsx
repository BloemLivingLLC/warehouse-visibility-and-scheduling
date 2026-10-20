import type { EventInput } from '@fullcalendar/core'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'
import FullCalendar from '@fullcalendar/react'
import timeGridPlugin from '@fullcalendar/timegrid'
import type { Shipment } from '../api/client'
import { useShipments } from '../hooks/useShipments'

// Converts a shipment into the event shape FullCalendar expects.
// The full shipment rides along in extendedProps so a click can show its details later.
function toCalendarEvent(shipment: Shipment): EventInput {
  return {
    id: String(shipment.orderkey),
    title: `${shipment.order_number} · ${shipment.customer}`,
    start: shipment.ship_date,
    allDay: true,
    classNames: [`event--${shipment.status.toLowerCase()}`],
    extendedProps: { shipment },
  }
}

export default function SchedulePage() {
  const { shipments, loading, error } = useShipments()

  if (loading) return <p>Loading schedule…</p>
  if (error) return <p>{error}</p>

  const events = shipments.map(toCalendarEvent)

  return (
    <section>
      <h1 className="page-title">Dock / Pickup Schedule</h1>
      <FullCalendar
        plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
        initialView="dayGridMonth"
        headerToolbar={{
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek',
        }}
        events={events}
        height="auto"
      />
    </section>
  )
}
