from app.services.metrics_service import MetricsService

class ApplicationContainer:
   
    def __init__(self):
        self.metrics_service = MetricsService()
