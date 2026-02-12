#a = 7

#a = 6.7 
#b = a
#print(a)

#var_a = "Hello"

#print(var_a)
#print(b)

#a = b = c = 0

#print(a, b, c)

#print(id(a), id(b), id(c))

#a, b = 1, 2
#print(a, b)
#a, b = b, a
#print(a, b)

#print(type(a))

#print(id(a), id(b))

#x = 5.8

#s = "Hello_Python"

#print(type(x), type(s))

#a = 4

#a **= 4
#print(a)

#a = abs(-5.6)
#print(a)

#print(min(1, 2, 3, 0, -5, 10))

#print(max(1, 2, 3, 0, -5, 10))

#print(pow(6,2))

#print(round(1.5))

#print(round(10.5))

#print(round(7.542525, 2)) # точность округления

#print(round(789.542525, -1))

# abs() min() max() pow() round() 

#print(max(1, 2, abs(-3), 4))

#import math

#print(math.ceil(5.2))

#print(math.floor(5.2))

#print(math.factorial(6))

#print(math.trunc(5.8))

#print(math.log2(8))

#print(math.log(27,3))

#print(math.sqrt(8))

#a = -6.14

#b = 7

#c = 25.6

#print(a, b, c, sep= " | ")

#x = 5.76

#y = -8

#"Координаты точки: x = 5.76, y = -8"

#print("Координаты точки: x = ", x, ", y = ", y, sep = "")

#f-строки

#print(f"Координаты точки: x = {x}; y = {y}")

#a = input()

#print(a, type(a))

# a = float(input("Введите длинну прямоугольника: "))
# b = float(input("Введите ширину прямоугольника: "))



# a, b = map(float, input("Введите две стороны прямоугольника: ").split())
# print("Периметр: ", 2 * (a + b))

# a, b, c = map(int, input("Введите две стороны треугольника: ").split())
# print("Периметр: ", a + b + c)

#Логические выводы

# a = 4 > 7
# print(a, type(a))
# y = 1.85
# #[-2,5]
# print(y >= -2 and y <= 5)
# print(2 >= y <= 5)

# bool() True False
#print(bool(0.0))

#строки

# s1 = "ПАНДА"
# s2 = "PaNDA"

# print(s1)
# print(s2)
# text = ''' Я изучаю Python от и до
# ПОТОМУ что 
# это нужно'''
# print(text)
# s1 = "я люблю"
# s2 = "python"
# a = " "
# print(s1 + a + s2 + a +str(True)) #конкатенация строк
# print("ха " * 5) # дублирование строки
# print(len("hello")) #длинна строки
#print("abc" in "abaiojoajafe") #вхождения строк
#print("fwfwf" == "fhajkf")
# print("кот" < "кит") #стравнение строк
# print(ord('k')) # код символа
# s = "Hello Python"
# print(s[len(s) - 1]) #индексация
# print(s[-1])
# строка [start:stop] #последний индекс в срезе не учитывается 
# print(s[1:3])
# print(s[1:]) # строка это упорядоченный набор символов
# print(s[:])
# print(s[2:-2])
# строка [start:stop:step] #шаг среза
# print(s[2:-2])
# print(s[2:-2:2])
# print(s[::-1]) #отрицательный шаг среза переварачивает строку 
# s2 = 'h' + s[1:] # строки относятся к неизменяемому типу данных
# print(s2)

#основные методы для строк
# s = "python"
# print(type(s))
# функции работы со строками называются методами 
# объект.метод.(аргумент)
# res = s.upper() #метод, который меняет строчные буквы на заглавные
# print(s.lower()) #метод, который меняет заглавные буквы на строчные
#string.count(sub[,start[,end]]) # start - индекс, 
#с которого начинается поиск, end - заканчивается
# msg = 'sndfoinfwonljngjerewfererewrfeferefe'
# print(msg.count("re"))
# print(msg.count("re",4, 10)) #старт, конец вычисления
# string.find(sub[,start[,end]]) - метод который находит первый индекс  
# нахождения подстроки в строке (слева на прово)
# msg = 'sndfoinfwonljngjerewfererewrfeferefe'
# print(msg.find("bre",1)) # если подстрока не находитьсяБ то возвр -1
# print(msg.rfind("re",1)) # слева напрово 
#sring.index(sub[,start[,end]]) находит индекс подстроки если подстроки
# не существует, то ошибка
# string.replace(old, new, count = -1) # метод замены подстроки
# count - максимальное кол-во замен (-1 - без ограничений)
# print(msg.replace("re", "xyz"))
# print(msg.replace("re", "RE"))
# print(msg.replace("re", "")) # удаление подстрок
# print(msg.replace("re", "RE", 2))
# string.isalpha() - проверяет состоит ли строка только из букв или нет
# print(msg.isalpha())
# s = "gergrev wrwefwefwef"
# print(s.isalpha())
# string.isdigit() - проверяет состоит ли строка только из цифр
# n = "-56"
# print(n.isdigit())
# string.rjust(width[,fillchar = '']) - возвращает новую строку с задан
# символом виз, при необходимомсти слева дполняет 
# символы заполнители филчар""

# d = "abc"
# d = "12"
# print(d.rjust(4, "0")) слева
# print(d.ljust(4, "*")) справа
# string.split(sep = None, maxsplit=-1) # возвращает коллекцию строк, 
# на которые разбиваается строка, sep = фрагмент разбиения
# print("Иванов Иван Иванович".split(" "))
# digs = "1, 234, 4, 63, 3,36,6,7757575"
# d = digs.replace(" ", "").split(",")
# #string.join(список) - из списка строк собирает единую строку
# print(", ".join(d))
# strin.strip() - удалет все символы пробелов в начале и конце строки
# print("    hello world      \n".strip())
# print("    hello world      \n".rstrip())
# print("    hello world      \n".lstrip())
# text = r"d:\Python 3.12.1\python.exe"
# print(text)

#f-string
# age = 24
# name = "Илья"
# print("Меня зовут " + name + ", мне " + str(age) + " и я люблю язык python")
# print("Меня зовут {fio} ,мне {old} и я люблю язык python".format(fio=name, old=age))
# print(f"Меня зовут {len(name.upper())}, мне {age * 2} и я люблю язык python")

#списки
# sities = ["Москва", "Ваолгда", "Арзамас"]
# ilya = [2, 4, 4, 5, 5, 5, 3]
# ilya[0] = "удовлетворительно"
# print(ilya)
# print(list("python"))
# print(max(ilya))
# print(min(ilya))
# print(sum(ilya)/len(ilya))
# print(sorted(ilya, reverse= True))
# print(sorted(ilya, reverse= False))
# print([1, 2, 3] + [4, 5, 66] + [True])
# print(sities * 3)
# s = [1, 2, 3] + [4, 5, 66] + [True]
# print(34 in s)
# del s[2]
# print(s)


# срезы списков
# сities = ["Москва", "Вологда", "Арзамас", "Саров"]
# ilya = [2, 4, 4, 5, 5, 5, 3]
# print(сities[:3])
# print(ilya [1:5:2])
# print(ilya [::-1])
# ilya[2:4] = ["хорошо", "удовлетворительно"]
# print(ilya)
# ilya[4:5] = 10, 20
# print(ilya)

#основные методы списков 

# a = [1, -54, 3, 23, 42, -45, 0]
# a.append(100) # добавление в конце списка элеменьа 100
# a.append([1, 2, 3])# можо добавлять только один элемент в список
# a.insert(3, -1000) # всиавляет значение в список на определённый индекс, тем самым расширяет его
# a.remove(-1000) # удаляет перве вхождение элемента в список по индексу по значению
#a.pop() удаляет последний элеменет в списке, возвращая его (запоминая) по индексу
#a.clear() удаляет весь список
# print(a, a.pop(3))
#c = a.copy()  с = a[:] c = lis(a) копия списка
#a.count(1) # позволяет найти количества вхождения элемента в список
# a.append(1)
# print(a.count(1424))
# a.index(значение, стартовый индекс поиска) позволяет находить идекс первого найденного значения
# a.reverse() меняет список значений на обратный
# a.sort() сортировка текущий список по возростанию 
# sorted(a) сортирует и возвращает новый список
# a.sort(reverse = True) по убыванию

# Вложенные списки 
# line = [1 , 7, 6, 11, 3]
# img = [[1 , 7, 6, 11, 3], [1 , 7, 6, 11, 3], [1 , 7, 6, 11, 3], [1 , 7, 6, 11, 3], [1 , 7, 6, 11, 3]]
# img = [line[:], line[:], line[:], line[:], line[:]]
# img[1] = [1] * 5 #заменяет элемент в списки новым элементом
# img[1][:] = [1] * 5 # изменяет сам элемент в списке 
# print(img)

# условный оператор if
# x = -4
# if x < 0:
#     x = -x
# print(x)
# x = int(input())
# if x:
#     print('eeeeeeeee')
# marks = [3, 3, 4, 4, 4]

# if 2 in marks:
#     print("студент будет отчислен")
# else:
#     print("студент успешно сдал сессию")

#вложенные условия и множественный выбор 
# x = int(input())

# if x % 2 == 0:
#     if 0 <= x <= 9:
#         print("это цифра")
#     else:
#         print("это число")
# else:
#     print('нечётное число')

# максимальное из 3 чисел 
# a, b, c = map(int, input("числа:").split()) 
# if a > b:
#     if a > c:
#         print("a - max digital")
#     else:
#         print("c - max digital")
# else:
#     if b > c:
#         print(f"{b} - b max digital")
#     else:
#         print(f"{c} - c max digital")

# множественный выбо при помощи elif

# item = int(input())

# if item == 1:
#     print("Python")
# elif item == 2:
#     print("C++")
# elif item == 3:
#     print("Java")
# elif item == 4:
#     print("JavaScript")
# else:
#     print("fuck you")

# тернарный условный оператор 

# a = 12
# b = 7
# if a > b:
#     res = a
# else:
#     res = b 

# res = a if a > b else b # тернарный условный оператор 
# print(res)

# s = "python"
# t = "upper"

# res = s.upper() if t == "upper" else s
# print(res)

# a = 12
# b = 7
# print([1, 2, 3, a if a > b else b, 4, 6])
# print("a - " + ("чётное" if a % 2 == 0 else "нечётноу") + " число")
# print(max(1, 2, 3, a if a > 0 else b, 4, 5))

# максимально среди трёх чисел при помощи тернарного оператора
# a = 2
# b = 3
# c = 4

# d = (a if a > c else c) if a > b else (b if b > c else c)
# print(d)

# цикл while

# n = int(input())
# s = 0
# i = 1
# while i <= n:
#     s += i
#     i += 1
# print(s)

# оператор цикла for
# d = [0, 1, 2, 3, 4, 5]
# # for x in d:
# #     print(x)
# # for x in "python":
# #     print(x)

# # for i in d:
# #     d[i] = 0
# # print(d)
# # print(list(range(0, 5)))
# # for i in range(len(d)):
# #     d[i] = 0
# # print(d)
# s = 0
# for i in range(2, 1001):
#     s += 1/i

# print(s)

# примеры оператора цикла for

# n = int(input("Введите натуральное цисло не более 100: "))
# if n < 1 or n > 100:
#     print("Неверно ведено число")
# else:
#     counter = 1
#     for i in range(1, n + 1):
#         counter *= n
#     print(f"Факториал {n} = {counter}")

# n = int(input())
# for i in range(1, n + 1):
#     if i <= n // 2:
#         print(i * "*")
#     else:
#         print((n - i)* "*")

# # итерируемые обекты 
# d = [5, 3 ,7 , 10, 2]
# it = iter(d)
# print(next(it), next(it), next(it), next(it))

# s = "python"
# it = iter(s)
# print(next(it))

#Вложенные циклы 

# for i in range(1, 4):
#     for j in range(1, 6):
#         print(f"i = {i}, j = {j}", end = " ")
#     print()

# a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# for row in a:
#     for x in row:
#         print(x, type(x), end=" ")
#     print()

# a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
# c = []

# for i, row in enumerate(a):
#     r = []
#     for j, x in enumerate(row):
#         r.append(x + b[i][j])
#     c.append(r)
#     print(r)
# print(c)

# Треугольник Паскаля
# n = int(input())
# P = []
# c = 0
# for i in range(n):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if i != j and j != 0:
#             row[j] = P[i - 1][j - 1] + P[i - 1][j]
#     P.append(row)
# for k in P:
#     print(int((n - c) / 2) * "  ", *k)
#     c += 1
# Множества 
# a = {1, 2, 3, "хуй", 1, 2, 3}
# print(a)
# a = {1,  3.5, (4, 5), "hu"}
# print(a)
# a = set([1, 2, 3, -4, 1, 2])
# print(a)
# a = set(range(7))
# print(a)
# print(a[0]) # эрор
# q = {"Краснодар", "Ульяновск", "Калуга", "Тюмень", "Москва"}
# # it = iter(q)
# # print(next(it))
# print(len(q))
# print("Москва" in q)
# print("abc" in q)
# b = set()
# b.add(7)
# b.add(33)
# print(b)
# b.update(["a", "b", (1, 2)])
# print(b)
# b.discard(7)
# print(b)
# # b.remove(7) # ошибка если элемента нет
# b.pop() # удаляет произвольный элемент из множества 
# print(b)
# b.clear()
# print(b)
# операции над множествами 
# setA = {1, 2, 3, 4}
# setB = {3, 4, 5, 6, 7} 
# print(setA & setB) # возвращает новое множество 
# print(setA.intersection(setB)) # результат пересечения
# setA.intersection_update(setB) # обновление множества а резултатом пересечения множест а и b
# print(setA) 
# setC = {9, 10, 11}
# print(setA & setC)
# setA = {1, 2, 3, 4}
# setB = {3, 4, 5, 6, 7} 
# print(setA | setB) # объединеие двух множеств

# print(setA.union(setB)) # тоже самое
# print(setA - setB)
# print(setB - setA)
# print(setA ^ setB)

# print(setA == setB) # если количество элементов совпадает и они равны
# setA = {1, 2, 3, 4}
# setB = {1, 2, 3, 4, 5} 
# print(setA < setB)

# генераторы множеств и словарей
# a = {x ** 2 for x in range(1, 5)}
# print(a) # генератор множеств

# a = {x: x ** 2 for x in range(1, 5)}
# print(a) # генератор словаря
# d = [1, 2, "1", 4 , -4, 3, "2"]
# a = {int(x) for x in d}
# print(a)
# m = {"неудовл.": 2, "удовл.": 3, "хорошо": "4", "отлично": 5}
# a = {key.upper(): int(value) for key, value in m.items()}
# print(a)
# d = [1, 2, "1", 4 , -4, 3, "2"]
# a = {int(x) for x in d if int(x)  > 0}
# print(a)
# lst_in = ["Пушкин: Капитанская дочка", "Пушкин: Евгений Онегин", "Толстой: Война и мир", "Достоевский: Преступление и наказание", "Достоевский: Идиот"]
# lst = [x.split(": ") for x in lst_in]
# d = [{i[0]: {i [1]}} for i in lst for j in range(len(i)) if i[1] not in i[j]]
# print(*d)


#функции в пайтон 
# def send_email(from_name, old):
#     text = f"тебя зовут {from_name}, тебе {old} лет"
#     print(text)


# def get_sqrt(x):
#     res = None if x < 0 else x ** 0.5
#     return res, x


# def get_max2(a, b):
#     return a if a > b else b

# def get_max3(a, b, c):
#     return get_max2(a, get_max2(b, c))


# def even(x):
#     return x % 2 == 0


# for i in range(1, 20):
#     if even(i):
#         print(i)


# Алгоритм Евклида
# Нахождение НОД (наименьшего общего делителя)


# Медленный алгортм Евклида 
# import time


# # def get_nod(a, b):
# #     """Вычисляется НОД для натуральных чисел a и b
# #     по алгоритму Евклида.
# #     :parametr a: первое натуральное число
# #     :peremetr b: второе натуральное число 
# #     :return: НОД
# #     """
# #     while a != b:
# #         if a > b:
# #             a -= b
# #         else:
# #             b -= a
# #     return a


# def test_nod(func):
#     # Тест № 1
#     a = 28
#     b = 35
#     res = func(a, b)
#     if res == 7:
#         print("Тест 1 - ok")
#     else:
#         print("Тест 1 - fail")
    

#     # Тест № 2
#     a = 100
#     b = 1
#     res = func(a, b)
#     if res == 1:
#         print("Тест 2 - ok")
#     else:
#         print("Тест 2 - fail")
    

#     # Тест № 3
#     a = 2
#     b = 100000000
#     st = time.time() # начальное время запуска функции 
#     res = func(a, b)
#     et = time.time() # конченое время вычисления функции
#     dt = et - st # сколько времени понадобилось на вычисление
#     if res == 2 and dt < 1:
#         print("Тест 3 - ok")
#     else:
#         print("Тест 3 - fail")


# # test_nod(get_nod)


# # Быстрый алгоритм Евклида


# def get_nod(a, b):
#     """Вычисляется НОД для натуральных чисел a и b
#     по быстрому алгоритму Евклида.
#     :parametr a: первое натуральное число
#     :peremetr b: второе натуральное число 
#     :return: НОД
#     """
#     if a < b :
#         a, b = b, a
#     while b != 0:
#         a, b = b, a % b
#     return a

# test_nod(get_nod)


# Именованные аргументы. Фактические и формальные параметры  Python для начинающих

# def get_V(a, b, c, varbose = True): 
#     if varbose:
#         print(f"a = {a}, b = {b}, c = {c}")
#     return a * b * c


# v = get_V(1 , 2, 4, False)
# print(v)


# def cmp_str(s1, s2, reg = False, trim = True):
#     if reg:
#         s1 = s1.lower()
#         s2 = s2.lower()
#     if trim:
#         s1 = s1.strip()
#         s2 = s2.strip()
    
#     return s1 == s2

# print(cmp_str("Python   ", "  python"))

# def add_value(value, lst = []):
#     lst.append(value)
#     return lst

# l = add_value(1)
# l = add_value(2)
# print(l)

# def add_value(value, lst = None):
#     if lst == None:
#         lst = []

#     lst.append(value)
#     return lst

# l = add_value(1)
# l = add_value(2)
# print(l)
# операторы * и ** распоковки и упаковки 

# x, y = (1, 2)
# print(x)

# x, *y = (1, 2, 3, 4, 6, 7, 7, 8, 11, 22, 4425)
# print(x)
# print(y)

# x, *y = [1, 'fwafwea', True]
# print(x)
# print(y)

# x, *y = 'Hello python'
# print(x)
# print(y)

# a = [1, 2, 3]

# print((*a,))

# d = -5, 5
# print(*range(*d), *(True, False), 1, 2, 3, 5)


# m = {"неудовл.": 2, "удовл.": 3, "хорошо": "4", "отлично": 5}
# m2 = {"Пушкин": "Капитанская дочка", "Пушкин": "Евгений Онегин", "Толстой": "Война и мир", "Достоевский": "Преступление и наказание", "Достоевский": "Идиот"}
# print({**m, **m2})


# Рекурсивные функции.
# Решить задачу при помощи метода слияния


# lst = [123, 42, 3,64, 6, 7, -7, 18, 11, 32, 25]


# def digit_min(a, b):
#     i = 0 
#     j = 0
#     c = []
    
    
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             c.append(a[i])
#             i += 1
            
#         else:
#             c.append(b[j])
#             j += 1
            
#     c += a[i:] + b[j:]
    
#     return c 
    

# def join(lst):
#     N = len(lst) // 2
#     l1 = lst[N:]
#     l2 = lst[:N]

    
#     if len(l1) > 1:
#         l1 = join(l1)
        
#     if len(l2) > 1:
#         l2 = join(l2)    
        
#     return digit_min(l1, l2) 


# # lst = [123, 42, 3,64, 6, 7, -7, 18, 11, 32, 25]
# print(join(lst))


# рекурсивыне функции
# def recursive(value):
#     print(value)
#     if value< 4:
#         recursive(value + 1)
#     print(value)


# recursive(1)

# def fact(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact(n - 1)


# print(fact(6))

# Лямбда функции

# s = lambda a, b: a + b
# print(s(1,2))

# a = [3, 4, 6, lambda: print("lambda"), 3, 5]

# print(a[3]())

# lst = [5, 3, 6, -8 , 0, -4, 10, 1]

# def get_filter(a, filter = None):
#     if filter is None:
#         return a

#     res = []
#     for x in a:
#         if filter(x):
#             res.append(x)
    
#     return res

# # универсальная функция для выбора филтра 

# r = get_filter(lst,filter = lambda x: x > 0)
# print(r)
# оператор присаваивания в лямбда функциях писать нельзя, так как лямбда функция не выполниться 


# области видимости переменных 
# N = 100 
# WIDH, HIEGHT = 1000, 500


# def my_func(lst):
#     global N
#     N = 20
#     for x in lst:
#         n = x + 1 + N
#         print(n)

# my_func([1, 2, 3])
# print(N)

# x = 0


# def outer():
#     global x
#     x = 1
#     def inter():
#         # nonlocal x
#         x = 2
#         print("inter: ", x)
    
#     inter()
#     print("outer: ", x)

# outer()
# print("global: ", x)


# замыкания 

# def say_name(name):
#     def say_goodbye():
#         print("Don't say me goodbye," + name + "!")
#     return say_goodbye


# print(say_name("Петя")())

# функция счётчик

# def counter(start = 0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#     return step

# c = counter(10)
# c1 = counter()

# print(c(), c1())
# print(c(), c1())
# print(c(), c1())

# функция, удаляющие ненужные символы в начале и конце строки 

# def strip_string(strip_chars = " "):
#     def do_strip(string):
#         return string.strip(strip_chars)
#     return do_strip


# strip1 = strip_string()
# strip2 = strip_string(" !&.,:;")

# print(strip1("  hello python;;! , "))
# print(strip2("  hello python;;! , "))

# Декоравторы функций 
# def func_decorator(func):
#     def wrapper(*arg, **kwargs):
#         print("что то до функции")
#         func(*arg, **kwargs)
#         print("что-то выводит после функции")
    
#     return wrapper


# def some_func():
#     print("сама функция сам фанк")

# some_func = func_decorator(some_func)

# some_func()

# декораторы функция с параметрами 
# вычисление производной функции
# from functools import wraps
# import math

# def df_deckor(dx = 0.01):
#     def deckor(func):
#         @wraps(func)
#         def wrapper(x, *arg, **kwargs):
#             res = (func(x + dx, *arg, **kwargs) - func(x, *arg, **kwargs)) / dx
#             return res
#         # wrapper.__name__ = func.__name__
#         # wrapper.__doc__ = func.__doc__
#         return wrapper
#     return deckor

# @df_deckor(dx = 0.000000001)
# def sin_df(x):
#     "функция для вычисления производной синуса"
#     return math.sin(x)


# df = sin_df(math.pi/3)
# print(sin_df.__doc__, sin_df.__name__)


# импорт стандартных модулей


# from math import ceil, pi
# import time
# import pprint

# math = "математика"
# pprint.pprint(locals())
# a = ceil(1.8)
# print(pi)

# импорт собственных модулей 

# классы и объекты
# class Point:
#     "Класс для представления координат точек на плоскости"
#     color = "red"
#     circle = 2



# a = Point()
# b = Point()

# a.x = 1
# a.y = 2
# b.x = 10
# b.y = 20
n = int(input())

z = [k for k in range(1, n ** 2 + 1)] 
counter = 0
print(z)
m = []



for i in range(1, n + 1):
    l = []
    for j in range(1, n + 1):
        if i == 1:
            l.append(z[counter])
            counter += 1
        elif i % 2 == 0:
            l.append(z[counter])
    m.append(l)
print(*m, sep="\n")
