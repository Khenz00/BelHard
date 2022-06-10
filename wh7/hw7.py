
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String

engine = create_engine('sqlite:///products.db', echo=True)
meta = MetaData()
conn = engine.connect()

products = Table(
    'products', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', Integer),
    Column('amount', Integer),
    Column('comm', String),
)


def insert():
    ins = products.insert().values(name=input('Введите имя '), price=input('Введите цену '),
                                   amount=input('Введите количество '), comment=input('Комментарий '))
    conn.execute(ins)


def select():
    sel = products.select()
    res = conn.execute(sel)
    for i in res:
        print(i)


def update():
    upd = products.update().where(products.c.id == input('Введите id продукта ')).values(name=input('Введите имя '),
                                                                                         price=input('Введите цену '),
                                                                                         amount=input(
                                                                                             'Введите количество '),
                                                                                         comment=input('Комментарий '))
    conn.execute(upd)


def delete():
    dlt = products.delete().where(products.c.id == input('Введите id продукта '))
    conn.execute(dlt)


while True:
    f = int(input(
' Вставка продукта - 1 \n Обновление продукта - 2 \n Удаление продукта - 3 \n Просмотор таблицы - 4 \n Выход - 0 \n '))
    if f == 0:
        break
    else:
        {1:insert, 2:update, 3:delete, 4:select}.get(f)()