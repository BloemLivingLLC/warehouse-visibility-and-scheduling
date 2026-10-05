import { useEffect, useState } from 'react'
import { getHealth } from '../api/client'

type Status = 'checking' | 'online' | 'offline'

// Shows whether the frontend can reach the backend's /api/health endpoint.
export default function BackendStatus() {
  const [status, setStatus] = useState<Status>('checking')

  useEffect(() => {
    getHealth()
      .then(() => setStatus('online'))
      .catch(() => setStatus('offline'))
  }, [])

  const label = {
    checking: 'Checking backend…',
    online: 'Backend connected',
    offline: 'Backend unreachable',
  }[status]

  return (
    <span className={`backend-status backend-status--${status}`}>
      <span className="backend-status__dot" />
      {label}
    </span>
  )
}
