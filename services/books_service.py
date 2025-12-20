import sqlite3 as sq

class BooksService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db
    def add_book(self,book):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.add(book,cursor)
                print("Kitap eklendi")
        except sq.Error as e:
            print(f"Kitap eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu {e}")

    def update_book(self,book):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.update(book, cursor)
                print("Kitap başarıyla güncellendi")
        except sq.Error as e:
            print(f"Güncelleme sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Güncelleme sırasında beklenmedik bir hata oluştu {e}")

    def delete_book(self,id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.delete(id,cursor)
                print("Silme işlemi başarılı")
        except sq.Error as e:
            print(f"Silme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Silme işlemi sırasında beklenmedik bir hata oluştu {e}")
        
    def get_book(self,id):
        try:    
            with self.__db as conn:
                cursor = conn.cursor()
                if not self.__repository.get_by_id(id,cursor):
                    print(f"{id} ye ait bir kitap bulunamadı")
                    return None
                return self.__repository.get_by_id(id,cursor)
        except sq.Error as e:
            print(f"Veri çekme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Veri çekme işlemi sırasında bir hata oluştu {e}")

    def get_books(self):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                return self.__repository.get_all(cursor)
        except sq.Error as e:
            print(f"Kitaplar listelenirken veritabanı hatası oluştu {e}")
            return []
        except Exception as e:
            print(f"Kitaplar listelenirken bir hata oluştu {e}")
            return []