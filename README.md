# Sprint_5
yandex_py_sprint_5

## Для запуска проетка требуется:

##### установить зависимости - pip install -r requirements.txt

##### запустить все тесты - pytest -v .\tests

# **Что есть что**

#### Тесты: '/tests'
#### 'conftest.py': фикстуры
#### 'locators.py': локаторы
#### 'data.py': креды тестового пользователя и креды генерируемого пользователя (при необходимости)
#### 'helpers.py': Здесь мы генерируем тестовые имена, почтовые адреса и пароли.


===========
# Проверки:
### **Регистрация:**
#### Успешная регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен.
#### Минимальный пароль — шесть символов.Ошибку для некорректного пароля.
### **Вход:**
#### вход по кнопке «Войти в аккаунт» на главной.
#### вход через кнопку «Личный кабинет».
#### вход через кнопку в форме регистрации.
#### вход через кнопку в форме восстановления пароля.
### **Переходы:**
#### Переход в личный кабинет.
#### Проверь переход по клику на «Личный кабинет».
#### Переход из личного кабинета в конструктор.
#### Переход по клику на «Конструктор» и на логотип Stellar Burgers.
### **Выход:**
#### Выход по кнопке «Выйти» в личном кабинете.
### **Раздел «Конструктор»:**
#### Работает переходы к разделам:«Начинки».
#### Работает переходы к разделам:«Соусы».
#### Работает переходы к разделам:«Булки».


## Написанные тесты:

#### **TestRegistration**

- test_registration_with_correct_user
- test_registration_with_empty_username
- test_registration_with_invalid_password

#### **TestLoginTheSite**

- test_login_to_account_with_button_on_the_main_page
- test_login_through_personal_account_button
- test_registration_with_correct_user
- test_login_from_recovery_form

#### **TestMovingToPersonalAccount**

- test_click_on_personal_account

#### **TestMovingFromAccountToLogo**

- test_transition_from_personal_account_to_logo_stellar_burgers

#### **TestExit**

- test_exit_from_personal_account

#### **TestMovingToConstructor** 

- test_moving_to_constructor_fillings
- test_moving_to_constructor_sauces
- test_moving_to_constructor_rolls
