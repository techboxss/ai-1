# LegalEase Frontend

This frontend now uses the separate FastAPI backend for Google OAuth, Gmail, and Ollama triage.

## Run

```bash
cp .env.example .env
npm install
npm run dev
```

Frontend: http://localhost:5173
Backend: http://localhost:8000

The old embedded `server.ts` service was removed. Google tokens stay in the FastAPI backend session cookie.
