from flask import Blueprint, render_template, request, redirect

from models.book import *
from models.book_list import books, add_new_book, delete_book

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def index():
    return render_template("index.jinja", title="Book Page", book_list=books)

@book_blueprint.route("/books", methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return redirect('/books')

@book_blueprint.route('/books/delete/<name>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect('/books')