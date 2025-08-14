from pydantic import BaseModel

class MetricsResponse(BaseModel):
    """Response schema for metrics API."""
    total_sales: float
    total_orders: int
