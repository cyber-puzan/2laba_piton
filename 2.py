import math

def process_input(data):
    if isinstance(data, list):
        if all(isinstance(x, (int, float)) for x in data) and len(data) > 0:
            digit = 1
            for number in data:
                digit *= number
            geometric = math.pow(digit, 1 / len(data))
            return geometric
        else:
            return "Ошибка: список должен содержать числа."

    elif isinstance(data, dict):

        sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        return sorted_dict

    elif isinstance(data, int):

        if data > 1:
            for i in range(2, int(math.sqrt(data)) + 1):
                if (data % i) == 0:
                    return f"{data} не является простым числом."
            else:
                return f"{data} - простое число."
        else:
            return "Введите число больше 1."

    elif isinstance(data, str):

        words = data.split()
        word_count = len(words)
        longest_word = max(words, key=len)
        return f"Количество слов: {word_count}, Самое длинное слово: {longest_word}"

    else:
        return "Ошибка: неподдерживаемый тип данных."


input_list = [3, 4, 8]
result = process_input(input_list)
print(result)

input_dict = {'a': 5, 'b': 2, 'c': 8}
result = process_input(input_dict)
print(result)

input_number = 17
result = process_input(input_number)
print(result)

input_string = "Это пример строки "
result = process_input(input_string)
print(result)
