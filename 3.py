def divide(a, b):
    try:
        result = a / b
        return f"Результат деления: {result}"

    except ZeroDivisionError:
        return "Деление на ноль невозможно"

    finally:
        print("Блок выполняется всегда")

a = 10
b = 2
result = divide(a, b)
print(result)

a = 10
b = 0
result = divide(a, b)
print(result)



