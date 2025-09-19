from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Update with your postgres credentials
DATABASE_URL = "postgresql://postgres:1107@localhost:5432/translate-enkn"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
