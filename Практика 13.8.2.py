total_cost = 0

def add():
    if 18 <= age < 25:
        return 990
    elif age >= 25:
        return 1390
    else:
        return total_cost

while True:
    try:
        visitors = int(input('Какое количество билетов вы желаете приобрести?: '))
        break
    except ValueError:
        print('Ошибка! Введите целое число больше нуля.\n   (Используйте цифры для ввода):')
while int(visitors) < 1:
    visitors = int(input('Ошибка! Введите целое число больше нуля: '))

for i in range(visitors):
    while True:
        try:
            age = int(input(f'Сколько полных лет посетителю {i + 1}? : '))
            break
        except ValueError:
            print('Ошибка! Введите целое число.\n   (Используйте цифры для ввода):')
    while int(age) < 0:
        age = int(input('Ошибка! Уточните возраст посетителя и введите количество полных лет: '))
    total_cost = total_cost + add()

if visitors > 3:
    total_cost = total_cost * 0.9
print('Итого:', total_cost, 'руб.')
