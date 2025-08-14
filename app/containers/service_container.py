from app.services.metrics_service import MetricsService

class ServiceContainer:
    
    def __init__(self):
        self.metrics_service = MetricsService()
