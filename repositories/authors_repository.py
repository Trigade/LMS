class AuthorsRepository:
    def __init__(self):
        pass

    def add(self, author, cursor):
        cursor.execute(
            """
                            INSERT INTO authors(first_name,last_name,biography) VALUES (?,?,?)
                            """,
            (
                author.first_name,
                author.last_name,
                author.biography,
            ),
        )

    def update(id, author, cursor):
        cursor.execute(
            """
                        UPDATE authors SET first_name = ?,last_name=?,biography=?, WHERE id = ?
                    """,
            (
                author.first_name,
                author.last_name,
                author.biography,
                author.id,
            ),
        )

    def delete(self, id, cursor):
        cursor.execute(
            """
                            DELETE FROM authors WHERE id=?
                            """,
            (id,),
        )

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                            SELECT * FROM authors WHERE id=?
                            """,
            (id,),
        )
        author = cursor.fetchone()
        return list(author)

    def get_all(self, cursor):
        cursor.execute("""
                            SELECT * FROM authors
                            """)
        authors = cursor.fetchall()
        return [list(author) for author in authors]
