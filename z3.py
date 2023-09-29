a = int(input('введите любое число- '))
b = int(input('введите вашу степень '))
r = 1

if b > 0:
        for i in range(b+1):
            if i == 0:
                continue

            r*=a
        print(r)
