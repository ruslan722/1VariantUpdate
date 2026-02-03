import pandas as pd
from peewee import OperationalError
from connect import db, Tovar, User, Zakaz, Punkt


def clean_int(value):
    """Преобразует строку с пробелами в целое число."""
    if pd.isna(value):
        return 0
    try:
        clean_str = str(value).replace(' ', '').replace('\xa0', '')
        return int(float(clean_str))
    except (ValueError, TypeError):
        return 0

def clean_str(value):
    """Преобразует пустые значения (NaN) в пустую строку."""
    if pd.isna(value):
        return ""
    return str(value).strip()

def clean_date(value):
    """Преобразует дату в строку формата ДД.ММ.ГГГГ."""
    if pd.isna(value):
        return None
    try:
        
        return pd.to_datetime(value).strftime('%d.%m.%Y')
    except Exception:
    
        return str(value)


def import_punkts():
    print(" Импорт пунктов выдачи")
    try:
        
        df = pd.read_excel('Пункты выдачи_import.csv', header=None, engine='openpyxl')
        
        data_list = []
        for _, row in df.iterrows():
            data_list.append({
                'adress': clean_str(row[0]),
               
            })
            
        with db.atomic():
            Punkt.insert_many(data_list).execute()
        print(f"Успешно: {len(data_list)} пунктов.")
    except Exception as e:
        print(f"Ошибка (Пункты): {e}")

def import_tovar():
    print("Импорт товаров ")
    try:
        df = pd.read_excel('Tovar.csv', engine='openpyxl')
        
        data_list = []
        for _, row in df.iterrows():
            full_opis = f"{clean_str(row.get('Наименование товара', ''))} {clean_str(row.get('Описание товара', ''))}"
            
            data_list.append({
                'article': clean_str(row['Артикул']),
                'edinisa': clean_str(row['Единица измерения']),
                'price': clean_int(row['Цена']),
                'postavsik': clean_str(row['Поставщик']),
                'proizvod': clean_str(row['Производитель']),
                'category': clean_str(row['Категория товара']),
                'sale': clean_int(row['Действующая скидка']),
                'kolvo': clean_int(row['Кол-во на складе']),
                'opis': full_opis.strip(),
                'photo': clean_str(row['Фото'])
            })
            
        with db.atomic():
            Tovar.insert_many(data_list).execute()
        print(f"Успешно: {len(data_list)} товаров.")
    except Exception as e:
        print(f"Ошибка (Товары): {e}")

def import_users():
    print(" Импорт пользователей ")
    try:
        df = pd.read_excel('user_import.csv', engine='openpyxl')
        
        data_list = []
        for _, row in df.iterrows():
            data_list.append({
                'role': clean_str(row['Роль сотрудника']),
                'fio': clean_str(row['ФИО']),
                'login': clean_str(row['Логин']),
                'password': clean_str(row['Пароль'])
            })
            
        with db.atomic():
            User.insert_many(data_list).execute()
        print(f"Успешно: {len(data_list)} пользователей.")
    except Exception as e:
        print(f"Ошибка (Пользователи): {e}")

def import_zakaz():
    print(" Импорт заказов ")
    try:
        df = pd.read_excel('Заказ_import.csv', engine='openpyxl')
        
        data_list = []
        for _, row in df.iterrows():
            data_list.append({
                'article': clean_str(row['Артикул заказа']),
             
                'data': clean_date(row['Дата заказа']),
                'data_dostavki': clean_date(row['Дата доставки']),
                'adress': clean_str(row['Адрес пункта выдачи']), 
                'fio': clean_str(row['ФИО авторизированного клиента']),
                'code': clean_int(row['Код для получения']),
                'status': clean_str(row['Статус заказа'])
            })
            
        with db.atomic():
            Zakaz.insert_many(data_list).execute()
        print(f"Успешно: {len(data_list)} заказов.")
    except Exception as e:
        print(f"Ошибка (Заказы): {e}")



if __name__ == "__main__":
    try:
        db.connect()
       
        db.create_tables([Tovar, User, Zakaz, Punkt], safe=True) 
        print("База данных подключена, таблицы проверены.\n")
        
        
        import_punkts()
        import_tovar()
        import_users()
        import_zakaz()
        
        db.close()
        print("\nИмпорт завершен.")
        
    except OperationalError as e:
        print(f"ОШИБКА ПОДКЛЮЧЕНИЯ: Не удалось соединиться с MySQL. Проверьте, запущена ли служба MySQL и создана ли база 'var'.\nДетали: {e}")