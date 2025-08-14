from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models
from app.db import get_db

app = FastAPI()

@app.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):
    return db.query(models.Metrics).all()
