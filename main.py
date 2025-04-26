from datetime import datetime
from password_generation import PasswordGenerator as Passgen

def main():
    print("VERY COOL PASSWORD GENERATOR")

    try:
        num_passwords = int(input("Колко пароли да генерира?\n"))
        length = int(input("Колко дълги да са паролите:\n"))
        if num_passwords <= 0 or length <= 0:
            raise ValueError("Не можеш да генерираш такава парола, положителни числа pls.")
    except ValueError as error:
        print("Грешка:", error)
        return

    use_letters = input("Паролата да включва букви? (y/n):\n").lower() == 'y'
    use_digits = input("Да включва ли цифри? (y/n):\n").lower() == 'y'
    use_symbols = input("Да включва нормалните специални символи? (y/n):\n").lower() == 'y'
    use_special = input("Да включва HTML специални символи (като ☺)? (y/n):\n").lower() == 'y'
    use_space = input("Включва празно място? (y/n)\n").lower() == 'y'
    add_note = input("Искаш ли да има бележка към паролите? (y/n)\n").lower() == 'y'
    generator = Passgen(use_letters, use_digits, use_symbols, use_special, use_space)

    passwords = []

    for i in range(num_passwords):
        try:
            password = generator.generate_password(length)
            passwords.append(password)
            print(f"Парола {i + 1}: {password}")
        except ValueError as e:
            print("Излезе проблем:", e)
            return

    try:
        with open("passwords.txt", "a", encoding="utf-8") as file:
            file.write("Нови пароли от " + datetime.now().strftime("%d.%m.%Y %H:%M:%S\n"))
            if(add_note):
                file.write(input("Какво да се запише като бешежка към паролите?:\n"))
            for pwd in passwords:
                file.write(pwd + "\n")
        print("Паролите са записани във файла 'passwords.txt'")
    except Exception as e:
        print("Проблем при записването:", e)
main()
