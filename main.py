import logging
from fastapi import FastAPI
import uvicorn
from app.containers.container import Container  
from app.api.v1.metrics import metrics_endpoints
from app.core.config import AppConfig

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    # Load settings
    settings = AppConfig()

    # Initialize dependency injection container
    container = Container()

    # Wire dependency injection modules
    container.wire(
        modules=[
            "app.api.dependencies",
            "app.api.v1.metrics.metrics_endpoints",
        ]
    )

    # Create FastAPI app
    app = FastAPI()

    # Attach DI container to the app
    app.container = container


    # Health check endpoint
    @app.get("/health")
    async def health_check():
        return {
            "status": "healthy",
            "service": "metrics-api",
            "version": "0.1.0",
        }

    # Register routes
    app.include_router(metrics_endpoints.router, prefix="/api/v1")

    print("FastAPI application configured successfully")
    return app


app = create_app()


if __name__ == "__main__":
    try:
        uvicorn.run(
            "main:app",
        )
    except KeyboardInterrupt:
        logging.info("Server shutdown requested by user")
    except Exception as e:
        logging.error(f"Server startup failed: {e}", exc_info=True)
        raise
