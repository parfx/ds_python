
# Функции

# Функция - "Фабрики", которая на вход принимают какие-либо данные и на выход возвращают другие данные

# 1 вариант.  Функция, которая на вход ничего не принимает и на выход ничего не возвращает

def func_1():
    print("hello world")

def func_2():
    name = "Parf"
    print(f"hello {name}!")


# 2 вариант. функция, которая принимает данные (имеет вход(-ы)), но ничего не возвращает

def func_3(argument_1, arg_2):
    result = argument_1 + arg_2
    print(result)

# вызов функции с передачей параметров 
# func_3(100, 55)


#2.1 вариант. Функции, принимающая данные, но ничего не возвращает
# аргументы имеют значения по умолчанию

def func_4(arg_1, arg_2, arg_3=10):
    result = arg_1 + arg_2 * arg_3
    print(result)

# func_4(100, 20, 2 )
#2.2 вариант. Функции, принимающая данные, но ничего не возвращает
# позиционные параметры

def func_5(arg_1=10, arg_2=20, arg_3=30):
    result = arg_1 + arg_2 + arg_3
    print(result)

# func_5(2, 3, 4)
# func_5(100, 20)

#2.3 вариант. Функции, принимающая данные, но ничего не возвращает
# именованные параметры

def func_6(arg_1=10, arg_2=20, arg_3=30):
    result = arg_1 + arg_2 + arg_3
    print(result)

# func_6(arg_3=100, arg_1=5)

#2.4 вариант. Функции, принимающая данные, но ничего не возвращает
# Множественные позиционные параметры 

def func_7(*args):
    """
    docstring
    """
    print(args)


# можно передавать произвольное количество позиционных параметров
# они будут упакованы в виде кортежа
# func_7(10, 27, 30)

def func_8(*args):
    """
    функция, которая складывает произвольное количество параметров
    """
    result = 0
    for num in args:
        result += num
    print(result)

# func_8(100)

#2.5 вариант. Функция, принимающая данные, но ничего не возвращает
# Множественные именованные параметры 

import math

def distance_calculate(**args):
    """
    функция, которая вычисляет дистанцию от начала координат (0,0,0) до точки с координатами (x,y,z)
    """
    keys = list(args.keys())

    # для вычисления дистанции применяем теорему Пифагора
    summa = 0

    # извлекаем все ключи из списка ключей
    for axis in keys:
        # суммирование квадратов катетов (значение координатных осей)
        summa += args[axis] **2

    # извлечение квадратного корня
    distance = math.sqrt(summa)

    print(f"Дистанция: {distance}")

# вызов функции
distance_calculate(x=10,y=20, z=10, a=5)      