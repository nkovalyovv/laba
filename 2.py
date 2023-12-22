def ispowers(k):
    while k % 5 == 0:
        k = k/5
    if k == 1:
        return True
    else:
        return False

kot = 0
count = 0
while kot < 10:
    number = input('Введите целое положительное число: ')
    if number.isdigit() == True:
        number = int(number)
        if ispowers(number):
            count += 1
        print('Количество степеней числа 5: ', count)
        kot += 1
    else:
        print('Ошибка!Введите коректное значение!')
    