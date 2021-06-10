def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)

prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_percent = int(input('Повышение на первый год: '))
second_percent = int(input('Повышение на второй год: '))

first_percent = [get_higher_price(first_percent, i_price) for i_price in prices_now]
second_percent = [get_higher_price(second_percent, i_price) for i_price in first_percent]

print('Сумма цен за кaждый год: ', round(sum(prices_now), 2), 
      round(sum(first_percent), 2), round(sum(second_percent), 2))


# squares = []
# for i in range(10):
#     squares.append(i ** 2)

squares = [i ** 2 for i in range(10)]

print(squares)


left_num = int(input('Левая граница: '))
right_num = int(input('Правая граница: '))

sc_list = [x ** 2 for x in range(left_num, right_num + 1)]
kv_list = [x ** 3 for x in range(left_num, right_num + 1)]

print('\nСписок квадратов чисел в диапазоне от', left_num, 'до', right_num, ': ', sc_list)
print('Список кубов чисел в диапазоне от', left_num, 'до', right_num, ': ', kv_list)


line = input('Введите строку: ')
sym = input('Введите дополнительный символ: ')

lin_list = [x * 2 + sym for x in line]

print(lin_list)


def in_goods(good):
    goods_list = []
    for i in range(1, goods + 1):
        print('Введите стоимость', i, 'товара: ', end='')
        pr = float(input())
        goods_list.append(pr)
    return goods_list

def fr_ls(good, price):
    return round(good * (1 + price / 100), 2)

goods = int(input('Введите кол-во товаров: '))
price_first = int(input('Повышение на первый год: '))
price_second = int(input('Повышение на второй год: '))

goods_list = in_goods(goods)
price_first = [fr_ls(i_good, price_first) for i_good in goods_list]
price_second = [fr_ls(i_good, price_second) for i_good in price_first]

print('\nСумма цен за каждый год: ', sum(goods_list), sum(price_first), sum(price_second))


# squares = []
# for i in range(10):
#     if i % 2 != 0:
#         squares.append(i ** 2)

squares_adds = [x ** 2 for x in range(10) if x % 2 != 0]
squares_cubs = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(10)]

print(squares_adds)
print(squares_cubs)

import random

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_3_condition = [('Погиб' if squad_1[i_damage] + squad_2[i_damage] > 100
                      else 'Выжил')
                     for i_damage in range (10)]

print('Урон первого отряда: ', squad_1)
print('Урон второго отряда: ', squad_2)
print('Состояние третьего отряда: ', squad_3_condition)


left = int(input('Введите число левой границы: '))
right = int(input('Введите число правой границы: '))

my_list = [x for x in range(left, right) if x % 2 == 0]
print(my_list)


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

original_prices = [(x if x > 0 else 0) for x in original_prices]

print(original_prices)


import random

original_prices = [random.randint(-20, 20) for _ in range(15)]
new_prices = original_prices[:]

for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

print(original_prices)
print(new_prices)
print("Мы потеряли: ",  abs(sum(original_prices) - sum(new_prices)))


nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
print(nums[:5])

two = nums[:]
two = [nums[i] for i in range(len(nums) - 2)]
print(two)

two = nums[:]
two = [two[i] for i in range(len(nums)) if i % 2 == 0]
print(two)

two = nums[:]
two = [two[i] for i in range(len(nums)) if i % 2 != 0]
print(two)

two = nums[:]
two = [x for x in nums[:: -1]]
print(two)

two = nums[:]
two = [x for x in nums[:: -2]]
print(two)


