from flask import render_template, redirect, request, Blueprint
from flask_login import login_required, current_user

from JustRead.forms import FilterBookForm, AddBookForm, BuyBookForm, DeleteBookForm
from JustRead.models import Book, Order, BookOrder, Booksforsale
from JustRead.queries import get_books_by_filters, get_book_by_pk, insert_book_order, update_book_availability, get_orders_by_customer_pk, insert_book, insert_booksForSale, delete_book

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


@Books.route('/books/delete/<pk>', methods=['GET', 'POST'])
@login_required
def delete_book2(pk):
    form = DeleteBookForm()
    book = get_book_by_pk(pk)
    if request.method == 'POST':
        if form.validate_on_submit():
            delete_book(book.pk)
            # Additional logic specific to Book
            update_book_availability(available=False,
                        book_pk=book.pk,
                        bookstore_pk=book.bookstore_pk)
            return redirect('/books')
    return render_template('pages/delete-book.html', form=form, book=book)

@Books.route('/books/your-orders')
def your_orders():
    orders = get_orders_by_customer_pk(current_user.pk)
    return render_template('pages/your-orders.html', orders=orders)

@Books.route("/add-book", methods=['GET', 'POST'])
@login_required
def add_book():
    form = AddBookForm()
    if request.method == 'POST':
        if form.validate_on_submit():
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

