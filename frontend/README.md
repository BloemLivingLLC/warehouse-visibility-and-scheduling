# Frontend

React + TypeScript single-page app for the Bloem warehouse visibility and truck scheduling platform, built with [Vite](https://vite.dev).

## Getting started

Requires Node.js 20+.

```bash
cd frontend
npm install
cp .env.example .env   # optional: change where /api is proxied
npm run dev            # http://localhost:5173
```

## Scripts

| Command | Description |
|---|---|
| `npm run dev` | Start the dev server with hot reload |
| `npm run build` | Type-check and build for production into `dist/` |
| `npm run preview` | Serve the production build locally |
| `npm run lint` | Lint with oxlint |

## Talking to the backend

The app calls the backend through relative `/api/*` URLs (see `src/api/client.ts`). In development, Vite proxies those requests to `VITE_API_PROXY_TARGET` (default `http://localhost:8000`). The header shows whether `GET /api/health` responds.

## Structure

```
src/
  api/          REST client and response types
  components/   Shared UI (layout, status indicator)
  pages/        One component per route: Shipments, Schedule, Bookings
  App.tsx       Route definitions
```
