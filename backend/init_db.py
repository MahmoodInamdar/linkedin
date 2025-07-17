import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.models import Base
from utils.config import DATABASE_URL
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

print("Database tables created successfully.") 