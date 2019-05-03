from flask import Flask
app = Flask(__name__)

import json


author_list = [
    {
        "id": "10",
        "name": "Robert C. Martin",
        "about": "Robert C. Martin (“Uncle Bob”) has been a programmer since 1970. He is founder of Uncle Bob Consulting, LLC, and cofounder with his son Micah Martin of The Clean Coders LLC. Martin has published dozens of articles in various trade journals and is a regular speaker at international conferences and trade shows. He has authored and edited many books, including: Designing Object Oriented C++ Applications Using the Booch Method, Patterns Languages of Program Design 3, More C++ Gems, Extreme Programming in Practice, Agile Software Development: Principles, Patterns, and Practices, UML for Java Programmers, Clean Code, and The Clean Coder. A leader in the industry of software development, Martin served for three years as editor-in-chief of the C++ Report, and he served as the first chairman of the Agile Alliance."
    },
    {
        "id": "11",
        "name": "Aditya Bhargava",
        "about": "Aditya Bhargava is a Software Engineer with a dual background in Computer Science and Fine Arts. He blogs about programming at adit.io."
    }
]


@app.route("/authors")
def authors():
    return app.response_class(
        response=json.dumps(author_list),
        status=200,
        mimetype='application/json'
    )


@app.route("/authors/<author_id>")
def author(author_id):
    selected_author = None
    if author_id == "10":
        selected_author = author_list[0]
    elif author_id == "11":
        selected_author = author_list[1]
    
    if selected_author is None:
        return '', 404

    return app.response_class(
        response=json.dumps(selected_author),
        status=200,
        mimetype='application/json'
    )
