class BooksRepository:
    def __init__(self):
        pass

    def add(self, book, cursor):
        cursor.execute(
            """
                INSERT INTO books(title,isbn,publish_year,stock_quantity,publisher_id,category_id) VALUES(?,?,?,?,?,?) 
            """,
            (
                book.title,
                book.isbn,
                book.publish_year,
                book.stock_quantity,
                book.publisher_id,
                book.category_id,
            ),
        )

    def update(self, book, cursor):
        pass

    def delete(self, id, cursor):
        cursor.execute(
            """
                DELETE FROM books WHERE id=?
        """,
            (id,),
        )

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                SELECT * FROM books WHERE id=? 
            """,
            (id,),
        )
        book = cursor.fetchone()
        return list(book)

    def get_all(self, cursor):
        cursor.execute("""
                SELECT * FROM books
            """)
        books = cursor.fetchall()
        return [list(book) for book in books]
