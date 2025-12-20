class BooksService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db
    def add_book(self,book):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.add(book,cursor)

    def update_book(self,book):
        pass

    def delete_book(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            self.__repository.delete(id,cursor)
        
    def get_book(self,id):
        with self.__db as conn:
            cursor = conn.cursor()
            return self.__repository.get_by_id(id,cursor)

    def get_books(self):
        with self.__db as conn:
            cursor = conn.cursor()
            return self.__repository.get_all(cursor)