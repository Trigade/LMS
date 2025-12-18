class PublishersService:
    def __init__(self,repository):
        self.__repository = repository

    def add_publisher(self,publisher):
        self.__repository.add(publisher)
            
    def update(self, book):
        pass

    def delete_publisher(self, id):
        self.__repository.delete(id)

    def get_by_id(self, id):
        return self.__repository.get_by_id(id)
    
    def get_all(self):
        return self.__repository.get_all()