# exercise 8.1
# запрашиваем у пользователя размеры шоколадки n и m, а также количество долек k
n, m, k = map(int, input("Введите через пробел размеры шоколадки (n, m) и количество долек (k): ").split())

# проверяем, можно ли отломить k долек от шоколадки
if k <= n * m and (k % n == 0 or k % m == 0):
    print("->yes")
else:
    print("->no")