from fastapi import APIRouter, Depends, UploadFile, File 
from typing import List, Dict
from app.services.metrics_service import MetricsService
from app.schemas.metrics_schemas import GroupTotal
from app.api.dependencies import get_metrics_service, get_db_cursor
from psycopg2.extensions import cursor  # for type hints
from pathlib import Path
import pandas as pd
import os, shutil                                     
from app.utils.data_cleaner import clean_file

router = APIRouter(prefix="/metrics", tags=["metrics"])

RAW_DIR = "app/api/uploads/raw_data"
CLEANED_DIR = "app/api/uploads/cleaned_data"


@router.get("/totals/regions", response_model=List[GroupTotal])
def get_region_totals(
    service: MetricsService = Depends(get_metrics_service),
    cur: cursor = Depends(get_db_cursor)
):
    return service.get_region_totals(cur)


@router.get("/data")
def get_data():
    """Just loads Excel dataset from local file (not DB)."""
    project_root = Path(__file__).resolve().parents[4]  # go up 5 levels
    dataset_path = project_root / "data" / "Adidas US Sales Datasets.xlsx"

    print("📂 Dataset path:", dataset_path)

    df = pd.read_excel(dataset_path)

    return {
        "message": "✅ Data loaded successfully",
        "rows": df.shape[0],
        "columns": df.shape[1]
    }


@router.get("/all", response_model=List[Dict])
def get_all_metrics(
    service: MetricsService = Depends(get_metrics_service),
    cur: cursor = Depends(get_db_cursor)
):
    return service.get_all_metrics(cur)


@router.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    # Ensure both folders exist
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(CLEANED_DIR, exist_ok=True)

    # Save raw file
    raw_path = os.path.join(RAW_DIR, file.filename)
    with open(raw_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Clean file → save in CLEANED_DIR
    cleaned_path, df = clean_file(raw_path, CLEANED_DIR)

    return {
        "message": "✅ File uploaded and cleaned successfully",
        "raw_file": os.path.basename(raw_path),
        "cleaned_file": os.path.basename(cleaned_path),
        "rows_cleaned": len(df)
    }
