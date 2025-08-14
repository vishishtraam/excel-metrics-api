import pandas as pd
from app.utils.kpi_calculator import calculate_kpis

def test_kpi_calculation():
    df = pd.DataFrame({"sales": [100, 200], "orders": [1, 2]})
    kpis = calculate_kpis(df)
    assert kpis["total_sales"] == 300
    assert kpis["total_orders"] == 3
