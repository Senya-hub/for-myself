client = 'Петя'
print(client)
print(' и ')
pet = 'Кот'
print(pet)

r = 'Red'
b = 'Blue'
g = 'Green'
print(r, b, g, r + g + b, b, g + b + '.')

first_animal=input('Первое животное: ')
second_animal=input('Второе животное: ')
print(first_animal + ' спит, ' + second_animal + ' идет')

name=input('Введите имя: ')
sur_name=input('Введите фамилию: ')
print('Вас зовут')
print(name)
print(sur_name)


name=input('Введите имя: ')
sur_name=input('Введите фамилию: ')
city=input('Введите город проживания: ')
print('==========')
print('Вас зовут ' + name + ' ' + sur_name)
print('Вы живете в городе ' + city)

first_name=input('Введите имя пользователя: ')
greeting=('Привет, ')
print(greeting, first_name)
intro=('К сожалению, у Вас нет доступа к системе.')
print(intro)
intro=('Пожалуйста, обратитесь к системному администратору.')
print(intro)

from_city=input('Введите город вылета: ')
to_city=input('Введите город прилета: ')
print(from_city + ' - ' + to_city)

user=input('Введите пользователя: ')
new_file=input('Введите имя файла: ')
print('Путь к файлу: ' + 'C:/' + user + '/docs/folder/' + new_file + '.txt')

a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
c = a
a = b
b = c
print(a, b)