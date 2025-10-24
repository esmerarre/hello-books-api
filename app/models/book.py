#need access to SQLAlchemy's tools for defining table columns in a model
from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

#SQLAlchemy will use the lowercase version of this class name as the name of the table it will create
#Our model inherits from db.Model
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]





# hardcoded books data, book.py

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]