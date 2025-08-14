

import pandas as pd

class MetricsRepository:
    
    def get_metrics(self, df: pd.DataFrame):
        total_sales = df["sales"].sum() if "sales" in df else 0
        total_orders = df["orders"].sum() if "orders" in df else 0
        return {
            "total_sales": total_sales,
            "total_orders": total_orders
        }
