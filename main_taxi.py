while True:     # Ввод колличества сотрудников и обработка на ошибки ввода
    try:
        numb = int(input('Введите колличество сотрудников'))
        break
    except(ValueError, TypeError):
        print(print('Некорректное значение'))

sotr = []
taxi = []
final_list = []
print('Введите расстояния до домов сотрудников')

for i in range(numb):   # Ввод расстояния сотрудников, обработка на ошибки ввода и внесение в массив
    while True:
        try:
            Value = int(input('Расстояние до дома сотрудника'))
            break
        except(ValueError, TypeError):
            print(print('Некорректное значение'))
    sotr.append(Value)
    final_list.append(Value)
print('Введите тарифы таксистов')

for i in range(numb):   # Ввод тарифа таксиста, обработка на ошибки ввода и внесение в массив
    while True:
        try:
            Value = int(input('Тариф таксиста'))
            break
        except(ValueError, TypeError):
            print(print('Некорректное значение'))
    taxi.append(Value)

for i in range(len(sotr)):  # Анализ данных, сортировка иформирование результирующего массива
    final_list[sotr.index(min(sotr))] = taxi.index(max(taxi))+1
    sotr[sotr.index(min(sotr))] = 1001
    taxi[taxi.index(max(taxi))] = -1
print(final_list)
