# Кто написал "Евгений Онегин"
two = 0
for a in range(5):
  answer = input('Кто написал произведение? ')
  if (answer == 'Пушкин') or (answer == 'пушкин'):
    print('Правильно!')
    break
  print('Неправильно! Два!')
  two += 1
print('Получено двоек: ', two)

# Робот-начальник
answer = ''
while answer != 'Да, конечно, сделал':
  answer = input('Ты выполнил задание, которые выдавал вчера? ')

# Купи слона
name = input('Как тебя зовут? ')
print(name, 'Купи слона!')
while True:
  ask = input('')
  print('Все говорят', ask, ', а ты купи слона!')

  # Символ в отдельной строке
word = 'Python!'
for sym in word:
  print(sym)

# Три раза в отдельной строке
word = input('Введите слово: ')
for sym in word:
  print(sym * 3)

# Доска
print('-' * 10)
for n in range(4):
  print('|00000000|')
print('-' * 10)

# Локальная сеть
number = int(input('Введите первый номер адреса: '))
diference = int(input('Введите разность: '))
summ = 0

print('\nIP-адрес:', end = ' ')
for u in range(3):
  print(number, end = '.')
  number += diference
  summ += number
print(summ)

# Табло
number = int(input('Введите число: '))
func = 10

if number <= 0:
  print('\nСчет еще не открыт!')
print('\n-=-', end = '')
for n in range(number // 10):
  print(func, end = '-=-')
  func += 10
print('\n')
