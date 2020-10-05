# циклы (операторы циклов)

# оператор цикла while

number = 0

# while number < 10:
#    if
#   print(number)
# number += 1 # number = number + 1

while number < 10:
    if number == 5:
        break  # то вызываем инструкцию break, которая прерывает цикл

    print(number)
    number += 1
# пример прерывания бесконечного цикла с использованием break
# while True:
#    s = input("Введите команду: ")
#    print(f"Вы ввели команду: {s}")
#   if s.lower == "стоп":
#       break

# пропуск куска кода из тела цикла  
# while True:
#    s = input("Введите слово 'ЙИЭС': ")
#   if s != "NO":
#       print("вы не ввели слово 'ЙИЭС'!!! :(( ")
#       continue
#    print(f"Вы ввели команду: {s}")
#    break    


# Оператор цикла for 

#for n in [1,2,3,4,5,6]:
#    print(n)

my_tuple = (100,200,300)

# for n in  my_tuple
#     print(n)

# for n in my_tuple[::-1]:
#    print(n)

# for n in my_tuple:
#    if n == 200:
#        break
#    print(n)

for idx in range(5, 20, 2):
    res = idx + 1
    print(res)
