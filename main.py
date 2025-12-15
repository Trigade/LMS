from database.db_service import DbService
from core.entities.books import Books
from services.books_service import BooksService
from repositories.books_repository import BooksRepository

db_service = DbService()
db_service.initialize_database()
conn = db_service.get_db_connection()

new_book = Books("Atakan","123456",2025,5,242,1)
book_repository = BooksRepository(conn)
book_service = BooksService(book_repository)
book_service.add_book(new_book)

print(book_service.get_book(1))