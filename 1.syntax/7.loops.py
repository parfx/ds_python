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

# for idx in range(5, 20, 2):
#    res = idx + 1
#    print(res)


# генераторы списков

# создание списка с числами в диапозоне от 0 до 9
# my_list = [num for num in range(10)]

# создание списка с числами в диапозоне от 50 до 90 c шагом 10
# my_list = [num for num in range(50 , 100 , 10)]

# создание списка с числами в диапозоне от 0 до 9 возведенье в степень 2 
# my_list = [num ** 2 for num in range(10)]

# cоздание списка с числами в диапозоне от 0 до 9 , которые больше 5
# my_list = [num ** 2 for num in range(10) if num > 5 ] 

# генератор словаря 

# создание словаря из списка символов
# my_dict = {symbol : symbol for symbol in ["a","b","c"]}

# создание словаря из списка символов
list_1 = [('b', 10), ('a', 20), ('c', 30)]

# my_dict = {key : val for key, val in list_1}


# практическое использование циклов 

# калькулятор

commands = {"stop", "+","-","*","/"}

while True:

    # ввод чисел
    num_list = []
    for i in range(2):
        num = int(input(f"Введите {i+1} число: "))
        num_list.append(num)

    # ввод команды
    cmd = None
    while True:
        cmd = input("Введите команду: ")
        if cmd not in commands:
            print("Вы ввели неправильную команду!!!")
            continue
        else:
            break
        
         

    # вычисление

    if cmd == 'stop':
        print("До свидание!!!")
        break
    elif cmd == "+":
        res = num_list[0] + num_list[1]
    elif cmd == "-":
        res = num_list[0] - num_list[1]
    elif cmd == "*":
        res = num_list[0] * num_list[1]
    elif cmd == "/":
        res = num_list[0] / num_list[1]             
    
    # вывод результата  
    print(f"Результат: {res}")   






