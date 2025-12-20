import sqlite3 as sq

class CategoriesService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_category(self,category):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.add(category,cursor)
        except sq.Error as e:
            print(f"Kategori eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu {e}")
            
    def update(self,category):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.update(category, cursor)
        except sq.Error as e:
            print(f"Güncelleme sırasında bir veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Güncelleme sırasında beklenmedik bir hata oluştu {e}")

    def delete_category(self,id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.delete(id,cursor)
        except sq.Error as e:
            print(f"Silme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Silme işlemi sırasında beklenmedik bir hata oluştu {e}")

    def get_by_id(self,id):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                if not self.__repository.get_by_id(id,cursor):
                    print(f"{id} ye sahip bir kategori bulunamadı.")
                    return None
                return self.__repository.get_by_id(id,cursor)
        except sq.Error as e:
            print(f"Kategori çekme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            print(f"Kategori çekme işlemi sırasında beklenmedik bir hata oluştu {e}")
        
    def get_all(self):
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                self.__repository.get_all(cursor)
        except sq.Error as e:
            print(f"Kategoriler listelenirken bir veritabanı hatası oluştu {e}")
            return []
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu {e}")
            return []