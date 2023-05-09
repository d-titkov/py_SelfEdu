# exercise 4.
# запрашиваем у пользователя значения выручки и издержек
revenue = float(input("Введите выручку фирмы: "))
expenses = float(input("Введите издержки фирмы: "))

# вычисляем прибыль или убыток
profit = revenue - expenses
if profit > 0:
    print("Финансовый результат - прибыль. Ее величина:", profit)
    # вычисляем рентабельность выручки
    profitability = profit / revenue
    print("Рентабельность выручки =", profitability)
    # запрашиваем у пользователя численность сотрудников
    employees = int(input("Введите численность сотрудников фирмы: "))
    # вычисляем прибыль на одного сотрудника
    profit_per_employee = profit / employees
    print("Прибыль фирмы в расчете на одного сотрудника =", profit_per_employee)
else:
    print("Финансовый результат - убыток. Его величина:", profit)