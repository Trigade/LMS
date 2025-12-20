class CategoriesRepository:
    def __init__(self,db):
        self.__db = db

    def add(self,category):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                        INSERT INTO categories(category_name,description) VALUES(?,?)
                            """,
                            (category.category_name,
                             category.description,)
                            )
            
    def update(self,id):
        pass

    def delete(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            DELETE * FROM categories WHERE id=?
                            """,
                            (id,)
                            )

    def get_by_id(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                        SELECT * FROM categories WHERE id=?
                            """,
                            (id,)
                            )
            category = cursor.fecthone()
            return list(category)
        
    def get_all(self):
        with self._db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT * FROM categories
                            """)
            categories = cursor.fetchall()
            return [list(category) for category in categories]