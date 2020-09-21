# Условные операторы 

a = 3

if a == 5:
    c = "Равно 5"
elif a == 4:                    
    c = "Равно 4" 
elif a == 3:                    
    c = "Равно 3" 
elif a == 2:                    
    c = "Равно 2"        
else: 
    c = "Ничему не равно "


b = 5

if b < 10 and b > 0:
    c = " 0 < b < 0 "
# elif b > 0:
# c = " > 0 "
else:
    c = " b не меньше 10 и не больше 0 "


x = True

# if not x:
#    print("Foo")
# else:
#   print("Bar")    


# * * * * Простой калькулятор * * * * 

a = int(input("Введите первое число  "))
b = int(input("Введите первое число  "))

operation = input("Введите символ операции (+, -, *, / ): ")

if operation == "+":
    res = a + b
elif operation == "-":
    res = a - b
elif operation == "*":
    res = a * b    
elif operation == "/":
    res = a / b        
elif operation == "^":
    res = a ** b       
else:
    res = "Символ операции не корректный!!!"

print(f"Результат {res}")