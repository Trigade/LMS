class CategoriesRepository:
    def __init__(self):
        pass

    def add(self, category, cursor):
        cursor.execute(
            """
                        INSERT INTO categories(category_name,description) VALUES(?,?)
                            """,
            (
                category.category_name,
                category.description,
            ),
        )

    def update(self, category, cursor):
        cursor.execute(
            """
                        UPDATE categories SET category_name=?,description=? WHERE id=?
                        """,
            (
                category.category_name,
                category.description,
                category.id,
            ),
        )

    def delete(self, id, cursor):
        cursor.execute(
            """
                            DELETE FROM categories WHERE id=?
                            """,
            (id,),
        )

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                        SELECT * FROM categories WHERE id=?
                            """,
            (id,),
        )
        category = cursor.fetchone()
        return list(category) if category else None

    def get_all(self, cursor):
        cursor.execute("""
                            SELECT * FROM categories
                            """)
        categories = cursor.fetchall()
        return [list(category) for category in categories]
