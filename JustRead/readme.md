# Just Read
## Initialization

Clone / download repository files and run the following to install the required packages (preferably within a venv):
	pip install -r requirements.txt

Create a new database in pgAdmin named Just Read and create an .env file and add the following to the env.file:
	SECRET_KEY=<secret_key>
	DB_USERNAME=postgres || <postgres_user_name>
	DB_PASSWORD=<postgres_user_password>
	DB_NAME=Just Read || <postgres_db_name>

When all this information is present (and correct) the server can be started with:
	flask run

## Folder setup

The app is divided into multiple folders similar to the structure of the Green Groceries example project, with a few tweaks:

- blueprints: Contains the separate blueprints of the app (with the submodules Books and Login containing different parts of the functionality)
- dataset: Contains the books.csv file used to import the book data
- static: Contains static files such as images and css
- templates: Contains all html files that are displayed in the user browser
- utils: Contains the sql files and script that generate the postgresql database. This folder further includes a script that generates custom choice objects for Flask forms. These choice objects are created based on the books dataset, allowing us to populate select fields in forms with relevant options.

At the root folder of the app (./JustRead) six more scripts are present with the following roles:

- __init__.py: Initializes the flask app and creates a connection to the database (and a cursor object for future queries)
- app.py: Runs the app created by __init__.py
- filters.py: Implements custom template filters for nicer formatting of data in the frontend
- forms.py: Implements forms used to save data from users
- models.py: Implements custom classes for each of the database tables to store data in a clean OOP manner
- queries.py: Implements functions for each needed query to the database used inside the app

## Routes 
Both implemented blueprints come with a routes.py file that initialize a Blueprint object and define routes for the app.

- Login:
	- __/home__: Home page
	- __/about__: About page
	- __/style-guide__: Style guide (displays all html elements used)
	- __/login__: User login page
	- __/signup__: User signup (creation) page
	- __/logout__: Logs user out and sends back to login page

- Books:
	- __/books__: Page for books in the database
	- __/books/buy/<pk>__: Page for books in the database
	- __/books/delete/<pk>__: Page for deleting book from the database
	- __/books/your-orders__: Page for your orders in the database
	- __/books/add-book__: Page for adding book in the database

## How to interact with our web-app
- As a customer: go to the top, right-hand corner and press “Sign up”. Enter your details and choose “Customer” at the bottom and press “Sign up”. Then you can press “Browse books” or “All books” to see available books, or you can view your orders by pressing “Your orders”. If you wish to buy a book, simply press “Buy book” and then “Yes, buy it”. This will move your chosen book to the “Your orders”.
- As a courier: go to the top, right-hand corner and press “Sign up”. Enter your details and choose “Courier” at the bottom and press “Sign up”. Then you can press “Your orders” to view orders.
- As a bookstore: go to the top, right-hand corner and press “Sign up”. Enter your details and choose “Bookstore” at the bottom and press “Sign up”. Then you can add books using “Add books”  at the top menu bar, or if you go to “All books” you can also delete books.

# Known issues
- We meant to implement the E/R diagram as included in the folder. However, due to the time constraints of this assignment, we did not manage to do this fully. Therefore the “rating” relation has not been implemented completely and in our project only book stores can rate a book when adding a book. Thus the customer can give ratings to neither book stores nor to books.
- Furthermore, we have included, but not fully implemented the courier entity. This is also due to the time constraints of this assignment as well as to the complexity of such an implementation.
- Finally, it should be noted that all features are visible to all the different types of users, but they are only interactable for the relevant user. I.e. the “Add books” option is available to all users, but only a book store can actually use it.
