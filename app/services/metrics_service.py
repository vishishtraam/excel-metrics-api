

import pandas as pd
from app.infrastructure.repositories.metrics_repository import MetricsRepository

class MetricsService:
    
    def __init__(self):
        self.repo = MetricsRepository()

    def calculate_metrics(self, df: pd.DataFrame):
        return self.repo.get_metrics(df)
