import { NavLink, Outlet } from 'react-router-dom'
import BackendStatus from './BackendStatus'

const navItems = [
  { to: '/', label: 'Shipments', end: true },
  { to: '/schedule', label: 'Dock Schedule' },
  { to: '/bookings', label: 'Carrier Bookings' },
]

export default function Layout() {
  return (
    <div className="app">
      <header className="app-header">
        <span className="app-header__title">Bloem Logistics</span>
        <nav className="app-nav">
          {navItems.map((item) => (
            <NavLink key={item.to} to={item.to} end={item.end}>
              {item.label}
            </NavLink>
          ))}
        </nav>
        <BackendStatus />
      </header>
      <main className="app-main">
        <Outlet />
      </main>
    </div>
  )
}
