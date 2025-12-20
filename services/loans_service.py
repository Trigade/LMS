import sqlite3 as sq

class LoansService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_loan(self,loan):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.add(loan,cursor)
        except sq.Error as e:
            print(f"Borç eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Borç eklenirken beklenmedik bir hata oluştu {e}")
            
    def update(self,loan):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.update(loan, cursor)
        except sq.Error as e:
            print(f"Borç güncelleme işlemi sırasında bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Borç güncelleme işlemi sırasında beklenmedik bir hata oluştu {e}")

    def delete_loan(self,id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.delete(id,cursor)
        except sq.Error as e:
            print(f"Borç silinirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Borç silinirken beklenmedik bir hata oluştu {e}")
            
    def get_by_id(self,id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                if not self.__repository.get_by_id(id,cursor):
                    return None
                return self.__repository.get_by_id(id,cursor)
        except sq.Error as e:
            print(f"Borç görüntülenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Borç görüntülenirken beklenmedik bir hata oluştu {e}")
        
    def get_all(self):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                return self.__repository.get_all(cursor)
        except sq.Error as e:
            print(f"Borçlar listelenirken bir veritabanı hatası oluştu {e}")
            return []
        except Exception as e:
            print(f"Borçlar listelenirken beklenmedik bir hata oluştu {e}")
            return []