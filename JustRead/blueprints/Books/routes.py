from flask import render_template, request, Blueprint
from flask_login import login_required, current_user

from JustRead.forms import FilterBookForm, AddBookForm
from JustRead.models import Book, Order
from JustRead.queries import get_books_by_filters

Books = Blueprint('book', __name__)




@Books.route("/books", methods=['GET', 'POST'])
def books():
    form = FilterBookForm()
    title = 'Our books!'
    books = []
    if request.method == 'GET':
        books = get_books_by_filters()
        #title = f'Our {request.form.get("category")}!'
    return render_template('pages/book.html', books=books)


# @Books.route("/add-book", methods=['GET', 'POST'])
# @login_required
# def add_book():
#     form = AddBookForm()
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             book_data = dict(
#                 isbn13=form.isbn13.data,
#                 title=form.title.data,
#                 subtitle=form.subtitle.data,
#                 categories=form.categories.data,
#                 thumbnail=form.thumbnail.data,
#                 description=form.description.data,
#                 published_year=form.published_year.data,
#                 average_rating=form.average_rating.data,
#                 num_pages=form.num_pages.data,
#                 ratings_count=form.ratings_count.data
#             )
#             book = Book(**book_data)
#             insert_book(book)
#     return render_template('pages/add-book.html', form=form)

# @Books.route("/your-books", methods=['GET', 'POST'])
# @login_required
# def your_books():
#     form = FilterBookForm()
#     books = []
#     if request.method == 'GET':
#         books = Book.query.filter_by(user_id=current_user.id).all()
#     if request.method == 'POST':
#         books = get_books_by_filters(category=request.form.get('category'),
#                                      title=request.form.get('title'),
#                                      author=request.form.get('author'),
#                                      year=request.form.get('year'),
#                                      rating=request.form.get('rating'),
#                                      user_id=current_user.id)
#     return render_template('pages/your-books.html', form=form, books=books)

# @Books.route('/books/order/<isbn13>', methods=['GET', 'POST'])
# @login_required
# def order_book(isbn13):
#     form = OrderBookForm()
#     book = Book.query.filter_by(isbn13=isbn13).first()
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             order_data = dict(
#                 isbn13=book.isbn13,
#                 user_id=current_user.id,
#                 address=form.address.data,
#                 date=form.date.data
#             )
#             order = Order(**order_data)
#             insert_order(order)
#     return render_template('pages/order-book.html', form=form, book=book)

# @Books.route('/books/your-orders')
# @login_required
# def your_orders():
#     orders = Order.query.filter_by(user_id=current_user.id).all()
#     return render_template('pages/your-orders.html', orders=orders)
