from pydantic import BaseModel

class GroupTotal(BaseModel):
    key: str
    total_sales: float
