class CategoriesService:
    def __init__(self,repository):
        self.__repository = repository

    def add_category(self,category):
        self.__repository.add(category)
            
    def update(self,id):
        pass

    def delete_category(self,id):
        self.__repository.delete(id)

    def get_by_id(self,id):
        self.__repository.get_by_id(id)
        
    def get_all(self):
        self.__repository.get_all()