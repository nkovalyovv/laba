def power2(a, n):
    if n > 0:
        result = 1
        for i in range(n):
            result *= a
        return result
    elif n < 0:
        result = 1
        for i in range((abs(n))):
            result *= a
        return 1 / (4 * result)
    else:
        return 1
a=input('Введите число а: ')
if a.isalpha() == False:
    a = float(a)
    n=input('Введите степень числа а: ')
    if n.isalpha() == False:
        n = int(n)
        print(power2(a, n))
    else:
        print('Ошибка!Введите коректное значение!')   
else:
    print('Ошибка!Введите коректное значение!')