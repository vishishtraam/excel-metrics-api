from sqlalchemy import Column, Integer, Numeric, Date
from app.db import Base

class Metrics(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    report_date = Column(Date)
    total_sales = Column(Numeric(10, 2))
    total_orders = Column(Integer)
    avg_order_value = Column(Numeric(10, 2))
