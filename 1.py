def is_password_good(password):
    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        return False

    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False

    return True

password = input("Введите пароль: ")
result = is_password_good(password)

if result:
    print("Пароль надежный!")
else:
    print("Пароль небезопасный.")
