import pandas as pd
import psycopg2
from typing import List, Dict
from dependency_injector.wiring import Provide
# from app.db import get_db  # assuming this returns a connection factory


class MetricsRepository:
   
    def __init__(self, db=Provide["db_connection"]):
        self._db = db
        self._df = None
        self.dataset_path = None  # if you still want to support Excel

    @property
    def df(self) -> pd.DataFrame:
        if self._df is None and self.dataset_path:
            self._df = self._load_and_clean_excel(self.dataset_path)
        return self._df

    def _load_and_clean_excel(self, path: str) -> pd.DataFrame:
        df = pd.read_excel(path)

        # Drop junk columns if present
        df = df.drop(columns=[c for c in ["Unnamed: 0", "Invoice Drae"] if c in df.columns], errors="ignore")

        # Convert dates
        if "Invoice Date" in df.columns:
            df["Invoice Date"] = pd.to_datetime(df["Invoice Date"], errors="coerce")

        # Ensure numeric types
        numeric_cols = ["Retailer ID", "Price per Unit", "Units Sold", "Total Sales",
                        "Operating Profit", "Operating Margin"]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # Drop rows missing critical data
        return df.dropna(subset=["Retailer", "Invoice Date", "Region", "Product"])


    def get_all_metrics(self, cur) -> List[Dict]:
        """Return all metrics from PostgreSQL as JSON."""
        cur = self._db .cursor()

        cur.execute("""
            SELECT id, report_date, total_sales, total_orders, avg_order_value
            FROM metrics
            ORDER BY report_date
        """)
        rows = cur.fetchall()
        return [dict(zip([desc[0] for desc in cur.description], row)) for row in rows]

    def get_summary(self, cur) -> Dict:
        """Return summary info for metrics table."""
        cur.execute("SELECT COUNT(*) FROM metrics")
        row_count = cur.fetchone()[0]
        col_count = len(cur.description) if cur.description else 5  # fallback
        return {
            "rows": row_count,
            "columns": col_count,
            "message": "✅ Metrics loaded successfully"
        }

    # ⬅️ CHANGED: accept cursor instead of fetching via pandas
    def totals_by_region(self, cur) -> List[Dict]:
        cur.execute("""
            SELECT region, SUM(total_sales) AS total_sales
            FROM metrics
            GROUP BY region
            ORDER BY total_sales DESC
        """)
        rows = cur.fetchall()
        return [{"key": row[0], "total_sales": float(row[1])} for row in rows]
