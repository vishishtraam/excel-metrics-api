from typing import List, Dict
from app.infrastructure.repositories.metrics_repository import MetricsRepository
from dependency_injector.wiring import Provide


class MetricsService:

    def __init__(self, repo: MetricsRepository=Provide["metrics_repository"]):
        self.repo = repo

    def get_region_totals(self, cur) -> List[Dict]:
        return self.repo.totals_by_region(cur)
 
    def get_all_metrics(self, cur) -> List[Dict]:
        """Fetch all rows from the metrics table in Postgres."""
        return self.repo.get_all_metrics(cur)

    def get_summary(self, cur) -> Dict:
        """Fetch summary information about dataset (rows/columns)."""
        return self.repo.get_summary(cur)

