class MembersService:
    def __init__(self, repository,db):
        self.__repository = repository
        self.__db = db

    def add_member(self, member):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.add(member,cursor)

    def update_member(self, member):
        pass

    def delete_member(self, id):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.delete(id,cursor)

    def get_by_id(self, id):
        with self.__db as conn:
            cursor = conn.cursor()
            return self.__repository.get_by_id(id,cursor)

    def get_all(self):
        with self.__db as conn:
            cursor = conn.cursor()
            return self.__repository.get_all(cursor)