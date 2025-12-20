class LoansService:
    def __init__(self,repository):
        self.__repository = repository

    def add_loan(self,loan):
        self.__repository.add(loan)
            
    def update(self,id):
        pass

    def delete_loan(self,id):
        self.__repository.delete(id)
            
    def get_by_id(self,id):
        return self.__repository.get_by_id(id)
        
    def get_all(self):
        return self.__repository.get_all()