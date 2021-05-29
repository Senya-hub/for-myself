langs = ['Python', 'Java', 'JS', 'SQL']

user_lang = input('После чего вставить: ')
i_lang = langs.index(user_lang)

langs.insert(i_lang + 1, 'C++')
print(langs)


def is_film_exist(movie, films_list):
    for i_movie in films_list:
        if i_movie == movie:
            return True
    return False

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня',
         'Проклятый остров', 'Начало', 'Матрица'
]
my_list = []

#while True:
    print('\nВаш текущий топ фильмов: ', my_list)
    new_movie = input('Название фильма: ')
    if is_film_exist(new_movie, films):
        print('Команды: добавить, удалить, вставить.')
        command = input('Введите команду: ')
        if command == 'добавить':
            my_list.append(new_movie)
        if command == 'удалить':
            if is_film_exist(new_movie, my_list):
                my_list.remove(new_movie)
            else:
                print('Такого фильма нет в нашем рейтинге.')
        if command == 'вставить':
            index = int(input('На какое место: '))
            my_list.insert(index - 1, new_movie)
    else:
        print('Такого фильма нет на сайте! ')


def is_repeat(movie, film_list):
    for i_mov in film_list:
        if i_mov == movie:
            return True
    return False

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня',
         'Проклятый остров', 'Начало', 'Матрица'
]
my_films = []

#while True:
    print('\nВаш текущий топ фильмов: ', my_films)
    new_movie = input('Название фильма: ')
    if is_repeat(new_movie, films):
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command == 'добавить':
            if is_repeat(new_movie, my_films):
                print('Этот фильм уже есть в вашем списке.')
            else:
                my_films.append(new_movie)
        if command == 'вставить':
            index = int(input('Введите номер: '))
            my_films.insert(index - 1, new_movie)
        if command == 'удалить':
            my_films.remove(new_movie)
    else:
        print('Данного фильма нет на нашем киносайте.\n')


zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

zoo.insert(1, 'bear')
for i_animal in zoo:
    if i_animal == 'elephant':
        zoo.remove(i_animal)

print('Зоопарк: ', zoo)
num = zoo.index('lion')
print('Лев сидит в клетке номер', num + 1)
number = zoo.index('monkey')
print('Обезьяна сидит в клетке номер', number +1)


total_person = int(input('Кол-во сотрудников: '))
salary = []
count = 0

for num in range(1, total_person + 1):
    print('Зарплата', num, 'сотрудника: ', end='')
    amount_sal = int(input())
    if amount_sal != 0:
        salary.append(amount_sal)
        count += 1
print('\nОсталось сотрудников: ', count)
print('Зарплаты: ', salary)
a = max(salary)
print('\nСамая высокая зарплата: ', a)
b = min(salary)
print('Самая низкая зарплата: ', b)