from app.infrastructure.repositories.metrics_repository import MetricsRepository

class RepositoryContainer:
   
    def __init__(self):
        self.metrics_repository = MetricsRepository()
