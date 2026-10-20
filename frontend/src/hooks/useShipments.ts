import { useEffect, useState } from 'react'
import { getShipments, type Shipment } from '../api/client'

//loads shipments from the backend and tracks loading/error state.
//each component that calls this gets its own state and does its own fetch.
export function useShipments() {
  const [shipments, setShipments] = useState<Shipment[]>([])
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
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

  return { shipments, loading, error }
}
