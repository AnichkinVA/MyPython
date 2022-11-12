while True:
    try:
        visitors = int(input('Какое количество билетов вы желаете приобрести?: '))
        break
    except ValueError:
        print('Ошибка! Введите целое число больше нуля.\n   (Используйте цифры для ввода):')
while int(visitors) < 1:
    visitors = int(input('Ошибка! Введите целое число больше нуля: '))

total_cost = 0

for i in range(visitors):
    while True:
        try:
            age = int(input(f'Сколько полных лет посетителю {i + 1}? : '))
            break
        except ValueError:
            print('Ошибка! Введите целое число.\n   (Используйте цифры для ввода):')
    while int(age) < 0:
        age = int(input('Ошибка! Уточните возраст посетителя и введите количество полных лет: '))
    # age = input(f'Введите возраст посетителя {i + 1} : ')
    # while age.isalpha() or int(age) < 0:
    #     age = input('Ошибка! Введице количество полных лет: ')
    # age = int(age)
    if 18 <= age < 25:
            total_cost += 990
    elif age >= 25:
        total_cost += 1390
    else:
        total_cost = total_cost
if visitors > 3:
    total_cost = total_cost * 0.9
print('Итого:', total_cost, 'руб.')