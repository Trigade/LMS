class AuthorsService:
    def __init__(self,repository):
        self.__repository = repository

    def add_author(self,author):
        self.__repository.add(author)
    
    def update_author():
        pass

    def delete_author(self,id):
        self.__repository.delete(id)

    def get_by_id(self,id):
        return self.__repository.get_by_id(id)
        
    def get_all(self):
        return self.__repository.get_all()