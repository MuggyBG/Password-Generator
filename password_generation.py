import random
import string

class PasswordGenerator:
    def __init__(self, use_letters=True, use_digits=True, use_symbols=True, use_special=False, use_space=False):
        self.use_letters = use_letters
        self.use_digits = use_digits
        self.use_symbols = use_symbols
        self.use_special = use_special
        self.use_space = use_space
        self.char_list = self.get_characters()

    def get_special(self):
        special_characters = []
        for number in range(1, 256):
            char = chr(number)
            if char.isprintable():
                special_characters.append(char)
        for number in range(9786, 10041):
            char = chr(number)
            if char.isprintable():
                special_characters.append(char)
        return special_characters

    def get_characters(self):
        char_list = []
        if self.use_letters:
            char_list.append(string.ascii_letters)
        if self.use_digits:
            char_list.append(string.digits)
        if self.use_symbols:
            char_list.append(string.punctuation)
        if self.use_space:
            char_list.append(" ")
        if self.use_special:
            char_list.append(''.join(self.get_special()))
        return char_list

    def generate_password(self, length):
        if not self.char_list:
            raise ValueError("Не е избран нито един тип символи.")
        all_chars = ''.join(self.char_list)
        return ''.join(random.choice(all_chars) for _ in range(length))
