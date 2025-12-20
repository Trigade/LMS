class PublishersRepository:
    def __init__(self):
        pass

    def add(self, publisher, cursor):
        cursor.execute(
            """
                    INSERT INTO publishers(name,address,phone) VALUES (?,?,?)
                        """,
            (
                publisher.name,
                publisher.address,
                publisher.phone,
            ),
        )

    def update(self, publisher, cursor):
        cursor.execute(
            """
                    UPDATE publishers SET name=?,address=?,phone=?  WHERE id=?
                        """,
            (
                publisher.name,
                publisher.address,
                publisher.phone,
                publisher.id,
            ),
        )

    def delete(self, id, cursor):
        cursor.execute(
            """
                DELETE FROM publishers WHERE id=?
        """,
            (id,),
        )

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                        SELECT * FROM publishers WHERE id=?
                            """,
            (id,),
        )
        publisher = cursor.fetchone()
        return list(publisher) if publisher else None

    def get_all(self, cursor):
        cursor.execute("""
                            SELECT * FROM publishers
                            """)
        publishers = cursor.fetchall()
        return [list(publisher) for publisher in publishers]
