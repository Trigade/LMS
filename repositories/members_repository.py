class MembersReporsitory:
    def __init__(self, db):
        self.__db = db

    def add(self, member):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    INSERT INTO members(first_name,last_name,email,phone,join_date,membership_status) VALUES (?,?,?,?,?)
            """,
                member.first_name,
                member.last_name,
                member.email,
                member.phone,
                member.phone,
                member.join_date,
                member.membersip_status,
            )
            print("Uye barasiyla eklendi")

    def update(self, member):
        pass

    def delete(self, id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                DELETE FROM books WHERE id=?
        """,
                (id,),
            )

    def get_by_id(self, id):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT * FROM members WHERE id = ?
        """,
                (id,),
            )
        member = cursor.fetchone()
        return list(member)

    def get_all(self):
        with self.__db as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT * FROM members
                """)
            members = cursor.fetchall()
            return [list(member) for member in members]
