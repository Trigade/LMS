class FinesService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_fine(self,fine):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.add(fine,cursor)

    def update(self):
        pass

    def delete_fine(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.delete(id,cursor)

    def get_by_id(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            return self.__repository.get_by_id(id,cursor)
    
    def get_all(self):
        with self.__db as conn:
            cursor = conn.cursor()
            return self.__repository.get_all(cursor)