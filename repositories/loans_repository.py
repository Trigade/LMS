class LoansRepository:
    def __init__(self):
        pass

    def add(self, loan, cursor):
        cursor.execute(
            """
                            INSERT INTO loans(loan_date,due_date,return_date,member_id,book_id) VALUES (?,?,?,?,?)
                            """,
            (
                loan.loan_date,
                loan.due_date,
                loan.return_date,
                loan.member_id,
                loan.book_id,
            ),
        )

    def update(self, loan, cursor):
        cursor.execute(
            """
                        UPDATE loans SET loan_date=?,due_date=?,return_date=?,member_id=?,book_id=? WHERE id=?
                        """,
            (
                loan.loan_date,
                loan.due_date,
                loan.return_date,
                loan.member_id,
                loan.book_id,
                loan.id,
            ),
        )

    def delete(self, id, cursor):
        cursor.execute(
            """
                            DELETE FROM loans WHERE id=?
                            """,
            (id,),
        )

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                            SELECT * FROM loans WHERE id=?
                            """,
            (id,),
        )
        loan = cursor.fetchone()
        return list(loan) if loan else None

    def get_all(self, cursor):
        cursor.execute(
            """
                            SELECT * FROM loans
                            """,
        )
        loans = cursor.fetchall()
        return [list(loan) for loan in loans]
