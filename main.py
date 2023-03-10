import math
import sys

import Func


def sas1():
    print("Value:\t", 3, "\nID:\t\t", id(3))
    number = 3
    print("\nValue:\t", number, "\nID:\t\t", id(number))
    number2 = 3
    print("\nValue:\t", 3, "\nID:\t\t", id(3))
    print("\nValue:\t", number2, "\nID:\t\t", id(number2))

    a = 5                                               # id A = 140711960048552
    b = 7                                               # id B = 140711960048616
    print("\nA:\t", a, "\nB:\t", b)
    print("\nID A:\t", id(a), "\nID B:\t", id(b))

    a = b                                               # id A = id B = 140711960048616
    print("\nA:\t", a, "\nB:\t", b)
    print("\nID A:\t", id(a), "\nID B:\t", id(b))

    b = 1                                               # id A = 140711960048616,
    print("\nA:\t", a, "\nB:\t", b)                     # id B = new id (140711960048424)
    print("\nID A:\t", id(a), "\nID B:\t", id(b))

    #
    print("\n///////////////////////////////////\n")
    #

    c = 5
    d = 7
    print("\nC:\t", c, "\nD:\t", d)
    print("\nID C:\t", id(c), "\nID D:\t", id(d))

    c = d
    print("\nC:\t", c, "\nD:\t", d)
    print("\nID C:\t", id(c), "\nID D:\t", id(d))

    d += 5  # d получила новый адрес!
    print("\nC:\t", c, "\nD:\t", d)
    print("\nID C:\t", id(c), "\nID D:\t", id(d))

    #
    print("\n///////////////////////////////////\n")
    #

    num = None  # id ...28
    print("\nNum:\t", num, "\nNum id:\t", id(num))
    num = 12  # new id: ...76
    print("\nNum:\t", num, "\nNum id:\t", id(num))
    num = 12  # optimisation: id = ...76
    print("\nNum:\t", num, "\nNum id:\t", id(num))
    num = 13  # new id: ...08
    print("\nNum:\t", num, "\nNum id:\t", id(num))

    #
    print("\n///////////////////////////////////\n")
    #

    list_s = [1, 3, 4, 9, 0]                            # list id: ...04 (const)

    print("\nList:\t\t", list_s,
          "\nList id:\t", id(list_s))
    print("\nList[0]:\t", list_s[0],                    # list[index] id: ...80
          "\nList[0] id:\t", id(list[0]))

    list_s[0] = -3.14                                   # list[index] id: new id - ...40

    print("\nList:\t\t", list_s,                        # list id: ...04
          "\nList id:\t", id(list_s))
    print("\nList[0]:\t", list_s[0],
          "\nList[0] id:\t", id(list[0]))


def sas2():
    a = 5
    b = 3

    print(a / b)                                        # float
    print(a % b)
    print(a // b)                                       # целая часть
    print(a ** b)                                       # возведение в степень

    print("\n//////////////////////////////////////\n")

    x = 2 + 1j                                          # комплексные числа
    z = complex(4, - 5)                                 # через функцию

    print(x + z)
    print(x - z)
    print(x / z)
    # print(x % z)                                      not working
    # print(x // z)
    print(x ** z)

    print((x + z).real)                                 # действительная часть (обращаемся к анонимному объекту через .)
    print((x + z).imag)                                 # мнимая часть

    y = 6 + 1j
    print(y.conjugate())                                # комплексно-сопряженное число

    print("\n//////////////////////////////////////\n")

    p = 41                                              # 101001
    q = 19                                              # 010011

    print(p | q)                                        # 111011
    print(p & q)                                        # 000001
    print(p ^ q)                                        # 111010
    print(~p)                                           # нет unsigned чисел

    print(p << 1)                                   # ...0101001 << 1 = 1010010
    print(p >> 1)                                   # ...0101001 >> 1 = 0010100 (при сдвиге за 2^0 значения 1 стираются)

    print("\n//////////////////////////////////////\n")

    num = 7589142                                       # cc 10

    print(hex(num))                                     # cc 16
    print(oct(num))                                     # cc 8
    print(bin(num))                                     # cc 2

    print("\n//////////////////////////////////////\n")

    # import math

    pi = math.pi                                        # число п
    e = math.e                                          # число е

    print("\npi:\t", pi)
    print("e:\t", e)

    print(math.ceil(pi))                                # округление к большему значению до целых
    print(math.fabs(-3.14))                             # абсолютное значение: 3
    print(math.factorial(5))                            # 1 * 2 * 3 * 4 * 5
    print(math.floor(pi))                               # целая часть

    print(math.log2(16))                                # логарифм от 16 по основанию 2
    print(math.log10(1000))                             # десятичный логарифм
    print(math.log(e * 16))                             # по умолчанию натуральный логарифм от e * 16
    print(math.log(15, 3))                              # логарифм от 15 по основанию 3

    print(math.sin(45))
    print(math.cos(-45))


def sas3():
    lst = [1, 2, 3, 4, 5, 6, True]
    print(lst)

    for i in range(len(lst)):                           # по умолчанию от 0 и до длины списка len(list)
        if lst[i] % 2 == 0:
            lst[i] += 1
        elif lst[i] == 5:
            lst[i] = 0
        else:
            lst[i] -= 1

    print(lst)

    for i in lst:                                       # семантика копирования
        i *= -1
        print(i)

    print(lst)

    count = 0
    while count < len(lst):
        lst[count] = None
        count += 1

    print(lst)


def sas4():
    """
    *  Список (list) – это структура данных для хранения объектов различных типов.
    Переменная, определяемая как список, содержит ссылку на структуру в памяти,
    которая в свою очередь хранит ссылки на какие-либо другие объекты или структуры.
    """

    lst_t = [1, 8, 3, -1]

    print("ID List:\t", id(lst_t), '\n')
    print("ID List[0]:\t", id(lst_t[0]), '\n',
          "ID List[1]:\t", id(lst_t[1]), '\n',
          "ID List[2]:\t", id(lst_t[2]), '\n',
          "ID List[3]:\t", id(lst_t[3]), sep="")
    print(id(lst_t[1]) - id(lst_t[0]),                  # если значения идут с одним шагом (lst[1] = lst[0] + 2 ...),
          id(lst_t[2]) - id(lst_t[1]),                  # то и id элементов будут отличаться в один какой-то шаг
          id(lst_t[3]) - id(lst_t[2]))

    #

    lst0 = [1, 2, 3, 4, 5]                  # инициализированный список
    lst1 = list()                           # получаем копию списка через ф-цию list('class list') (пустой список)
    lst2 = lst0[:]                          # копируем список в другой
    lst3 = list(lst0)                       # присваиваем копию list0

    #

    print("ID lst0:\t", id(lst0), '\n',     # id у всех свой!
          "ID lst1:\t", id(lst1), '\n',
          "ID lst2:\t", id(lst2), '\n',
          "ID lst3:\t", id(lst3), sep="")

    print(lst0)
    print(lst1)
    print(lst2)
    print(lst3)

    #

    list_s = [0, 1, 0, 1]
    lst0 = list_s                           # lst0 - псевдоним list_s
    lst1 = list_s                           # lst1 - псевдоним list_s
    lst2 = list_s
    lst3 = lst2                             # lst3: псевдоним lst2 - псевдоним list_s!

    print("ID lst0:\t", id(lst0), '\n',     # id у всех одинаковый!
          "ID lst1:\t", id(lst1), '\n',
          "ID lst2:\t", id(lst2), '\n',
          "ID lst3:\t", id(lst3), sep="")

    lst0[0] = 0             # [0]
    lst1[1] = 1             # [0, 1]
    lst2[2] = 2             # [0, 1, 2]
    lst3[3] = 3             # [0, 1, 2, 3]
    list_s.append("end!")   # [0, 1, 2, 3, 'end!']

    print(lst0, id(lst0))   # каждый список владеет list_s и является его ссылкой
    print(lst1, id(lst1))
    print(lst2, id(lst2))
    print(lst3, id(lst3))
    print(list_s, id(list_s))


def sas5():
    """
    *   Списковое включение (List Comprehensions) - автоматическое заполнение списка, упрощенная запись циклического
        заполнения: list = [i for i in range(n)]
        Обработчик списков (List Comprehensions) - упрощенное получение копии списка - то же списковое включение:
        copy_list = [i for i in list]
        Срезы (Slice) - start:stop:step - тройка чисел для получения подсписка, но в данном случае это именно срез,
        как отдельный тип данных <class slice>. С помощью среза можно получить копию подсписка:
        copy_list_slice = list[slice(start = 0, stop = n + 1, step = 1)]
        copy_list_slice = list[start: stop: step] - анонимная версия
    """

    lst = [1, 12, -5, 37.467, True, "end!"]
    stlist = lst[:-3]                           # получаем подсписок от 0 (по умолчанию) до -3 (6 - 3 = 3)

    st = [-2, -7, 0]

    print(lst)
    print(stlist)

    stlist.append(-3)                           # добавляем элемент в конец списка
    stlist.insert(1, 2)
    stlist.pop()                                # по умолчанию удаляется последний элемент
    temp = stlist.pop(-1)                       # удаляем элемент по индексу + возвращаем этот элемент и записываем
    print(stlist)

    stlist.clear()
    stlist.append(temp)
    # stlist.append(list(st))                   # добавляем в конец список, как целый элемент
    stlist.extend(st)                           # добавляем все элементы, как отдельные
    stlist[len(stlist):] = st                   # аналогично
    print(stlist)

    #

    stlist.remove(-2)                           # удаляем первый попавшийся элемент со значением -2
    stlist.remove(-2)
    print(stlist.count(-7))                     # возвращает количество повторений элемента

    # stlist.sort(reverse=False)                # для использования, типы данных должны быть сравнимы
    stlist.pop(1)
    stlist.sort(reverse=False)      # сортировка по возрастанию
    print(stlist)

    stlist.reverse()                # инверсия списка
    print(stlist)
    print(stlist.index(-7))         # возвращает индекс элемента

    lss = stlist.copy()             # возвращает копию списка
    print(lss)
    lss = stlist[:]                 # аналогичная запись
    print(lss)

    #
    print("\n///////////////////////////////////////////\n")
    #

    nums1 = [i for i in range(1, 6)]                        # list comprehensions (списковое включение)
    nums2 = [i ** 2 for i in nums1]
    print('nums1 = {}\nnums2 = {}'.format(nums1, nums2), '\n')

    nums0 = [i for i in range(0, 10)]                       # берем элементы из среза:
    print(nums0[:], '\n',                                   # срез (в данном случае копия)
          nums0[1:5], '\n',                                 # срез от 1 до 5 с шагом по умолчанию 1
          nums0[:-2:2], '\n',                               # срез по умолчанию от 0 до -2(8) с шагом 2
          nums0[::-1], sep="")                              # срез по умолчанию от 0 до конца с обратным шагом -1

    print(nums0)
    slc = slice(0, -1, 3)                                   # объект класса slice (отрицательный шаг не работает поч?)
    print(nums0[slc])

    #
    print("\n///////////////////////////////////////////\n")
    #

    glist = [i for i in range(1000)]
    print(type(glist), '\t\t\t', sys.getsizeof(glist), "байт")  # 8856
    gen = (i for i in glist)                                    # генератор (а не кортеж ли это часом?!)
    print(type(gen), '\t', sys.getsizeof(gen), " байт")         # 200


def sas6():

    """
    *   Кортеж (tuple) – это неизменяемая структура данных, которая по своему подобию очень похожа на список.
        Методы такие-же, как и у списка, но только те, что не изменяют сам кортеж ну или же константные методы
        Преимущества:
            1. доступ к элементам осуществляется быстрее
            2. затраты по памяти меньше
    """

    tpl1 = (1, 2, 3, 4, 5, 6, 7)
    tpl2 = tuple((1, 2, 3, 4, 5, 6, 7))
    tpl0 = tuple(tpl1)

    print(tpl2)

    tpl0.count(1)
    tpl0.index(1)
    # tpl0.insert()
    # tpl0.clear()
    del tpl0

    tpl = (i for i in range(10000))
    lst = [i for i in range(10000)]

    print("Tuple:\t", type(tpl), '\n', sys.getsizeof(tpl), sep="")  # 85176
    print("List: \t", type(lst), '\n', sys.getsizeof(lst), sep="")  # 200! - элементы хранятся где-то еще...

    print(tuple(lst[:5]))
    print(list(tpl))


def sas7():
    """
    *   Словарь (dict) представляет собой структуру данных (которая ещё называется ассоциативный массив),
        предназначенную для хранения произвольных объектов с доступом по ключу: key : value.
        Ключи уникальны!
    """

    dict1 = {"key1": 18, "key2": 19}
    dict2 = dict(alex=1, mark=2)        # через функцию
    print("Dict1:\t\t", dict1)
    print("Dict2:\t\t", dict2)

    dict2["key1"] = 12                  # добавляем пару с ключом 'key1' и значением 12 (такого ключа нет в словаре)
    dict2["key2"] = 19                  # ---//---
    dict2["alex"] = 2                   # обращаемся к ключу и меняем значение (такой ключ у нас есть)
    dict2["mark"] = 12                  # ---//---
    del dict2["key2"]                   # удаляем пару по ключу (если такого ключа нет, то выбрасывается исключение)
    # del dict2["sass"]                 # выбрасывается исключение

    if "sass" in dict2:                 # True если ключ "sass" есть в словаре
        del dict2["sass"]

    print("New dict:\t", dict2)

    #
    print("\n///////////////////////////////////////////\n")
    #

    dict1 = dict2.copy()                # возвращает копию словаря
    print(dict1)
    dict1 = dict2.fromkeys(dict2, 2)    # создает словарь с ключами из другого словаря/списка/кортежа и значением 2,
    print(dict1)                        # None по умолчанию

    print(dict1.get("alex"))            # возвращает копию значения по ключу
    print(dict1.get("sass"))            # None, если такого ключа нет

    print(dict1.items())                # возвращает список пар, где ключ-значение - кортеж
    print(dict1.keys())                 # список ключей
    print(dict1.values())               # список значений

    print(dict1.pop("sas", None))       # удаляет пару и возвращает значение, если не нашелся, то вернется None
    print(dict1)
    print(dict1.pop("key1"))            # если не нашелся, то вернется default и выбросится исключение
    print(dict1)
    print(dict1.popitem())
    print(dict1)

    #
    print("\n///////////////////////////////////////////\n")
    #

    dict1 = {"str1": 1, "str2": 2, "str3": 3, "str4": 4}
    other = dict(str1=0, str2=1, alex=5)

    print(dict1.setdefault("str3", 2))  # возвращает значение по ключу, если не нашлось, то записывает новую пару
    print(dict1)
    print(dict1.setdefault("mark", 6))
    print(dict1)
    print(dict1.setdefault("anna", 7))  # если значение не указано, то в новую пару записывается None
    print(dict1)
    dict1.update(other)                 # обновление: перезапись значений или добавление новых пар
    print(dict1)

    dict1.clear()


def sas8():
    """
    * Задача:
        Дана строка типа: xxx3[xxx5[xxx2[xxx]xxx]xxx]xxxx - где:
        x - некоторые буквы или в сумме какая-то подстрока,
        число - множитель на который нужно продублировать подстроку,
        скобки - начало и конец дублируемой строки.

    * Свойства:
        после числа (коэффициента) всегда есть открывающая скобка и перед каждой открывающей скобки
        всегда стоит коэффициент;
        у каждой открывающей скобки есть соответствующая закрывающая скобка;
        и стоит учитывать двузначные числа.

    """

    string = "abc     2[Sys 3[sUs4[Z]]]     SAS 12[ ak2[M]]"
    result = Func.get_str(string)

    print(string)
    print(result)

    # lambda function

    print((lambda x: x ** 2)(5))
    print((lambda x: x ** 2)(7))
    print((lambda x: x ** 2)(9))


def sas9():
    """
    * Исключениями (exceptions) - проблемы, возникающие в ходе выполнения программы,
    которые допускают возможность дальнейшей ее работы в рамках основного алгоритма.

    2 типа:
        1. Синхронные - эти исключения могут возникнуть только в определенных местах программы.
        Например, если у вас есть код, который открывает файл и считывает из него данные,
        то исключение типа “ошибка чтения данных” может произойти только в указанном куске кода.

        2. Асинхронные - эти исключения могут возникнуть в любой момент работы программы,
        они, как правило, связаны с какими-либо аппаратными проблемами, либо приходом данных.
        В качестве примера можно привести сигнал отключения питания.
    """

    try:
        int("sas")
    except Exception as exc:                            # Exception - родитель всех исключений
        print("Error!:\t", exc, "\ntype:\t", type(exc))

    #

    try:
        d = int(input("value:\t"))                      # символ или 0 вызовут исключение
        var = 12 / d
        print("All right!", var)
    except (ZeroDivisionError, ValueError):             # типы возможных исключений
        print()
    else:
        print("Else block")                             # блок else выполняется, если исключение не выбросилось
    finally:
        print("Finally")                                # блок finally выполняется всегда после конструкции

    #

    try:
        raise Exception("Some exception")
    except Exception as exc:
        print("Exception:\t", exc)

    #

    class NegValException(Exception):                   # наследуемся от базового класса исключений
        pass

    try:
        val = int(input("input positive number: "))
        if val < 0:
            raise NegValException("Neg val: " + str(val))   # выбрасываем свое исключение
        print(val + 10)
    except NegValException as e:
        print(e)

    #

    try:
        Func.get_exception()                           # местное раскручивание стека
    except Exception as exc:
        print("Catch!:\t", exc)


def sas10():
    """
    * Режимы доступа к файлу:
    ‘r’ – открыть файл для чтения;
    ‘w’ – открыть файл для записи;
    ‘x’ – открыть файл с целью создания, если файл существует, то вызов функции open завершится с ошибкой;
    ‘a’ – открыть файл для записи, при этом новые данные будут добавлены в конец файла, без удаления существующих;
    ‘b’ – бинарный режим;
    ‘t’ – текстовый режим;
    ‘+’ – открывает файл для обновления.
    * По умолчанию файл открывается на чтение в текстовом режиме.

    """
    # nums = map(int, input().split())
    # print(list(nums))

    try:
        open("sas.txt", 'x')                        # создаем файл
    except Exception as exc:
        print("File already created!:\t", exc)      # обрабатываем исключение, если файл уже был создан
    else:
        print("File is created!")

    file = open("sas.txt", 'w')                     # открываем файл для записи
    file.write("sas sys sus\n")
    file.write("sas sys sus\n")                     # записываем строки
    file.seek(0)                                    # устанавливаем курсор записи в позицию 0
    file.write("Start pos(0):\t")                   # перезаписываем начиная от начала (seek(0))
    file.seek(3)                                    # тоже перезапись
    file.write("pos(3): ")
    file.seek(60)                                   # задаем много большую позицию
    file.write("pos(60): some text")                # где-то в середине файла продолжаем запись (файл сильно увеличился)
    pos = file.tell()                               # текущая позиция (pos1)

    file.write(
        "\nend pos: " + str(pos) +                  # pos1
        ' ' + str(file.tell())                      # тоже pos1
    )                                               # уже pos2

    file.write(
        "\nnew pos: " +
        str(file.tell())                            # pos2
    )                                               # после записи pos3

    file.close()                                    # ручками закрываем файл

    #

    with open("sas.txt", 'r') as file:              # wist отслеживает конец работы и закрывает файл
        for line in file:                           # построчное чтение через цикл
            print(line)

        file.seek(0)                                # в начало файла

        line = file.read(5)                         # посимвольно считывание (5 символов)
        print("\nNew read:\t", line)

        line = file.readline()                      # от текущей позиции (6) считываем строку
        print("Read line:\t", line)

        line = file.readline()
        print("Read line:\t", line)

    # файл закрыт


def sas11():

    from SomeModl import some_func, some_pos

    some_func()
    print(some_pos())
    # some_result()

    import SomeModl

    SomeModl.some_result()
    some_func()
    SomeModl.some_pos()

    # import cowsay as cow
    # cow.cow("Ожидай")


def sas12():
    pass


# sas1()
# sas2()
# sas3()
# sas4()
# sas5()
# sas6()
# sas7()
# sas8()
# sas9()
# sas10()
# sas11()
sas12()
