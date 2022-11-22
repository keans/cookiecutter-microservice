from database.db import SessionLocal


def get_db():
    """
    get the database for the Dependency
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
