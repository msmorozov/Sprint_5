import helpers
user = [
    'morozovms',
    'morozovms@test.ru',
    'wxR7fpl'
]

user_name = helpers.UserDataGenerator.generate_name()
mail = helpers.UserDataGenerator.generate_email()
password = helpers.PasswordGenerator.generate_password()