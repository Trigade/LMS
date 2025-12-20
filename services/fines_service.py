import sqlite3 as sq

class FinesService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_fine(self,fine):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.add(fine,cursor)
        except sq.Error as e:
            print(f"Ceza eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu {e}")

    def update(self,fine):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.update(fine, cursor)
        except sq.Error as e:
            print(f"Ceza eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Ceza eklenirken beklenmedik bir hata oluştu {e}")

    def delete_fine(self,id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.delete(id,cursor)
        except sq.Error as e:
            print(f"Ceza silinirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Ceza silinirken beklenmedik bir hata oluştu {e}")

    def get_by_id(self,id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                if not self.__repository.get_by_id(id,cursor):
                    return None
                return self.__repository.get_by_id(id,cursor)
        except sq.Error as e:
            print(f"Ceza görüntülenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Ceza görüntülenirken beklenmedik bir hata oluştu {e}")
    
    def get_all(self):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                return self.__repository.get_all(cursor)
        except sq.Error as e:
            print(f"Cezalar listelenirken bir veritabanı hatası oluştu {e}")
            return []
        except Exception as e:
            print(f"Cezalar listelenirken beklenmedik bir hata oluştu {e}")
            return []