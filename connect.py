from peewee import AutoField,  MySQLDatabase, IntegerField, CharField, \
     Model

db =MySQLDatabase('var', user='root', password= 'root', host ='localhost', port=3306)


class BaseModel(Model):
    
    class Meta:
        database = db

class Tovar(BaseModel):
    id = AutoField()
    article = CharField()
    name = CharField()
    edinisa = CharField()
    price =  IntegerField()
    postavsik = CharField()
    proizvod = CharField()
    category = CharField()
    sale = IntegerField()
    kolvo = IntegerField()
    opis = CharField()
    photo = CharField()

class User(BaseModel):
    id = AutoField()
    fio = CharField()
    login = CharField()
    password = CharField()
    role = CharField()

class Zakaz(BaseModel):
    id = AutoField()
    article = CharField()
    data = CharField()
    data_dostavki = CharField()
    adress = CharField()
    fio = CharField()
    status = CharField()
    code = IntegerField()

class Punkt(BaseModel):
    id = AutoField()
    adress = CharField()
   

class Tovar_app(BaseModel):
    id = AutoField()
    article = CharField()
    name = CharField()
    edinisa = CharField()
    price =  IntegerField()
    postavsik = CharField()
    proizvod = CharField()
    category = CharField()
    sale = IntegerField()
    kolvo = IntegerField()
    opis = CharField()
    photo = CharField()

class App2zakaz(BaseModel):
    id = AutoField()
    article = CharField()
    status = CharField()
    adress = CharField()
    data = CharField()
    data_dostavki = CharField()

db.connect()
db.create_tables([Tovar, User, Zakaz, Punkt, Tovar_app, App2zakaz])
db.close()
    