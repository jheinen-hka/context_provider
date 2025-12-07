from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9+

app = FastAPI(
    title="context_provider",
    description="Python Environment Context Service (Request/Response)",
    version="0.1.0",
)

# health check endpoint
@app.get("/health")
async def health():
    return {"ok": True}

# context endpoint
@app.get("/context")
async def get_context():
    now = datetime.now(ZoneInfo("Europe/Berlin"))
    return {
        "type": "context-snapshot",
        "version": "0.1",
        "producedAt": now.isoformat(),
        "data": {
            "message": "Stub message",
            "serverTime": now.isoformat(),
        },
    }