#Сформировать список из  N членов последовательности.Для N = 5: 1, -3, 9, -27, 81 и т.д.
n = int(input('Введите число: '))

def number(n):
    return [((-3)**i) for i in range(n)]

print (number(n))