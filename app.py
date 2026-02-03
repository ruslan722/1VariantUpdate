import tkinter as tk
from tkinter import Label, PhotoImage, Entry, messagebox
from connect import Tovar_app, App2zakaz, User


root = tk.Tk()
root.title('магазин обуви')
root.geometry('800x600')
root.configure(bg='#ffffff')
root.resizable(False, False)
root.iconbitmap('icon.ico')

def avtorizaciya():
   # код для очистки окна перед открытием
    for widget in root.winfo_children(): 
        widget.destroy()
    avtorizaciya_widow =Label(root, bg='#7fff00', width=65, height=28)

    avtorizaciya_widow.place(x=150, y=100)
    avt = Label(avtorizaciya_widow, text='Авторизация', bg='#7fff00', font=('Times New Roman', 16))
    avt.place(x=160, y=20)
    login = Label(avtorizaciya_widow, text='Логин:', bg='#7fff00', font=('Times New Roman', 16))
    login.place(x=40, y=80)
    login_entry = Entry(avtorizaciya_widow, width=30)
    login_entry.place(x=160, y=83)

    pasword = Label(avtorizaciya_widow, text='Пароль:', bg='#7fff00', font=('Times New Roman', 16))
    pasword.place(x=40, y=140)
    pasword_entry = Entry(avtorizaciya_widow, width=30)
    pasword_entry.place(x=160, y=143)
    def avtorization():
        global id_user
        login = login_entry.get()
        password = pasword_entry.get()

        def get_zap():
            users = User.select() 
            return users
        
        user_list = get_zap()
        for i in user_list:
            if login == i.login and password == i.password:
                id_user = i.id
                messagebox.showinfo('Успех', ' Вы вошли успешно!')
                avtorizaciya_widow.destroy()
                glavnaya()
        

    voiti = Label(avtorizaciya_widow, text='Войти', bg='#00FA9A', width=15, font=('Times New Roman', 16))
    voiti.place(x=20, y=350)
    voiti.bind('<Button-1>', lambda e: avtorization())
    gost = Label(avtorizaciya_widow, text='Войти как гость', bg='#00FA9A', width=15, font=('Times New Roman', 16))
    gost.place(x=235, y=350)
    gost .bind('<Button-1>', lambda e: gosts())
    no_account = Label(avtorizaciya_widow, text='Нет аккаунта? Зарегистрироваться', bg='#7fff00', font=('Times New Roman', 12))
    no_account.place(x=123, y=385)
    no_account.bind('<Button-1>', lambda e: register())

def register():
    for widget in root.winfo_children():
        widget.destroy()
    avtorizaciya_widow =Label(root, bg='#7fff00', width=65, height=28)
    avtorizaciya_widow.place(x=150, y=100)
    avt = Label(avtorizaciya_widow, text='Регистрация', bg='#7fff00', font=('Times New Roman', 16))
    avt.place(x=160, y=20)
    login = Label(avtorizaciya_widow, text='Логин:', bg='#7fff00', font=('Times New Roman', 16))
    login.place(x=40, y=80)
    login_entry = Entry(avtorizaciya_widow, width=30)
    login_entry.place(x=160, y=83)

    pasword = Label(avtorizaciya_widow, text='Пароль:', bg='#7fff00', font=('Times New Roman', 16))
    pasword.place(x=40, y=140)
    pasword_entry = Entry(avtorizaciya_widow, width=30, show='*')
    pasword_entry.place(x=160, y=143)
    def reg():
        login = login_entry.get()
        password = pasword_entry.get()
        _ = User.create(
            login=login,
            password=password
        )
        avtorizaciya_widow.destroy()
        messagebox.showinfo('Успех', 'Вы успешно зарегистрировались!')
        avtorizaciya()


    voiti = Label(avtorizaciya_widow, text='Зарегистрироваться', bg='#00FA9A', width=15, font=('Times New Roman', 16))
    voiti.place(x=20, y=350)
    voiti.bind('<Button-1>', lambda e: reg())
    gost = Label(avtorizaciya_widow, text='Войти как гость', bg='#00FA9A', width=15, font=('Times New Roman', 16))
    gost.place(x=235, y=350)
    no_account = Label(avtorizaciya_widow, text='Есть аккаунт? Войти', bg='#7fff00', font=('Times New Roman', 12))
    no_account.place(x=145, y=385)
    no_account.bind('<Button-1>', lambda e: avtorizaciya())

def gosts():
    global image_obyv
    for widget in root.winfo_children(): 
        widget.destroy()

    messagebox.showerror('Oшибка', 'Данные не загружены')

    messagebox.showwarning('Внимание', 'Вы вошли как гость. Функционал ограничен.')
    
    messagebox.showinfo('Успех', ' Вы вошли успешно!')

    
    doc = Label(root, text=' Список товаров', bg='#00FA9A', font=('Times New Roman', 16), 
                fg='black', width=68, height=2)
    doc.place(x=0, y=5)

    image_obyv = PhotoImage(file='icon.png')
    image_obyv = image_obyv.subsample(15)
    image_obyv_label = Label(doc, image=image_obyv, bg='#00FA9A')
    image_obyv_label.place(x=10, y=2)

    doc_name = Label(doc, text='Магазин обуви', bg='#00fa9a', font=('Times New Roman', 12))
    doc_name.place(x=65, y=5)
    exit = Label(root, text= 'Выйти', bg='#00FA9A', font=('Times New Roman', 12),
                    fg='black', width=10)
    
    exit.place(x=700, y=20)
    exit.bind('<Button-1>', lambda e: avtorizaciya())

def glavnaya():     
    global image_obyv_label, image_obyv
    for widget in root.winfo_children():
        widget.destroy()

    def get_role():
        role = User.get(User.id == id_user)
        return role
    
    

    roles = get_role()


    
    doc = Label(root, text=' Список товаров', bg='#00FA9A', font=('Times New Roman', 16), 
                fg='black', width=68, height=2)
    doc.place(x=0, y=5)

    image_obyv = PhotoImage(file='icon.png')
    image_obyv = image_obyv.subsample(15)
    image_obyv_label = Label(doc, image=image_obyv, bg='#00FA9A')
    image_obyv_label.place(x=10, y=2)

    doc_name = Label(doc, text='Магазин обуви', bg='#00fa9a', font=('Times New Roman', 12))
    doc_name.place(x=65, y=5)
    exit = Label(root, text= 'Выйти', bg='#00FA9A', font=('Times New Roman', 12),
                    fg='black', width=10)
    exit.place(x=700, y=20)


    exit.bind('<Button-1>', lambda e: avtorizaciya())
    name_user = Label(root, text=f' {roles.fio}', bg='#00FA9A', font=('Times New Roman', 12))
    name_user.place(x=600, y=20)


    def magazin():
        content = Tovar_app.select()
        return content
    tovar_list = magazin()
    y_position = 100
    for i in tovar_list:
        info = Label(root, bg='#7fff00', width=100, height=8)
        info.place(x=50, y=y_position)

        photo = PhotoImage(file=f'{i.photo}')
        photo = photo.subsample(5)
        photo_label = Label(info, image=photo, bg='#7fff00')
        photo_label.image = photo
        photo_label.place(x=5, y=8)
        kat_name = Label(info, text=f'{i.category} | {i.name}', bg='#7fff00', font=('Times New Roman', 10))
        kat_name.place(x=160, y=8)
        discription = Label(info, text=f'{i.opis}', bg='#7fff00', font=('Times New Roman', 8))
        discription.place(x=160, y=25)
        proizvod = Label(info, text=f'Производитель: {i.proizvod}', bg='#7fff00', font=('Times New Roman', 8))
        proizvod.place(x=160, y=40)
        price = Label(info, text =f'Цена: {i.price} руб', bg='#7fff00', font=('Times New Roman', 8))
        price.place(x=160, y=55)
        edinisa = Label(info, text=f'Единица измерения: {i.edinisa}', bg='#7fff00', font=('Times New Roman', 8))
        edinisa.place(x=160, y=70)
        kol = Label(info, text=f'Количество на складе: {i.kolvo}', bg='#7fff00', font=('Times New Roman', 8))
        kol.place(x=160, y=85)


        y_position +=130

    def button_add_tovar():
        root_add_tovar = tk.Toplevel()
        root_add_tovar.title('Добавление товара')
        root_add_tovar.geometry('500x500')
        root_add_tovar.configure(bg='#ffffff')
        root_add_tovar.resizable(False, False)
        root_add_tovar.iconbitmap('icon.ico')
        label_photo = Label(root_add_tovar, text='ФОТО', bg='#ffffff', font=('Times New Roman', 12))
        label_photo.place(x=10, y=10)
        entry_photo = Entry(root_add_tovar, width=15)
        entry_photo.place(x=190, y=13)
        label_name = Label(root_add_tovar, text='Название товара', bg='#ffffff', font=('Times New Roman', 12))
        label_name.place(x=10, y=50)
        entry_name = Entry(root_add_tovar, width=15)
        entry_name.place(x=190, y=53)
        category = Label(root_add_tovar, text='Категория товара', bg='#ffffff', font=('Times New Roman', 12))
        category.place(x=10, y=90)
        entry_category = Entry(root_add_tovar, width=15)
        entry_category .place(x=190, y=93)
        label_opis = Label(root_add_tovar, text='Описание товара', bg='#ffffff', font=('Times New Roman', 12))
        label_opis.place(x=10, y=130)
        entry_opis = Entry(root_add_tovar, width=15)
        entry_opis.place(x=190, y=133)
        proizvod = Label(root_add_tovar, text='Производитель', bg='#ffffff', font=('Times New Roman', 12))
        proizvod.place(x=10, y=170)
        entry_proizvod = Entry(root_add_tovar, width=15)
        entry_proizvod.place(x=190, y=173)
        postavsik = Label(root_add_tovar, text='Поставщик', bg='#ffffff', font=('Times New Roman', 12))
        postavsik.place(x=10, y=210)
        entry_postavsik = Entry(root_add_tovar, width=15)
        entry_postavsik.place(x=190, y=213)
        label_price = Label(root_add_tovar, text='Цена', bg='#ffffff', font=('Times New Roman', 12))
        label_price.place(x=10, y=250)
        entry_price = Entry(root_add_tovar, width=15)
        entry_price.place(x=190, y=253)
        label_kolvo = Label(root_add_tovar, text='единица измерения', bg='#ffffff', font=('Times New Roman', 12))
        label_kolvo.place(x=10, y=290)
        entry_kolvo = Entry(root_add_tovar, width=15)
        entry_kolvo.place(x=190, y=293)
        label_edinisa = Label(root_add_tovar, text='Количество на складе', bg='#ffffff', font=('Times New Roman', 12))
        label_edinisa.place(x=10, y=330)
        entry_edinisa = Entry(root_add_tovar, width=15)
        entry_edinisa.place(x=190, y=333)
        dev_sale = Label(root_add_tovar, text='Скидка', bg='#ffffff', font=('Times New Roman', 12))
        dev_sale.place(x=10, y=370)
        entry_sale = Entry(root_add_tovar, width=15)
        entry_sale.place(x=190, y=373)
        article = Label(root_add_tovar, text='Артикул', bg='#ffffff', font=('Times New Roman', 12))
        article.place(x=10, y=410)
        entry_article = Entry(root_add_tovar, width=15)
        entry_article.place(x=190, y=413)
        def add_tovar():
            Tovar_app.create(
                photo=entry_photo.get(),
                article=entry_article.get(),
                name =entry_name.get(),
                category=entry_category.get(),
                opis = entry_opis.get(),
                proizvod=entry_proizvod.get(),
                postavsik=entry_postavsik.get(),
                price=entry_price.get(),
                kolvo=entry_kolvo.get(),
                edinisa=entry_edinisa.get(),
                sale=entry_sale.get()

                
            )
            messagebox.showinfo('Успех', 'Товар добавлен успешно!')
            root_add_tovar.destroy()

        button_add = tk.Button(root_add_tovar, text='Добавить', bg='#00FA9A', width=15, font=('Times New Roman', 12), command= add_tovar)
        button_add.place(x=150, y=450)

    def red_tovar():
        red =tk.Toplevel()
        red.title('Редактировать товар')
        red.geometry('400x500')
        red.resizable(False, False)
        red.configure(bg='#ffffff')

        id_label = Label(red, text='id', bg = '#ffffff', font=('Times New Roman', 12))
        id_label.place(x=10, y=10)
        id_label_entry = Entry(red, width=15)
        id_label_entry.place(x=170, y=10)

        article_label = Label(red, text='Артикл', bg ='#ffffff', font=('Times New Roman', 12))
        article_label.place(x=10, y=40)
        article_label_entry = Entry(red, width=15)
        article_label_entry.place(x=170, y=40)
        edinisa_label = Label(red, text='Единица измерения', bg ='#ffffff', font=('Times New Roman', 12))
        edinisa_label.place(x=10, y=70)
        edinisa_label_entry = Entry(red, width=15)
        edinisa_label_entry.place(x=170, y=70)
        price_label = Label(red, text='Цена', bg= '#ffffff', font=('Times New Roman', 12))
        price_label.place(x=10, y=100)
        price_label_entry = Entry(red, width=15)
        price_label_entry.place(x=170, y=100)
        postavsik_label = Label(red, text='Поставщик', bg= '#ffffff', font=('Times New Roman', 12))
        postavsik_label .place(x=10, y=130)
        postavsik_label_entry = Entry(red, width=15)
        postavsik_label_entry.place(x=170, y=130)
        proizvod_label = Label(red, text='Производитель', bg= '#ffffff', font=('Times New Roman', 12))
        proizvod_label .place(x=10, y=160)
        proizvod_label_entry = Entry(red, width=15)
        proizvod_label_entry.place(x=170, y=160)
        category_label = Label(red, text='Категория', bg= '#ffffff', font=('Times New Roman', 12))
        category_label.place(x=10, y=190)
        category_label_entry = Entry(red, width=15)
        category_label_entry.place(x=170, y=190)
        sale_label = Label(red, text='Скидка', bg= '#ffffff', font=('Times New Roman', 12))
        sale_label.place(x=10, y=220)
        sale_label_entry = Entry(red, width=15)
        sale_label_entry.place(x=170, y=220)
        kolvo_label = Label(red, text='Количество на складе', bg= '#ffffff', font=('Times New Roman', 12))
        kolvo_label.place(x=10, y=250)
        kolvo_label_entry = Entry(red, width=15)
        kolvo_label_entry.place(x=170, y=250)
        opis_label = Label(red, text='Описание', bg= '#ffffff', font=('Times New Roman', 12))
        opis_label.place(x=10, y=280)
        opis_label_entry = Entry(red, width=15)
        opis_label_entry.place(x=170, y=280)
        photo_label = Label(red, text='Фото', bg= '#ffffff', font=('Times New Roman', 12))
        photo_label.place(x=10, y=310)
        photo_label_entry = Entry(red, width=15)
        photo_label_entry.place(x=170, y=310)
        name_label = Label(red, text='Название', bg= '#ffffff', font=('Times New Roman', 12))
        name_label.place(x=10, y=340)
        name_label_entry = Entry(red, width=15)
        name_label_entry.place(x=170, y=340)

        def update_tovar():
            id = id_label_entry.get()
            article = article_label_entry.get()
            edinisa = edinisa_label_entry.get()
            price = price_label_entry.get()
            postavsik = postavsik_label_entry.get()
            proizvod = proizvod_label_entry.get()
            category = category_label_entry.get()
            sale = sale_label_entry.get()
            kolvo = kolvo_label_entry.get()
            opis = opis_label_entry.get()
            photo = photo_label_entry.get()
            name = name_label_entry.get()

            tovar = Tovar_app.get(Tovar_app.id == id)
            tovar.article = article
            tovar.edinisa = edinisa
            tovar.price = price
            tovar.postavsik = postavsik
            tovar.proizvod = proizvod
            tovar.category = category
            tovar.sale = sale
            tovar.kolvo = kolvo
            tovar.opis = opis
            tovar.photo = photo
            tovar.name = name
            tovar.save()
            messagebox.showinfo('Успех', 'Товар отредактирован успешно!')
            red.destroy()

        button_update = tk.Button(red, text='Редактировать', bg='#00FA9A', width=15, font=('Times New Roman', 12), command= update_tovar)
        button_update.place(x=130, y=400)
    
    def delete_tovar():
        del_tovar = tk.Toplevel()
        del_tovar.title('Удаление товара')
        del_tovar.geometry('300x150')
        del_tovar.configure(bg='#ffffff')
        del_tovar.resizable(False, False)

        id_label = Label(del_tovar, text='id', bg='#ffffff', font=('Times New Roman', 12))
        id_label .place(x=10, y=20)
        id_label_entry = Entry(del_tovar, width=15)
        id_label_entry.place(x=120, y=20)

        def delete_tovar_db():
            id = id_label_entry.get()
            tovar = Tovar_app.get(Tovar_app.id == id)
            tovar.delete_instance()
            messagebox.showinfo('Успех', 'Товар удален успешно!')
            del_tovar.destroy()

        delete_button = tk.Button(del_tovar, text='Удалить', bg='#00FA9A', width=15, font=('Times New Roman', 12), command= delete_tovar_db)
        delete_button.place(x=80, y=70)
        


    def zakaz():
        zakaz_window = tk.Toplevel()
        zakaz_window.title('Заказы')
        zakaz_window.geometry('800x600')
        zakaz_window.configure(bg='#ffffff')
        zakaz_window.resizable(False, False)

        def get_zakaz():
            zakazapp_list = App2zakaz.select()
            return zakazapp_list
        zakaz_list = get_zakaz()

        y_position = 50

        for i in zakaz_list:
            info = Label(zakaz_window, bg='#7fff00', width = 90, height=7)
            info.place(x=50, y=y_position)
           

            article = Label(info, text=f'Артикул: {i.article}', bg='#7fff00', font=('Times New Roman', 12))
            article.place(x=10, y=10)
            status = Label(info, text=f'Статус: {i.status}', bg='#7fff00', font=('Times New Roman', 12))
            status.place(x=10, y=35)
            adress = Label(info, text=f'Адрес: {i.adress}', bg='#7fff00', font=('Times New Roman', 12))
            adress.place(x=10, y=60)
            data = Label(info, text=f'Дата заказа: {i.data}', bg='#7fff00', font=('Times New Roman', 12))
            data.place(x=10, y=85)
            data_dostavki = Label(info, text=f'Дата доставки: {i.data_dostavki}', bg='#7fff00', font=('Times New Roman', 12))
            data_dostavki.place(x=450, y=35)

            y_position +=150

        def great_zakaz():
            zakaz = tk.Toplevel()
            zakaz.title('Создание заказа')
            zakaz.geometry('400x300')
            zakaz.configure(bg='#ffffff')
            zakaz.resizable(False, False)

            article = Label(zakaz, text=f'Артикул:', bg= '#ffffff',  font=('Times New Roman', 12))
            article.place(x=5, y=5)
            article_entry = Entry(zakaz, width=15)
            article_entry.place(x=120, y=5)
            
            status = Label(zakaz, text='Cтатус:', bg= '#ffffff', font=('Times New Roman', 12))
            status.place(x=5, y=45)
            status_entry = Entry(zakaz, width=15)
            status_entry.place(x=120, y=45)
            adress = Label(zakaz, text='Адрес:', bg= '#ffffff', font=('Times New Roman', 12))
            adress.place(x=5, y=85)
            adress_entry = Entry(zakaz, width=15)
            adress_entry.place(x=120, y=85)
            data = Label(zakaz, text='Дата заказа:', bg= '#ffffff', font=('Times New Roman', 12))
            data.place(x=5, y=125)
            data_entry = Entry(zakaz, width=15)
            data_entry.place(x=120, y=125)
            data_dostavki = Label(zakaz, text='Дата доставки:', bg= '#ffffff', font=('Times New Roman', 12))
            data_dostavki.place(x=5, y=165)
            data_dostavki_entry = Entry(zakaz, width=15)
            data_dostavki_entry.place(x=120, y=165)

            def add_zakaz():
                App2zakaz.create(
                    article=article_entry.get(),
                    status=status_entry.get(),
                    adress=adress_entry.get(),
                    data=data_entry.get(),
                    data_dostavki=data_dostavki_entry.get()

                )
                messagebox.showinfo('Успех', 'Заказ создан успешно!')
                zakaz.destroy()

            button_add_zakaz = tk.Button(zakaz, text='Создать заказ', bg='#00FA9A', width=15, font=('Times New Roman', 12), command= add_zakaz)
            button_add_zakaz.place(x=130, y=220)

        def red_zakaz():
            zakaz_red = tk.Toplevel()
            zakaz_red.title('Редактирование заказа')
            zakaz_red.geometry('400x400')
            zakaz_red.configure(bg='#ffffff')
            zakaz_red.resizable(False, False)
            id_label = Label(zakaz_red, text='id', bg='#ffffff', font=('Times New Roman', 12))
            id_label.place(x=10, y=20)
            id_label_entry = Entry(zakaz_red, width=15)
            id_label_entry.place(x=120, y=20)
            article_label = Label(zakaz_red, text='Артикл', bg ='#ffffff', font=('Times New Roman', 12))
            article_label.place(x=10, y=60)
            article_label_entry = Entry(zakaz_red, width=15)
            article_label_entry.place(x=120, y=60)
            status_label = Label(zakaz_red, text='Статус', bg= '#ffffff', font=('Times New Roman', 12))
            status_label.place(x=10, y=100)
            status_label_entry = Entry(zakaz_red, width=15)
            status_label_entry.place(x=120, y=100)
            adress_label = Label(zakaz_red, text='Адрес', bg= '#ffffff', font=('Times New Roman', 12))
            adress_label.place(x=10, y=140)
            adress_label_entry = Entry(zakaz_red, width=15)
            adress_label_entry.place(x=120, y=140)
            data_label = Label(zakaz_red, text='Дата заказа', bg= '#ffffff', font=('Times New Roman', 12))
            data_label.place(x=10, y=180)
            data_label_entry = Entry(zakaz_red, width=15)
            data_label_entry.place(x=120, y=180)
            data_dostavki_label = Label(zakaz_red, text='Дата доставки', bg= '#ffffff', font=('Times New Roman', 12))
            data_dostavki_label.place(x=10, y=220)
            data_dostavki_label_entry = Entry(zakaz_red, width=15)
            data_dostavki_label_entry.place(x=120, y=220)

            def update_zakaz():
                id = id_label_entry.get()
                article = article_label_entry.get()
                status = status_label_entry.get()
                adress = adress_label_entry.get()
                data = data_label_entry.get()
                data_dostavki = data_dostavki_label_entry.get()

                zakaz = App2zakaz.get(App2zakaz.id == id)
                zakaz.article = article
                zakaz.status = status
                zakaz.adress = adress
                zakaz.data = data
                zakaz.data_dostavki = data_dostavki
                zakaz.save()
                messagebox.showinfo('Успех', 'Заказ отредактирован успешно!')
                zakaz_red.destroy()

            button_update_zakaz = tk.Button(zakaz_red, text='Редактировать', bg='#00FA9A', width=15, font=('Times New Roman', 12), command= update_zakaz)
            button_update_zakaz.place(x=130, y=300)

        def delete_zakaz():
            del_zakaz = tk.Toplevel()
            del_zakaz.title('Удаление заказа')
            del_zakaz.geometry('300x150')
            del_zakaz.configure(bg='#ffffff')
            del_zakaz.resizable(False, False)

            id_label = Label(del_zakaz, text='id', bg='#ffffff', font=('Times New Roman', 12))
            id_label .place(x=10, y=20)
            id_label_entry = Entry(del_zakaz, width=15)
            id_label_entry.place(x=120, y=20)

            def delete_zakaz_db():
                id = id_label_entry.get()
                zakaz = App2zakaz.get(App2zakaz.id == id)
                zakaz.delete_instance()
                messagebox.showinfo('Успех', 'Заказ удален успешно!')
                del_zakaz.destroy()
            delete_button = tk.Button(del_zakaz, text='Удалить', bg='#00FA9A', width=15, font=('Times New Roman', 12), command= delete_zakaz_db)
            delete_button.place(x=80, y=70)
            
        if roles.role == 'Администратор' :

            add_tovar_zakaz = Label(zakaz_window, text=f'Добавить заказ', bg= '#00FA9A', width= 15, font=('Times New Roman', 12))
            add_tovar_zakaz.place(x=50, y=550)
            add_tovar_zakaz.bind('<Button-1>', lambda e: great_zakaz())



            red_tovar_zakaz = Label(zakaz_window, text=f'Редактировать заказ', bg= '#00FA9A', width= 17, font=('Times New Roman', 12))
            red_tovar_zakaz.place(x=200, y=550)
            red_tovar_zakaz.bind('<Button-1>', lambda e: red_zakaz())

            delete_tovar_zakaz = Label(zakaz_window, text=f'Удалить заказ', bg= '#00FA9A', width= 15, font=('Times New Roman', 12))
            delete_tovar_zakaz.place(x=370, y=550)
            delete_tovar_zakaz .bind('<Button-1>', lambda e: delete_zakaz())

    if roles.role == 'Администратор' :
        add_tovar = Label(root, text='Добавить товар', bg='#00FA9A', width= 15, font=('Times New Roman', 12))
        add_tovar.place(x=50, y=550)
        add_tovar.bind('<Button-1>', lambda e: button_add_tovar())

        edit_tovar = Label(root, text='Редактировать товар', bg='#00FA9A', width= 17, font=('Times New Roman', 12))
        edit_tovar.place(x=200, y=550)
        edit_tovar.bind('<Button-1>', lambda e: red_tovar())

        delete_tovar_button = Label(root, text='Удалить товар', bg='#00FA9A', width= 15, font=('Times New Roman', 12))
        delete_tovar_button.place(x=370, y=550)
        delete_tovar_button.bind('<Button-1>', lambda e: delete_tovar())

    if roles.role in ['Администратор', 'Менеджер']:
        
        zakaz_sd = Label(root, text='Заказы', bg='#00FA9A', width= 15, font=('Times New Roman', 12))
        zakaz_sd.place(x=540, y=550)
        zakaz_sd.bind('<Button-1>', lambda e: zakaz())

   
avtorizaciya()
#register()
#glavnaya()
root.mainloop()