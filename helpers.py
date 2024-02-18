from faker import Faker
import secrets
import string

class UserDataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_name(self):
        return self.fake.name()

    def generate_empty_name(self):
        return ""

    def generate_email(self):
        return self.fake.email()



class PasswordGenerator:
    @staticmethod
    def generate_password():
        length = secrets.randbelow(5) + 6

        password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
        return password

    @staticmethod
    def generate_wrong_password():
        length = secrets.randbelow(5)

        password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
        return password


# Пример использования классов
user_data_generator = UserDataGenerator()
name = user_data_generator.generate_name()
empty_name = user_data_generator.generate_empty_name()
email = user_data_generator.generate_email()



print("Имя пользователя:", name)
print("Не корректное имя пользователя:", empty_name)
print("Email пользователя:", email)

password = PasswordGenerator.generate_password()
print("Сгенерированный пароль:", password)

wrong_password = PasswordGenerator.generate_wrong_password()
print("Сгенерированный пароль:", wrong_password)
