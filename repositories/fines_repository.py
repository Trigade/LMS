class FinesRepository:
    def __init__(self):
        pass

    def add(self, fine, cursor):
        cursor.execute(
            """
                            INSERT INTO fines(amount,payment_status,loan_id) VALUES (?,?,?)
                            """,
            (
                fine.amount,
                fine.payment_status,
                fine.loan_id,
            ),
        )

    def update(self, id):
        pass

    def delete(self, id, cursor):
        cursor.execute(
            """
                            DELETE * FROM fines WHERE id=?
                            """,
            (id,),
        )

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                            SELECT * FROM fines WHERE id=?
                            """,
            (id,),
        )
        fine = cursor.fetchone()
        return list(fine)

    def get_all(self, cursor):
        cursor.execute(
            """
                            SELECT * FROM fines
                            """,
        )
        fines = cursor.fetchall()
        return [list(fine) for fine in fines]
