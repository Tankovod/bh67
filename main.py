# print('hi')
# print('hi')
# print('hi there')
# print('hi there')
# name = ' rgdfgf '
# age = 34
# print(name, age, sep='2423423r3t')

# surname = 'popov'
# fullname = 'serfdgd'
# print(fullname*3)
#
# print(len('esrsg\n\nfds'))

# s = 'ergf 234 esgfdfg'
# print(s.rpartition('234'))

# ----- LESSON ------------------------------------------------------- 4
# if 0 or 5:
#     print('uuu')
#
# print(any([0, 0, 0, 0, 4]))

# a = input()
# while not a.isdigit():
#     a = input()

# ---------
# i = 0
# a = input().split(' ')
# print(a)
# summ = int(a[0])
# percent = int(a[1])
# b = summ
# years = 0
#
# while i < 2:
#     b += b*(percent*0.01)
#     i = b/summ
#     print(b)
#     years +=1
#
# print('years=' + str(years))
# ---------
# numbers = ['1', '2', '3', '4', '5']
# numbers = [int(i) for i in numbers]

# for i in numbers.copy():
#     numbers.remove(i)
#     numbers.append(int(i))
# print(numbers)

# --------- ---------------------------------- task
# data = {'1': 1, '2': '234', '3': 45, '5': False}
# for i, j in data.items():
#     if isinstance(j, int) and not isinstance(j, bool):
#         print(i)
# --------- ---------------------------------- task

# ----- LESSON ------------------------------------------------------- 5
# def func0(s, d , *args, **kwargs):
#     print(s , d)
#     print(args)
#     print(kwargs)
#
# func0(34, 34, 234, 234, h=234, fg=234)

# ----- LESSON ------------------------------------------------------- 8
#
# class Button:
#     def __init__(self, text: str, link: str):
#         self.text = text
#         self.link = link
#
#     def dict(self):
#         return {'text': self.text, 'link': self.link}
#
#
# buttons = [Button('df', 'dfg'), Button('dfg', 'dfg')]
#
#
# class Keyboard:
#     def __init__(self, name, buttons):
#         self.name = name
#         self.buttons = buttons
#
#     def dict(self):
#         return {'name': self.name, 'buttons': [i.dict() for i in self.buttons]}
#
#
# print(Keyboard('dd', buttons).dict())
#
# data = '[Section1]\nkey1=value1\nkey2=value2\n[Section2]\nkey3=value3\nkey4=value4\nkey5=value5'
# class ConfigParser:
#     def __init__(self, text):
#         self.text = text
#
#     def split_str(self):
#         strng = ['[' + i for i in self.text.split('[') if i != '']
#         strng = [(i.split('\n')) for i in strng]
#         # strng = strng
#         # sections = [i for i in strng if i[0] == '[']
#         # k_v = [i for i in strng if i[0] != '[']
#         #
#         # print(sections, k_v)
#         print(strng)


# ConfigParser(data).split_str()
# ----- LESSON ------------------------------------------------------- 9

# class A:
#     a = 'a'
#
# class D(A):
#     a = 'd'
#
# class F(D):
#     a = 'f'
#
# class B:
#     a = 'b'
#
# class C(F,B, D, A):
#     pass
#
# print(C.mro())

# ----- LESSON ------------------------------------------------------- 10

# file = open('input.txt', 'r', encoding='utf-8')
#
#
# file.close()

# with open('input.txt', 'r', encoding='utf-8') as file:
# text = file.read()

# print(file.readline())
# print(file.readline())

# print(file.readlines())

# for line in file:
#     print(line)

# file.seek(0)
# print(file.read())

# with open('input.txt', 'r', encoding='utf-8') as file:
#     lst = file.readlines()
#
# dd = []
# for line in lst:
#     dd.append(line.strip().split())
#
# with open('output.txt', 'a', encoding='utf-8') as file:
#     for line in dd:
#         file.write(str(sum(map(int, line))) + '\n')

# with open('input.txt', 'r', encoding='utf-8') as file1, open('output.txt', 'w', encoding='utf-8') as file2:
#     for i, line in enumerate(file1):
#         c = line.count(' ')www
#         w = len([l for l in line if l.isalpha()])
#         file2.write(f'В {i + 1} строке {w} букв и  {c + 1} слов\n')

# from json import load, dump
# from csv import reader, writer, DictReader, DictWriter
# with open('a.csv', 'r', encoding='utf-8') as file, open('u.json', 'w', encoding='utf-8') as file2:
#     dct = list(DictReader(file))
#     dump(dct, file2, indent=2)

# ----- LESSON ------------------------------------------------------- 11
# from datetime import datetime, date, time, timedelta
#
# date1 = datetime.now()
# date1 = datetime.now().timestamp()
# print(date1)

# ----- LESSON ------------------------------------------------------- 12

# from psycopg2 import connect
#
# conn = connect('postgresql://admin:admin@localhost:5432/belhard')
# with conn.cursor() as cur:
#     cur.execute('''CREATE TABLE IF NOT EXISTS category(id SERIAL PRIMARY KEY, name VARCHAR(64) NOT NULL UNIQUE);''')
#     conn.commit()
#
# with conn.cursor() as cur:
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS post(
#         id SERIAL PRIMARY KEY,
#         title VARCHAR(128) NOT NULL,
#         description TEXT NOT NULL,
#         date_publish TIMESTAMP DEFAULT now(),
#         category_id INTEGER NOT NULL,
#         FOREIGN KEY(category_id) REFERENCES category(id) ON DELETE CASCADE
#         );
#     """)
#
#     conn.commit()
#
# with conn.cursor() as cur:
#     # cur.executemany('''
#     #     INSERT INTO category (name)
#     #     VALUES (%s);''', (('Finance', ), ('Sport', )))
#     cur.execute('''
#         INSERT INTO post (title, description, category_id) VALUES (%s, %s, %s)''', ('Post 1', 'Desc', 1))
#     conn.commit()
#
# with conn.cursor() as cur:
#     cur.execute('''
#     SELECT category.name, post.title FROM category
#     LEFT JOIN post ON post.category_id = category.id
#     ORDER BY category.name;''')
#     print(cur.fetchall())

from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker
from sqlalchemy import Column, INT, VARCHAR, TIMESTAMP, ForeignKey, TEXT, BOOLEAN, create_engine


class Base(DeclarativeBase):

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://admin:admin@localhost:5432/belhard')
    session = sessionmaker(bind=engine)

class Category(Base):
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), unique=True, nullable=False, index=True)


class Post(Base):
    title = Column(VARCHAR(128), nullable=False)
    description = Column(TEXT, nullable=False)
    date_publish = Column(TIMESTAMP, server_default='now()')
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    is_published = Column(BOOLEAN, default=False)


# with Category.session() as session:
#     categoties = [
#         Category(name='Finance'),
#         Category(name='Sport')
#     ]
#     session.add_all(categoties)
#     session.commit()
#     for category in categoties:
#         session.refresh(category)
#
#     for category in categoties:
#         print(category.id, category.name)


# with Category.session() as session:
#     category_1 = session.get(Category, 1)
#     category_1.name = 'Politics'
#     session.add(category_1)
#     session.commit()
#     print(category_1.id, category_1.name)

