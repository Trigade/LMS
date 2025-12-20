import sqlite3 as sq

class AuthorsService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_author(self,author):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.add(author, cursor)
                print("Yazar başarıyla eklendi")
        except sq.Error as e:
            print(f"Yazar eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu {e}")
    
    def update_author(self,author):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.update(author, cursor)
                print("Yazar başarıyla güncellendi")
        except sq.Error as e:
            print(f"Güncelleme sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Güncelleme sırasında beklenmeyen bir hata oluştu {e}")

    def delete_author(self,id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.delete(id,cursor)
                print("Yazar başarıyla silindi")
        except sq.Error as e:
            print(f"Silme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Silme işlemi sırasında beklenmeyen bir hata oluştu {e}")

    def get_by_id(self,id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                if not self.__repository.get_by_id(id,cursor):
                    print(f"{id} için yazar bulunamadı")
                    return None
                return self.__repository.get_by_id(id,cursor)
        except sq.Error as e:
            print(f"Veri çekilirken veritabanı hatası oluştu {e}")
            return None
        except Exception as e:
            print(f"Veri çekilirken beklenmeyen bir hata oluştu {e}")
            return None
        
    def get_all(self):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                return self.__repository.get_all(cursor)
        except sq.Error as e:
            print(f"Yazarlar listelenirken veritabanı hatası: {e}")
            return []
        except Exception as e:
            print(f"Hata: {e}")
            return []