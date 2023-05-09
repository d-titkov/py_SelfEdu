# exercise 6.1
# запрашиваем у пользователя номер билета
ticket_number = input("Введите номер билета (6 цифр): ")

# вычисляем суммы первых трех и последних трех цифр
sum_first_half = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
sum_second_half = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

# проверяем, является ли билет счастливым
if sum_first_half == sum_second_half:
    print("->yes")
else:
    print("->no")