class FinesService:
    def __init__(self,repository):
        self.__repository = repository

    def add_fine(self,fine):
        self.__repository.add(fine)

    def update(self):
        pass

    def delete_fine(self,id):
        self.__repository.delete(id)

    def get_by_id(self,id):
        return self.__repository.get_by_id(id)
    
    def get_all(self):
        return self.__repository.get_all()