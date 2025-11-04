from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.author import Author
from .route_utilities import validate_model

bp = Blueprint("author_bp", __name__, url_prefix="/authors")

@bp.post("")
def create_author():
    request_body = request.get_json()
    try:
        new_author = Author.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_author)
    db.session.commit()

    response = new_author.to_dict()
    return response, 201

@bp.get("")
def get_all_author():
    query = db.select(Author)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Author.title.ilike(f"%{name_param}%"))

    query = query.order_by(Author.id)

    authors = db.session.scalars(query)
    # We could also write the line above as:
    # books = db.session.execute(query).scalars()
    authors_response = [author.to_dict() for author in authors]
    
    return authors_response