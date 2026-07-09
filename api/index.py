import os
import sys

# Ensure Python knows where to find our backend modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from configs.config import settings
from routes.health_routes import router as health_router
from routes.auth_routes import router as auth_router
from routes.gmail_routes import router as gmail_router
from routes.triage_routes import router as triage_router

app = FastAPI(title="LegalEase FastAPI Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin, "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(gmail_router)
app.include_router(triage_router)

# ── Serve React frontend static files ────────────────────────────────────────
# The dist/ folder is built by `npm run build` and sits at the repo root
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dist")

if os.path.isdir(DIST_DIR):
    # Serve static assets (JS, CSS, images)
    app.mount("/assets", StaticFiles(directory=os.path.join(DIST_DIR, "assets")), name="assets")

    # Catch-all: serve index.html for any non-API route (SPA client-side routing)
    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        index_file = os.path.join(DIST_DIR, "index.html")
        return FileResponse(index_file)
