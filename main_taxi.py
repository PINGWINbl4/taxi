while True:
    try:
        numb = int(input('Введите колличество сотрудников'))
        break
    except(ValueError, TypeError):
        print(print('Некорректное значение'))

sotr = []
taxi = []
print('Введите расстояния до домов сотрудников')

for i in range(numb):
    while True:
        try:
            Value = int(input('Расстояние до дома сотрудника'))
            break
        except(ValueError, TypeError):
            print(print('Некорректное значение'))
    sotr.append(Value)
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
    print('Сотрудник с расстоянием до дома', max(sotr), 'Поедет на такси с тарифом', min(taxi))
    sotr.remove(max(sotr))
    taxi.remove(min(taxi))
