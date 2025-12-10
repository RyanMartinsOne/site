from flask import Blueprint, render_template

library_route = Blueprint('library', __name__)

@library_route.route("/")
def show_books():
    return render_template('library/index.html')

@library_route.route("/<int:book_id>")
def book_detail(book_id):
    return render_template('library/index.html', book_id=book_id)