from fastapi import FastAPI, UploadFile, File, HTTPException
from app.services import DataProcessorService

app = FastAPI(
    title="Async Data Ingestion & Analytics Engine",
    description="High-performance FastAPI service to ingest, clean via Pandas, and store data in SQL databases.",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "status": "online",
        "engine": "Data Processing Engine Active",
        "docs": "/docs"
    }

@app.post("/api/v1/upload-data/")
async def upload_and_process_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(('.csv', '.xlsx')):
        raise HTTPException(status_code=400, detail="Only CSV or Excel files are supported.")

    contents = await file.read()
    
    # Process & Clean data using Pandas Service
    processed_data = DataProcessorService.process_and_clean_csv(contents)

    return {
        "filename": file.filename,
        "status": "Success",
        "summary": processed_data["summary"],
        "message": "Data successfully cleaned via Pandas and ready for SQL ingestion."
    }
