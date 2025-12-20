class LoansRepository:
    def __init__(self,db):
        self.__db = db

    def add(self,loan):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            INSERT INTO loans(loan_date,due_date,return_date,member_id,book_id) VALUES (?,?,?,?,?)
                            """,
                            (loan.loan_date,
                             loan.due_date,
                             loan.return_date,
                             loan.member_id,
                             loan.book_id,)
                            )
            
    def update(self,id):
        pass

    def delete(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            DELETE * FROM loans WHERE id=?
                            """,
                            (id,)
                            )
            
    def get_by_id(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT * FROM loans WHERE id=?
                            """,
                            (id,)
                            )
            loan = cursor.fetchone()
            return list(loan)
        
    def get_all(self):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT * FROM loans
                            """,
                            )
            loans = cursor.fetchall()
            return [list(loan) for loan in loans]