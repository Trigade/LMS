class MembersRepository:
    def __init__(self):
        pass

    def add(self, member, cursor):
        cursor.execute(
            """
                INSERT INTO members(first_name, last_name, email, phone) 
                VALUES (?, ?, ?, ?)
                """,
            (member.first_name, member.last_name, member.email, member.phone),
        )

    def update(self, member, cursor):
        cursor.execute(
            """
                        UPDATE members SET first_name=?,last_name = ?,email =?,phone=? WHERE id = ?
                        """,
            (
                member.first_name,
                member.last_name,
                member.email,
                member.phone,
                member.id,
            ),
        )

    def delete(self, id, cursor):
        cursor.execute(
            """
                DELETE FROM members WHERE id=?
        """,
            (id,),
        )

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                SELECT * FROM members WHERE id = ?
        """,
            (id,),
        )

        member = cursor.fetchone()
        return list(member) if member else None

    def get_all(self, cursor):
        cursor.execute("""
                            SELECT * FROM members
                """)
        members = cursor.fetchall()
        return [list(member) for member in members]
