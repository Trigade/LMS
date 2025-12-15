class BooksRepository:
    def __init__(self,db):
        self.__db = db

    def add(self,book):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO books(title,isbn,publish_year,stock_quantity,publisher_id,category_id) VALUES(?,?,?,?,?,?) 
            """,book.title,book.isbn,book.publish_year,book.stock_quantity,book.publisher_id,book.category_id)

    def update(self,book):
        pass

    def delete(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM books WHERE id=?
        """,id)
        
    def get_by_id(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM books WHERE id=? 
            """,id)
            book = cursor.fetchone()
            return book

    def get_all(self):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM books
            """)
            books = cursor.fetchall()
            return books