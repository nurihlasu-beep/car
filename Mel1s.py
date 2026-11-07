print("=== КАЛЬКУЛЯТОР ===")

num1 = float(input("Введите первое число: "))
operator = input("Введите действие (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operator == "+":
    print("Ответ:", num1 + num2)

elif operator == "-":
    print("Ответ:", num1 - num2)

elif operator == "*":
    print("Ответ:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Ответ:", num1 / num2)
    else:
        print("Ошибка! На ноль делить нельзя.")

else:
    print("Неизвестная операция!")