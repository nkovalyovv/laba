def head3(n):
    if n < 10:
        return 3 * 10 + n
    else:
        return head3(n // 10) * 10 + n % 10
n = input('Введите число: ')
if n.isdigit() == True:
    n = int(n)
    print(head3(n))
else:
    print('Ошибка!Введите коректное значение!')
