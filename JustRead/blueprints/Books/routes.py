from flask import render_template, redirect, request, Blueprint
from flask_login import login_required, current_user

from JustRead.forms import FilterBookForm, AddBookForm, BuyBookForm
from JustRead.models import Book, Order, BookOrder, Booksforsale
from JustRead.queries import get_books_by_filters, get_book_by_pk, insert_book_order, update_book_availability, get_orders_by_customer_pk, insert_book, insert_booksForSale

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


@Books.route('/books/buy/<pk>', methods=['GET', 'POST'])
@login_required
def buy_book(pk):
    form = BuyBookForm()
    book = get_book_by_pk(pk)
    if request.method == 'POST':
        if form.validate_on_submit():
            order = BookOrder(dict(book_pk=book.pk, bookstore_pk=book.bookstore_pk, customer_pk=current_user.pk))
            insert_book_order(order)
            # Additional logic specific to Book
            update_book_availability(available=False,
                        book_pk=book.pk,
                        bookstore_pk=book.bookstore_pk)
        return redirect('/books')
    return render_template('pages/buy-book.html', form=form, book=book)


@Books.route('/books/your-orders')
def your_orders():
    orders = get_orders_by_customer_pk(current_user.pk)
    return render_template('pages/your-orders.html', orders=orders)

@Books.route("/add-book", methods=['GET', 'POST'])
@login_required
def add_book():
    form = AddBookForm()
    if request.method == 'POST':
        print("gres")
        if form.validate_on_submit():
            print("gres2")
            book_data = dict(
                title=form.title.data,
                authors=form.authors.data,
                categories=form.categories.data,
                thumbnail=form.thumbnail.data,
                description=form.description.data,
                published_year=form.published_year.data,
                average_rating=form.average_rating.data,
                num_pages=form.num_pages.data,
                ratings_count=form.ratings_count.data
            )
            book = Book(book_data)
            new_book_pk = insert_book(book)
            sell = Booksforsale(dict(bookstore_pk=current_user.pk, books_pk=new_book_pk, available=True))
            insert_booksForSale(sell)
            return redirect('/books')
    return render_template('pages/add-book.html', form=form)


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
