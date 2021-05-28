N = int(input('Введите целое число: '))

numbers_list = []

for i in range(1, N + 1):
    if i % 2 != 0:
        numbers_list.append(i)
print(numbers_list)


nam = 'Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар'
name_list = list(nam)

for i in range(1, len(name_list) + 1):
    if i % 2 == 0:
        print(name_list[i - 1])


amount = int(input('Кол-во клеток: '))

cell_list = []
a = []

for i in range(1, amount + 1):
    print('Эффективность', i, 'клетки:', end=' ')
    effect = int(input())
    cell_list.append(effect)
    if i - 1 > effect:
        a.append(cell_list[i - 1])

print('\nНеподходящие значения: ', end='')
for n in a:
    print(n, end=' ')


amount_card = int(input('Кол-во видеокарт: '))
card_list = []
new_card_list = []
max_card = 0

for n in range(1, amount_card + 1):
    print(n, 'Видеокарта:', end=' ')
    nam_card = int(input())
    card_list.append(nam_card)
    if nam_card > max_card:
        max_card = nam_card
for i in card_list:
    if i != max_card:
        new_card_list.append(i)

print('\nСтарый список видеокарт:', card_list)
print('Новый список видеокарт:', new_card_list)


films = 'Крепкий орешек', 'Назад в будущее', 'Таксист',\
        'Леон', 'Богемская рапсодия', 'Город грехов',\
         'Мементо', 'Отступники', 'Деревня'
films_list = list(films)
like_film = []

in_film = input('Введите фильм: ')
while in_film != 'end':
    count = 0
    for index in range(9):
        if films_list[index] == in_film:
            like_film.append(in_film)
        else:
            count += 1
    if count == 9:
        print('Ошибка! Фильм не входит в топ.')
    in_film = input('Введите фильм или end: ')
print('\nСписок любимых фильмов: ', end='')
for i in range(len(like_film)):
    print(like_film[i], ',', end=' ')


originalWord = input('Введите слово: ')
word = list(originalWord)
count = len(word)

for a in range(len(word)):
    for b in range(a + 1, len(word)):
        if word[a] == word[b]:
            count -= 1

print('Кол-во уникальных букв: ', count, ', а повторяющих эти буквы: ', len(word) - count)


total_con = int(input('Кол-во контейнеров: '))
con_list = []

for _ in range(total_con):
    con_weight = int(input('Введите вес контейнера: '))
    if con_weight < 200:
        con_list.append(con_weight)
    else:
        print('Ошибка! Вес не должен превышать 200.')
new_con = int(input('\nВведите вес нового контейнера: '))
for i in range(total_con):
    if new_con > con_list[i] :
        n = i
print('\nНомер, куда встанет новый контейнер:', n)


num = [1, 2, 3, 4, 5]
num_list = [1, 4, -3, 0, 10]


step = int(input('Сдвиг: '))
if step == 1:
    print('Изначальный список: ', num)
    first_num = num
    a = len(num) - step
    num.insert(-len(num), num[a])
    num.pop(a + 1)
    print('Сдвинутый список: ', num)
elif step == 3:
    print('Изначальный список: ', num_list)
    for i in range(1, step):
        num_list.insert(i + step + 1, i)
        num_list.pop(0)
    print('Сдвинутый список: ', num_list)


word = list(input('Введите слово: '))
n = 0
symbol = 0

for i in range(len(word) - 1, -1, -1):
    if word[i] == word[n]:
        symbol += 1
    n += 1
if n == symbol:
    print('\nСлово является палиндромом')
else:
    print('\nСлово не является палиндромом')