def calculate_kpis(df):
    return {
        "total_sales": float(df["sales"].sum()),
        "total_orders": int(df["order_id"].nunique())
    }
