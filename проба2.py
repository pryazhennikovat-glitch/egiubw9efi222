def calculator():
    print("Простой калькулятор")
    print("Операции: +, -, *, /")
    
    try:
        a = float(input("Введите первое число: "))
        op = input("Введите операцию: ")
        b = float(input("Введите второе число: "))
        
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                return "Ошибка: деление на ноль!"
            result = a / b
        else:
            return "Неизвестная операция"
        
        return f"Результат: {result}"
    except ValueError:
        return "Ошибка: введите корректные числа"

print(calculator())
