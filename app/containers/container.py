"""Containers module."""

import atexit
import psycopg2
from dependency_injector import containers, providers
from app.infrastructure.repositories.metrics_repository import MetricsRepository
from app.services.metrics_service import MetricsService
from app.core.config import AppConfig


def create_db_connection():
    """Create and return a PostgreSQL connection with error handling."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="metrics-api",
            user="postgres",
            password="Vishi"
        )
        print("PostgreSQL connection established")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None



def close_db_connection(conn):
    """Gracefully close PostgreSQL connection."""
    if conn:
        try:
            conn.close()
            print("PostgreSQL connection closed")
        except psycopg2.Error as e:
            print(f"Error closing PostgreSQL connection: {e}")


class Container(containers.DeclarativeContainer):
    """Base container for the application."""

    # Application config
    app_config = providers.Singleton(AppConfig)

    # PostgreSQL connection provider
    db_connection = providers.Singleton(create_db_connection)

    # Repository provider (inject connection)
    metrics_repository = providers.Singleton(
        MetricsRepository,
        db=db_connection
    )

    # Service provider (inject repository)
    metrics_service = providers.Factory(
        MetricsService,
        repo=metrics_repository
    )
