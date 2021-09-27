while True:
    try:
        numb = int(input('Введите колличество сотрудников'))
        break
    except(ValueError, TypeError):
        print(print('Некорректное значение'))

sotr = []
taxi = []
final_list = []
print('Введите расстояния до домов сотрудников')

for i in range(numb):
    while True:
        try:
            Value = int(input('Расстояние до дома сотрудника'))
            break
        except(ValueError, TypeError):
            print(print('Некорректное значение'))
    sotr.append(Value)
    final_list.append(Value)
print('Введите тарифы таксистов')

for i in range(numb):
    while True:
        try:
            Value = int(input('Тариф таксиста'))
            break
        except(ValueError, TypeError):
            print(print('Некорректное значение'))
    taxi.append(Value)

for i in range(len(sotr)):
    final_list[sotr.index(min(sotr))] = taxi.index(max(taxi))+1
    sotr[sotr.index(min(sotr))] = 1001
    taxi[taxi.index(max(taxi))] = -1
print(final_list)
