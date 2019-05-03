from flask import Flask
app = Flask(__name__)

import json

book_list = [
    {
        "id": "1",
        "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "pages": 432,
        "authorId": "10"
    },
    {
        "id": "2",
        "title": "Clean Architecture: A Craftsman's Guide to Software Structure and Design",
        "pages": 432,
        "authorId": "10"
    },
    {
        "id": "3",
        "title": "Grokking Algorithms: An illustrated guide for programmers and other curious people",
        "pages": 256,
        "authorId": "11"
    }
]

@app.route('/books')
def books():
    return app.response_class(
        response=json.dumps(book_list),
        status=200,
        mimetype='application/json'
    )

@app.route('/books/<book_id>')
def book(book_id):
    selected_book = None
    if book_id == "1":
        selected_book = book_list[0]
    elif book_id == "2":
        selected_book = book_list[1]
    elif book_id == "3":
        selected_book = book_list[2]
    
    if selected_book is None:
        return '', 404
    
    return app.response_class(
        response=json.dumps(selected_book),
        status=200,
        mimetype='application/json'
    )
