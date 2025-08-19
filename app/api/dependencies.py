from typing import Generator
from psycopg2.extensions import cursor
from dependency_injector.wiring import Provide, inject
from app.containers.container import Container
from app.services.metrics_service import MetricsService
from fastapi import Depends


@inject
def get_metrics_service(
    metrics_service: MetricsService = Depends(Provide[Container.metrics_service]),
) -> MetricsService:
    return metrics_service


@inject
def get_db_cursor(
    conn=Depends(Provide[Container.db_connection]),
) -> Generator[cursor, None, None]:  
    """Provide a cursor per request."""
    cur = conn.cursor()
    try:
        yield cur
        conn.commit()
    finally:
        cur.close()
