class MembersService:
    def __init__(self, repository):
        self.__repository = repository

    def add_member(self, member):
        self.__repository.add(member)

    def update_member(self, member):
        pass

    def delete_member(self, id):
        self.__repository.delete(id)

    def get_by_id(self, id):
        return self.__repository.get_by_id(id)

    def get_all(self):
        return self.__repository.get_all()