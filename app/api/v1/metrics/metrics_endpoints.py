from fastapi import APIRouter, Depends
from typing import List, Dict
from app.services.metrics_service import MetricsService
from app.schemas.metrics_schemas import GroupTotal
from app.api.dependencies import get_metrics_service, get_db_cursor
from psycopg2.extensions import cursor  # for type hints
from pathlib import Path
import pandas as pd

router = APIRouter(prefix="/metrics", tags=["metrics"])


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
