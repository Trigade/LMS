class AuthorsRepository:
    def __init__(self,db):
        self.__db = db

    def add(self,author):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            INSERT INTO authors(first_name,last_name,biography) VALUES (?,?,?)
                            """,
                            (author.first_name,
                             author.last_name,
                             author.biography,
                             )
                            )
    
    def update():
        pass

    def delete(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            DELETE FROM authors WHERE id=?
                            """,
                            (id,)
                            )

    def get_by_id(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT * FROM authors WHERE id=?
                            """,
                            (id,)
                            )
            author = cursor.fetchone()
            return list(author)
        
    def get_all(self):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT * FROM authors
                            """)
            authors = cursor.fetchall()
            return [list(author) for author in authors]