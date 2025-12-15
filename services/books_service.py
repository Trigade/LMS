class BooksService:
    def __init__(self,repository):
        self.__repository = repository

    def add_book(self,book):
        self.__repository.add(book)

    def update_book(self,book):
        pass

    def delete_book(self,id):
        self.__repository.delete(id)
        
    def get_book(self,id):
        return self.__repository.get_by_id(id)

    def get_books(self):
        return self.__repository.get_all()