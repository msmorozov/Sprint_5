import helpers
user = [
    'morozovms',
    'morozovms@test.ru',
    'wxR7fpl'
]

user_name = helpers.user_data_generator.generate_name()
mail = helpers.user_data_generator.generate_email()
password = helpers.PasswordGenerator.generate_password()