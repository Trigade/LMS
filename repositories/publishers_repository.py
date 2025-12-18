class PublishersRepository:
    def __init__(self,db):
        self.__db = db

    def add(self,publisher):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                    INSERT INTO publishers(name,address,phone) VALUES (?,?,?)
                        """,
                        (publisher.name,
                         publisher.address,
                         publisher.phone,
                         )
                        )
            
    def update(self, book):
        pass

    def delete(self, id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                DELETE FROM publishers WHERE id=?
        """,
                (id,)
            )

    def get_by_id(self, id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                        SELECT * FROM publishers WHERE id=?
                            """,
                            (id,)
                            )
        publisher = cursor.fetchone()
        return list(publisher)
    
    def get_all(self):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT * FROM publishers
                            """)
            publishers = cursor.fetchall()
            return [list(publisher) for publisher in publishers]