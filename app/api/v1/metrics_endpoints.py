from fastapi import APIRouter, UploadFile, File
from app.utils.excel_reader import read_and_clean_excel
from app.utils.kpi_calculator import calculate_kpis

router = APIRouter()

@router.post("/upload")
async def upload_excel(file: UploadFile = File(...)):
    df = read_and_clean_excel(file.file)
    kpis = calculate_kpis(df)
    return {"kpis": kpis}
