from database.db_service import DbService
#from core.entities.books import Books
#from services.books_service import BooksService
#from repositories.books_repository import BooksRepository
from core.entities.members import Members
from services.members_service import MembersService
from repositories.members_repository import MembersRepository

db_service = DbService()
db_service.initialize_database()
conn = db_service.get_db_connection()

"""new_book = Books("Atakan","123456",2025,5,242,1)
book_repository = BooksRepository(conn)
book_service = BooksService(book_repository)
book_service.add_book(new_book)

print(book_service.get_book(1))"""

new_member = Members("Mustafa","Kaya","mkaya2514@gmail.com","5436535259")
member_repository = MembersRepository(conn)
member_service = MembersService(member_repository)
member_service.add_member(new_member)
