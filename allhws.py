import re
import fractions
import calendar

def task1(a, b):
    return a + b, a * b

def task2(a, b):
    return (a + (b ** 0.5)) ** 0.5

def task3():
    numbers = [a for a in range(10, 50, 5) if a % 3 != 0]
    return numbers

def task5(celcius):
    return celcius * 32

def task6(m, por):
    money = (((por / 100) + 1) * m) * 5
    return money

def task7(w, m, y):
    return (w * 7) + (m * 30) + (y * 365)

def task8(a):
    b = 2
    list = []
    while b * b <= a:
        if a % i:
             b += 1
        else:
            a //= b
            list.append(b)
    if a > 1:
        list.append(a)
    return list

def task9(a):
    output = {1, a}
    for z in range(2, int(a ** 0.5) + 1):
        if a % z == 0:
            output.update((z, a // z))
    return output

def task10(a1, a2, b1, b2):
    location = ((((a2 - a1) ** 2) + ((b2 - b1) ** 2)) ** 0.5)
    return location

def task11(a):
    sqrs = []
    for i in range(1, a):
        if i ** 2 < a:
            sqrs.append(i ** 2)
    return sqrs

def task12(a, fro, limit):
    a_noa = sum(a[fro:limit + 1])
    return a_noa

def task13(size, price):
    a = [price for _ in range(size)]
    return a

def task14(a, num):
    for i in a:
        if i == num:
            a.remove(i)
    return a

def task15(a):
    max_num = a.index(max(a))
    min_num = a.index(min(a))
    a[max_num], a[min_num] = a[min_num], a[max_num]
    return int("".join(map(str, a)))

def task16(a):
    for z, valor in enumerate(a):
        if a[z] > a[z - 1]:
            orden = False
        else:
            orden = True

def task17(a):
    num = int(len(a) / 2)
    if a[num:] == a[:num][::-1]:
        return True
    else:
        return False

def task18(letter_,*args ):
    return ' '.join([word for word in letter_.split() if not any(letter in word for letter in args)])

def task19(IP):
    adress = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", IP)
    return bool(adress) and all(map(lambda n: 0 <= int(n) <= 255, adress.groups()))

def task20(s):
    numeros = [int(i) for i in s if i.isdigit()]
    return int("".join(map(str, numeros)))

def task21(a):
    num_par = []
    num_impar = []
    [num_par.append(i) if i % 2 == 0 else num_impar.append(i) for i in a]
    return sum(num_par) / len(num_par), (sum(num_impar) / len(num_impar))

def task22(a):
    return [index for index, value in enumerate(a) if value != 0]

def task23(a, num):
    return min(a, key=lambda x: abs(x - num))

def task24(s):
    return "".join(["{0}c{0}".format(l) if l in "ауеэоыяиюaeiou" else l for l in s])

def task25(a):
    return max([sum(i) for i in list(zip(a, a, a[1:]))])

def task26(a):
    return not a == list(set(a))

def task27(a):
    return [i for i, b in enumerate(a) if 0.90 * max(a) < b < 1.10 * max(a)]

def task28(a, a1, b):
    return [i * -1 if a1 < i < b else i for i in ar]

def task29(a1, a2):
    return a1 == a2


def task30(a):
    return sorted(a, key=bool)[::-1]


def task31(a):
    return a[::2]

def task32(a):
    max_a = a.index(max(a))
    a.remove(a[max_a])
    max_b = a.index(max(a))
    return [max_a, max_b]

def task33(a):
    return sorted(a)[-1] - sorted(a)[-2]

def task34(a):
    return calendar.month_name[a]

def task35(a):
    return 'WINTER' if 0 < n <= 3 \
        else 'SUMMER' if 7 <= n <= 9 \
        else 'SPRING' if 4 <= n <= 6 \
        else 'AUTUM'

def task36(a, b):
    return dict(zip(a, b))


def task37(a):
    b = dict()
    for i, c in a.items():
        b.setdefault(c, []).append(i)
    return str(b).replace("[", "(").replace("]", ")")

def task38(a):
    return dict(map(reversed, a.items()))

def task39(a, b, c):
    b0 = dict_.get(a)
    c[a] = (b0, b) if a in c else c.setdefault(a, b)
    return c

def task40(a):
    a = int(input('Enter a: '))
    b = {}
    v = {b.setdefault(k + 1, (k + 1) ** 2) for k in range(a)}
    return d

def task41(a, b):
    return np.random.randint(23, size=(a, b))


def task42(a):
    return max(map(max, a)), min(map(min, a))

def task43(a):
    return tuple(max(i) for i in a)

def task44(a):
    return tuple(max(i) for i in zip(*a))

def task45(a):
    a = np.array(a)
    num_max = np.max(a)
    a[a >= num_max] = 0
    return a

def task46(a):
    siz = np.shape(a)
    b = np.ones((siz[0], siz[1]))
    b[1:-1, 1:-1] = 0
    return b

def task47(a):
    b = [b for list in c for item in list]
    return max(set(b), key=b.count)

def task48(a, r1, r2):
    output = np.array(a)
    output[[r1, r2]] = output[[r2, r1]]
    return output

def task49(a, c1, c2):
    output = np.array(a)
    output[:, [c1, c2]] = output[:, [c2, c1]]
    return output

def task50(a1, a2):
    if len(a1) == len(a2):
        return  [i * j for i, j in zip(a1, a2)]
    else:
        return np.diff(a1 + a2)

def task51(a):
    lineas = [linea.count(0) for linea in a]
    max_num = lineas.index(max(lineas))
    a.remove(a[max_num])
    return a

def task52(a):
    array = {}
    new_array = ''
    if type(a) == str:
        for l in a:
         array[l] = array.get(l, 0) + 1
        return array
    else:
        for i in a:
         new_array += i[0] * i[1]
        return new_array

def task53(a):
    d = 1
    n = 1
    for i in a:
        n *= i[0]
        d *= i[1]
    if f.Fraction(n, d):
        return f.Fraction(n, d)
    else:
        return f'{numerador}/{denominador}'

def task54(precio, carro):
    return sum([precio[i] * carro[i] for i in precio and carro])
