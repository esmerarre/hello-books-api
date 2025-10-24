from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): #an empty subclass Base that we can give to our SQLAlchemy constructor.
    pass