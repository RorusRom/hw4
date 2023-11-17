import random

class UserEncryptor:
    def __init__(self, number):
        self._user_input = number
        self._encrypt()

    def _encrypt(self):
        operation = random.randint(1, 2)

        if operation == 1:
            self._user_input += random.randint(1, 10)
        elif operation == 2:
            self._user_input *= random.randint(1, 5)

    def __str__(self):
        return str(self._user_input)

user_number = int(input("Введите число: "))
user_encryptor = UserEncryptor(user_number)

print("Введенное число:", user_number)
print("Зашифрованное число:", user_encryptor)
