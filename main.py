import os
import uuid
from typing import Dict, Any

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from analysis import analyze_video

# Make sure upload directory exists
os.makedirs("videos", exist_ok=True)

app = FastAPI()

# Jinja2 templates (for the HTML page)
templates = Jinja2Templates(directory="templates")

# In-memory storage for reports (demo only)
REPORTS: Dict[str, Dict[str, Any]] = {}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    # Create unique ID for this game
    game_id = str(uuid.uuid4())

    # Save video to disk
    filename = f"{game_id}_{file.filename}"
    video_path = os.path.join("videos", filename)

    with open(video_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # "Analyze" video using fake AI
    report = analyze_video(video_path)

    # Store in memory
    REPORTS[game_id] = report

    return JSONResponse(
        {
            "game_id": game_id,
            "message": "Video uploaded and analyzed (demo AI).",
            "report": report,
        }
    )


@app.get("/report/{game_id}")
async def get_report(game_id: str):
    report = REPORTS.get(game_id)
    if not report:
        return JSONResponse(
            {"error": "Report not found. Maybe the game ID is wrong."},
            status_code=404,
        )
    return JSONResponse({"game_id": game_id, "report": report})


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
