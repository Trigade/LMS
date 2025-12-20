class PublishersService:
    def __init__(self, repository, db):
        self.__repository = repository
        self.__db = db

    def add_publisher(self, publisher):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.add(publisher, cursor)

    def update(self, publisher):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.update(publisher, cursor)

    def delete_publisher(self, id):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.delete(id, cursor)

    def get_by_id(self, id):
        with self.__db as conn:
            cursor = conn.cursor()
            return self.__repository.get_by_id(id, cursor)

    def get_all(self):
        with self.__db as conn:
            cursor = conn.cursor()
            return self.__repository.get_all(cursor)
