import sqlite3 as sq

class MembersService:
    def __init__(self, repository,db):
        self.__repository = repository
        self.__db = db

    def add_member(self, member):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.add(member,cursor)
        except sq.Error as e:
            print(f"Üye eklenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Üye eklenirken beklenmedik bir hata oluştu {e}")

    def update_member(self, member):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.update(member, cursor)
        except sq.Error as e:
            print(f"Üye güncelleme işlemi sırasında bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Üye güncelleme işlemi sırasında beklenmedik bir hata oluştu {e}")

    def delete_member(self, id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.delete(id,cursor)
        except sq.Error as e:
            print(f"Üye silme işlemi sırasında bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Üye silme işlemi sırasında beklenmedik bir hata oluştu {e}")

    def get_by_id(self, id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                if not self.__repository.get_by_id(id,cursor):
                    return None
                return self.__repository.get_by_id(id,cursor)
        except sq.Error as e:
            print(f"Üye görüntülenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Üye görüntülenirken beklenmedik bir hata oluştu {e}")

    def get_all(self):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                return self.__repository.get_all(cursor)
        except sq.Error as e:
            print(f"Üyeler listelenirken bir veritabanı hatası oluştu {e}")
            return []
        except Exception as e:
            print(f"Üyeler listelenirken beklenmedik bir hata oluştu {e}")
            return []