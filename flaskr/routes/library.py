from flask import Blueprint, render_template, request

library_route = Blueprint('library', __name__)

@library_route.route("/", methods=['GET', 'POST'])
def show_books():
    if request.method == 'POST':
        book_data = {
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'genre': request.form.get('genre')
        }
        return render_template('library/index.html', books=[book_data])
    return render_template('library/index.html')

@library_route.route("/<int:book_id>")
def book_detail(book_id):
    return render_template('library/index.html', book_id=book_id)