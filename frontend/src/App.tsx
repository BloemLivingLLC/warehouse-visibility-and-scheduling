import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Layout from './components/Layout'
import BookingsPage from './pages/BookingsPage'
import NotFoundPage from './pages/NotFoundPage'
import SchedulePage from './pages/SchedulePage'
import ShipmentsPage from './pages/ShipmentsPage'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<ShipmentsPage />} />
          <Route path="schedule" element={<SchedulePage />} />
          <Route path="bookings" element={<BookingsPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
