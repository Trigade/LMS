class CategoriesService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_category(self,category):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.add(category,cursor)
            
    def update(self,id):
        pass

    def delete_category(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.delete(id,cursor)

    def get_by_id(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.get_by_id(id,cursor)
        
    def get_all(self):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.get_all(cursor)