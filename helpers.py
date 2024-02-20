from faker import Faker
import secrets
import string

class UserDataGenerator:
    fake = Faker()

    @staticmethod
    def generate_name():
        return UserDataGenerator.fake.name()

    @staticmethod
    def generate_empty_name():
        return ""

    @staticmethod
    def generate_email():
        return UserDataGenerator.fake.email()



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
# user_data_generator = UserDataGenerator()
# name = user_data_generator.generate_name()
# empty_name = user_data_generator.generate_empty_name()
# email = user_data_generator.generate_email()
# password = PasswordGenerator.generate_password()
# wrong_password = PasswordGenerator.generate_wrong_password()