# Начинаем изучать списки.
numbers_list = [1, 5, 2, -7, 6]
for i in range(5):
    new_num = int(input('Введите число: '))
    numbers_list.append(new_num)
for number in numbers_list:
    print(number, '** 2 = ', number ** 2)


#Регистрация книг
books_ID = [50, 34, -1, -1, 2, 23, -1]
new_books_ID =[]
returned = 0

for _ in range(10):
    id = int(input('Введите ID книги: '))
    books_ID.append(id)

for id in books_ID:
    if id == -1:
        returned += 1
    else:
        new_books_ID.append(id)

print('Новый список выданных книг: ', new_books_ID)
print('Вернули за день: ', returned)


numbers = [3, 7, 5]

#while True:
 number = int(input('Новое число: '))
 numbers.append(number)
 print('Текущий список чисел:', numbers)

 for i in numbers:
   print(i ** 2, i ** 3, i ** 4, sep = '\t')
 print()


numbers_list = []
for i in range(101):
    numbers_list.append(i)
print(numbers_list)

emplyee = int(input('Введите кол-во сотрудников: '))
list_ID = []
for _ in range(emplyee):
    emplyee_ID = int(input('ID сотрудника: '))
    list_ID.append(emplyee_ID)
look_ID = int(input('Какой ID ищем? '))
for i in list_ID:
    if i == look_ID:
        print('Сотрудник работает!')
        break
    else:
        print('Сотрудник не работает!')


    scores = [3, 5, 10, 7, 6]
print(scores)

scores[1] *= 3
x = scores[4]
x += 10
scores[3] = x

print(x)
print(scores)


monsters_count = int(input('Кол-во монстров: '))
mage_index = int(input('Номер мага в списке: '))
monsters_damage = []

for monster in range(monsters_count):
    print('Урон у ', monster + 1, 'мотстра', end = ' ')
    damage = int(input(''))
    monsters_damage.append(damage)

for i_monster in range(monsters_count):
    if monsters_damage[i_monster] < 100 and i_monster != mage_index - 1:
        monsters_damage[i_monster] += monsters_damage[mage_index - 1]


print(monsters_damage)


nums_list = []
N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)
maximum = nums_list[0]
minimum = nums_list[0]
for i in nums_list:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i
print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)


N = int(input('Кол-во чисел в списке: '))
number_determine = []
a = 0

for i in range(1, N + 1):
    print('Введите ', i, ' число:', end = ' ')
    number = int(input())
    number_determine.append(number)
print(number_determine)

divider = int(input('Введите делитель: '))

for i_num in range(N):
    if number_determine[i_num] % 10 == 0:
        print('Индекс числа: ', number_determine[i_num], ' : ', i_num)
        a += i_num
print('Сумма индексов: ', a)


amount_dog = int(input('Введите кол-во собак: '))
max_dog = 0
min_dog = 0
summ_dogs = []

for i in range(1, amount_dog + 1):
    print('Очки ', i, 'собаки: ', end = ' ')
    glasses = int(input())
    summ_dogs.append(glasses)
print(summ_dogs)

max_dog = summ_dogs[0]
min_dog = summ_dogs[0]
for i in summ_dogs:
    if max_dog < i:
        max_dog = i
    if min_dog > i:
        min_dog = i
print(max_dog, min_dog)
max_dog, min_dog = min_dog, max_dog
print(max_dog, min_dog)