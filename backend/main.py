from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI(
    title="FALCON",
    description="Prototype API for AI-based identity and document screening.",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def home():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/health")
def health():
    return {
        "project": "FALCON",
        "status": "prototype-online",
        "detection_engine": "not-trained-yet",
    }


@app.post("/api/analyze")
async def analyze_document(file: UploadFile = File(...)):
    # Prototype only: accepts the document so the end-to-end application
    # contract exists. No authenticity claim is made at this stage.
    contents = await file.read()

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "bytes_received": len(contents),
        "status": "received",
        "analysis": {
            "ocr": "pending",
            "document_validation": "pending",
            "forensics": "pending",
            "face_match": "pending",
            "liveness": "pending",
            "risk_score": None,
        },
        "message": (
            "Prototype upload successful. The trained detection pipeline "
            "will be connected in later milestones."
        ),
    }
