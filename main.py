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

class Button:
    def __init__(self, text: str, link: str):
        self.text = text
        self.link = link

    def dict(self):
        return {'text': self.text, 'link': self.link}


buttons = [Button('df', 'dfg'), Button('dfg', 'dfg')]


class Keyboard:
    def __init__(self, name, buttons):
        self.name = name
        self.buttons = buttons

    def dict(self):
        return {'name': self.name, 'buttons': [i.dict() for i in self.buttons]}


print(Keyboard('dd', buttons).dict())

data = '[Section1]\nkey1=value1\nkey2=value2\n[Section2]\nkey3=value3\nkey4=value4\nkey5=value5'
class ConfigParser:
    def __init__(self, text):
        self.text = text

    def split_str(self):
        strng = ['[' + i for i in self.text.split('[') if i != '']
        strng = [(i.split('\n')) for i in strng]
        # strng = strng
        # sections = [i for i in strng if i[0] == '[']
        # k_v = [i for i in strng if i[0] != '[']
        #
        # print(sections, k_v)
        print(strng)


ConfigParser(data).split_str()