from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Change username, password, and dbname as per your setup
DATABASE_URL = "postgresql://postgres:Vishi@localhost:5432/metrics-api"

# Create engine to connect to PostgreSQL
engine = create_engine(DATABASE_URL)

# Create a session factory for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for creating database models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
