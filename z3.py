a = int(input('введите любое число- '))
b = int(input('введите вашу степень '))
r = 1 # начальное значение 1 потому что при умножении ничего не меняется

if b > 0:
        for i in range(b+1):
            if i == 0:
                continue

            r*=a
        print(r)
