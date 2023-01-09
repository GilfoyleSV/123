x = input('Введите число:')
lenght = len(x)
index_first_num = 0

if float(x) < 1:

    for i in x:

        if i in '123456789':
            index_first_num = x.index(i)
            break

    print("Формат плавающей точки: " + x[index_first_num] + '.' + x[index_first_num + 1: lenght] + f' * 10 ** {-(index_first_num - 1)}')

else:
    print('Формат плавающей точки: ' + x[0] + '.' + x[1:] + f' * 10 ** {lenght - 1}')
