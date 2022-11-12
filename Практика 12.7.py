bank_conditions = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}    # словарь - названия банков
                                                                        # и процентные ставки по депозитам
interest_rate = [] # создаем список процентных ставок

for key in bank_conditions.keys():
    interest_rate.append(bank_conditions[key])     # наполнили список значениями процентных ставок

you_money = int(input('Введите размер депозита: '))    # запрашиваем размер депозита

# рабочий код!!!
# accumulation = list(map(int, [i * (you_money / 100) for i in interest_rate]))    # вычисляем размер накопленных процентов на
                                                                                 # сумму согласно указанной ставки банка

# accumulation = list(map(lambda x: x * you_money / 100, interest_rate))  # вычисляем размер накопленных процентов на
                                                                          # сумму согласно указанной ставки банка
                                                                          # (еще один вариант, но он мне менее понятен)

accumulation = list([i * (you_money / 100) for i in interest_rate])    # если отключить рабочий код и включить этот
accumulation = list([round(i, 2) for i in accumulation])               # то мы получим округдение до 2 знаков

print('Размер процентов в разных банках составит: ', ", ".join(map(str, accumulation)))    # вывод накопленных за год процентов

print('Максимальная сумма, которую вы можете заработать:', max(accumulation))    # вывод максимальных годовых процентов



