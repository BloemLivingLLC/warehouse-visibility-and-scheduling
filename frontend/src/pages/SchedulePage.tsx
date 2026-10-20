import type { EventClickArg, EventInput } from '@fullcalendar/core'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'
import FullCalendar from '@fullcalendar/react'
import timeGridPlugin from '@fullcalendar/timegrid'
import { useEffect, useRef, useState } from 'react'
import type { Shipment } from '../api/client'
import ShipmentDetails from '../components/ShipmentDetails'
import { useShipments } from '../hooks/useShipments'

//converts a shipment into the event shape FullCalendar expects
//the full shipment rides along in extendedProps so a click can show its details later
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
  const [selectedShipment, setSelectedShipment] = useState<Shipment | null>(null)
  const calendarRef = useRef<FullCalendar>(null)

  //fullCalendar only re-measures on window resize, so tell it to resize
  // whenever the details panel opens or closes and changes its width
  useEffect(() => {
    calendarRef.current?.getApi().updateSize()
  }, [selectedShipment])

  if (loading) return <p>Loading schedule…</p>
  if (error) return <p>{error}</p>

  const events = shipments.map(toCalendarEvent)

  //fullCalendar passes the clicked event; we stored the shipment on it in toCalendarEvent
  function handleEventClick(info: EventClickArg) {
    setSelectedShipment(info.event.extendedProps.shipment as Shipment)
  }

  return (
    <section>
      <h1 className="page-title">Dock / Pickup Schedule</h1>
      <div className={selectedShipment ? 'schedule-layout schedule-layout--open' : 'schedule-layout'}>
        <FullCalendar
          ref={calendarRef}
          plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
          initialView="dayGridMonth"
          headerToolbar={{
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek',
          }}
          events={events}
          eventClick={handleEventClick}
          height="auto"
        />
        {selectedShipment && (
          <ShipmentDetails
            shipment={selectedShipment}
            onClose={() => setSelectedShipment(null)}
          />
        )}
      </div>
    </section>
  )
}
