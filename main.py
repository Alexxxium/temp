import math


def sas1():

    print("Value:\t", 3, "\nID:\t\t", id(3))
    number = 3
    print("\nValue:\t", number, "\nID:\t\t", id(number))
    number2 = 3
    print("\nValue:\t", 3, "\nID:\t\t", id(3))
    print("\nValue:\t", number2, "\nID:\t\t", id(number2))

    a = 5                                           # id A = 140711960048552
    b = 7                                           # id B = 140711960048616
    print("\nA:\t", a, "\nB:\t", b)
    print("\nID A:\t", id(a), "\nID B:\t", id(b))

    a = b                                           # id A = id B = 140711960048616
    print("\nA:\t", a, "\nB:\t", b)
    print("\nID A:\t", id(a), "\nID B:\t", id(b))

    b = 1                                           # id A = 140711960048616,
    print("\nA:\t", a, "\nB:\t", b)                 # id B = new id (140711960048424)
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

    d += 5                                          # D получила новый адрес!
    print("\nC:\t", c, "\nD:\t", d)
    print("\nID C:\t", id(c), "\nID D:\t", id(d))

    #
    print("\n///////////////////////////////////\n")
    #

    num = None                                      # id ...28
    print("\nNum:\t", num, "\nNum id:\t", id(num))
    num = 12                                        # new id: ...76
    print("\nNum:\t", num, "\nNum id:\t", id(num))
    num = 12                                        # optimisation: id = ...76
    print("\nNum:\t", num, "\nNum id:\t", id(num))
    num = 13                                        # new id: ...08
    print("\nNum:\t", num, "\nNum id:\t", id(num))

    #
    print("\n///////////////////////////////////\n")
    #

    listS = [1, 3, 4, 9, 0]                         # list id: ...04 (const)

    print("\nList:\t\t", listS,
          "\nList id:\t", id(listS))
    print("\nList[0]:\t", listS[0],                 # list[index] id: ...80
          "\nList[0] id:\t", id(list[0]))

    listS[0] = -3.14                                # list[index] id: new id - ...40

    print("\nList:\t\t", listS,                     # list id: ...04
          "\nList id:\t", id(listS))
    print("\nList[0]:\t", listS[0],
          "\nList[0] id:\t", id(list[0]))


def sas2():
    a = 5
    b = 3

    print(a / b)                # float
    print(a % b)
    print(a // b)               # целая часть
    print(a ** b)               # возведение в степень

    print("\n//////////////////////////////////////\n")

    x = 2 + 1j                  # комплексные числа
    z = complex(4, - 5)         # через функцию

    print(x + z)
    print(x - z)
    print(x / z)
    # print(x % z)              not working
    # print(x // z)
    print(x ** z)

    print((x + z).real)         # действительная часть (обращаемся к анонимному объекту через .)
    print((x + z).imag)         # мнимая часть

    y = 6 + 1j
    print(y.conjugate())        # комплексно-сопряженное число

    print("\n//////////////////////////////////////\n")

    p = 41                      # 101001
    q = 19                      # 010011

    print(p | q)                # 111011
    print(p & q)                # 000001
    print(p ^ q)                # 111010
    print(~p)                   # нет unsigned чисел

    print(p << 1)               # ...0101001 << 1 = 1010010
    print(p >> 1)               # ...0101001 >> 1 = 0010100 (при сдвиге за 2^0 значения 1 стираются)

    print("\n//////////////////////////////////////\n")

    num = 7589142               # cc 10

    print(hex(num))             # cc 16
    print(oct(num))             # cc 8
    print(bin(num))             # cc 2

    print("\n//////////////////////////////////////\n")

    # import math

    pi = math.pi                # число п
    e = math.e                  # число е

    print("\npi:\t", pi)
    print("e:\t", e)

    print(math.ceil(pi))        # округление к большему значению до целых
    print(math.fabs(-3.14))     # абсолютное значение: 3
    print(math.factorial(5))    # 1 * 2 * 3 * 4 * 5
    print(math.floor(pi))       # целая часть

    print(math.log2(16))        # логарифм от 16 по основанию 2
    print(math.log10(1000))     # десятичный логарифм
    print(math.log(e * 16))     # по умолчанию натуральный логарифм от e * 16
    print(math.log(15, 3))      # логарифм от 15 по основанию 3

    print(math.sin(45))
    print(math.cos(-45))


def sas3():
    lst = [1, 2, 3, 4, 5, 6, True]
    print(lst)

    for i in range(len(lst)):           # по умолчанию от 0 и до длины списка
        if lst[i] % 2 == 0:
            lst[i] += 1
        elif lst[i] == 5:
            lst[i] = 0
        else:
            lst[i] -= 1

    print(lst)

    for i in lst:                       # в i копируется объект
        i *= -1
        print(i)

    print(lst)

    count = 0
    while count < len(lst):
        lst[count] = None
        count += 1

    print(lst)


# sas1()
# sas2()
sas3()
