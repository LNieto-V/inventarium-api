from sqlmodel import create_engine
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_TEST_URL, 
    echo=True, 
    connect_args={"check_same_thread": False}
)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
