user_name = input('Введите пользователя: ')
file_name = input('Введите имя файла: ')

path1 = 'c:/{user}/docs/folder/{new_file}.txt'.format(
   user = user_name, 
   new_file = file_name
)

path_1 = 'c:/{0}/docs/folder/{1}.txt'.format(
  user_name, 
  file_name
)

path_2 = f'c:/{user_name}/docs/folder/{file_name}.txt'

print('Путь к файлу: ', path1)
print('Путь к файлу: ', path_1)
print('Путь к файлу: ', path_2)

# Цикл заучить.------------------------------------------
while True:
  grats_template = input('Введите поздравления,'
                         'в шаблоне нужно использовать конср. {name}: ')
  if '{name}' in grats_template:
    break
  print('Ошибка: в шаблоне отсутсвует конструкция {name}.')

print('Введите список имен (заканчивается на end): ')
name_list = []
while True:
  name = input('Имя: ')
  if name != 'end':
    name_list.append(name)
  else:
    break

for i_name in name_list:
  print(grats_template.format(name=i_name))
#-------------------------------------------------------

name_1 = input('Имя: ')
number_1 = int(input('Номер заказа: '))

num = 'Здравствуйте, {name}! Ваш номер заказа: {number}. Приятного дня!'.format(
  name = name_1, 
  number = number_1
)

print(num)



name = input('Введите имя: ')
number = int(input('Введите долг: '))

num = '{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!'.format(
  name, 
  number
)
print(num)

#-----------------------------------------------------------
ip_address = []
j = 1

while True:
  if j <= 4:
    print('Введите', j, 'число: ', end='')
    num_address = int(input())
    if num_address >= 0 and num_address <= 255:
      ip_address.append(num_address)
      j += 1
    else:
      print('\nОшибка! Число должно быть больше 0 и меньше 255')
  else:
    break
c = '{0}.{1}.{2}.{3}'.format(
   ip_address[0],
   ip_address[1],
   ip_address[2],
   ip_address[3]
)    

print('\n', c)