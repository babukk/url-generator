
from flask import request, jsonify, Response
import json
from slugify import slugify

from . import app, db
from models import Book, book_schema

# --------------------------------------------------------------------------------------------------
@app.route('/books/api/v1.0/book', methods=['POST'])
def create_book():

    author = request.json['author']
    title = request.json['title']
    description = request.json['description']

    new_book = Book(title, author, description)

    db.session.add(new_book)
    db.session.commit()

    # print repr(new_book)

    return book_schema.jsonify(new_book), 201

# --------------------------------------------------------------------------------------------------
@app.route('/books/api/v1.0/book', methods=['GET'])
def get_books():
    books = []

    query = db.session.query(Book)
    books = query.all()
    print repr(books)

    print books[1]['author']

    return Response(
        status=200,
        mimetype="application/json",
        response=json.dumps([e.serialize() for e in books]) + "\n"
    )

# --------------------------------------------------------------------------------------------------
@app.route('/books/api/v1.0/make_slug/<id>', methods=['PUT'])
def slug_book(id):
    query = db.session.query(Book)
    book = query.filter_by(id=id).first()

    if book.slug:
        slug = book.slug
    else:
        slug = slugify(str(id) + "_" + book['title'])
        book.slug = slug
        db.session.commit()

    return Response(
        status=201,
        mimetype="application/json",
        response=json.dumps({'slug': slug,}) + "\n"
    )

# --------------------------------------------------------------------------------------------------
@app.route('/books/api/v1.0/get_book/<slug>', methods=['GET'])
def get_book(slug):
    query = db.session.query(Book)
    book = query.filter_by(slug=slug).first()

    return Response(
        status=200,
        mimetype="application/json",
        response=json.dumps({'book': book.serialize(),}) + "\n"
    )
