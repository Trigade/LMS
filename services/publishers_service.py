import sqlite3 as sq

class PublishersService:
    def __init__(self, repository, db):
        self.__repository = repository
        self.__db = db

    def add_publisher(self, publisher):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.add(publisher, cursor)
        except sq.Error as e:
            print(f"Yayıncı eklenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Yayıncı eklenirken beklenmedik bir hata oluştu {e}")

    def update(self, publisher):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.update(publisher, cursor)
        except sq.Error as e:
            print(f"Yayıncı güncellenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Yayıncı güncellenirken beklenmedik bir hata oluştu {e}")

    def delete_publisher(self, id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.delete(id, cursor)
        except sq.Error as e:
            print(f"Yayıncı silinirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Yayıncı silinirken beklenmedik bir hata oluştu {e}")

    def get_by_id(self, id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                if not self.__repository.get_by_id(id,cursor):
                    return None
                return self.__repository.get_by_id(id, cursor)
        except sq.Error as e:
            print(f"Yayıncı görüntülenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Yayıncı görüntülenirken beklenmedik bir hata oluştu {e}")

    def get_all(self):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                return self.__repository.get_all(cursor)
        except sq.Error as e:
            print(f"Yayıncılar listelenirken bir veritabanı hatası oluştu {e}")
            return []
        except Exception as e:
            print(f"Yayıncılar listelenirken beklenmedik bir hata oluştu {e}")
            return []
