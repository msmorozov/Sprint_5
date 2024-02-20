from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLocators:
    #кнопка входа в аккаунт
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(), "Войти в аккаунт")]')
    #кнопка регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    #сообщение о не корректном пароле
    INVALID_PASSWORD_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")

    #поле имя в ЛК пользователя
    NAME_SPACE = (By.NAME, "Name")

    #регистрация, поле имя
    REGISTRATION_NAME_FIELD = (By.XPATH, "//*[@id='root']//input")
    #регистрация, поле email
    REGISTRATION_EMAIL_FIELD = (By.XPATH, "//form//fieldset[2]//input")
    #регистрация, поле пароль
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    #кнопка регистрации после внесения кредов нового пользователя
    REGISTRATION_NEW_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

    #поле email при входе
    LOGIN_MAIL_FIELD = (By.XPATH, '//input[@type="text" and @name="name"]')
    #поле пароля при входе
    LOGIN_PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    #кнопка войти
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    #кнопка войти на странице регистрации
    LOGIN_BUTTON_ON_REGISTRATION_PAGE = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Войти"]')
    #кнопка войти на странице восстановления пароля
    LOGIN_BUTTON_ON_PASSWORD_RECOVERY_PAGE = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Войти"]')
    #поле в аккаунте с именем пользователя
    LOGIN_FIELD_IN_ACCOUNT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default input__textfield-disabled'][@name='Name']")

    #кнопка ЛК
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH,'//p[text()="Личный Кабинет"]')
    #кнопка восстановления пароля
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Восстановить пароль"]')
    #кнопка выхода
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    #иконка бургера
    STELLAR_BURGER_BUTTON = (By.CSS_SELECTOR, '#root > div > header > nav > div > a > svg')

    #выбор в конструкторе элемента соусы
    SAUCES_ELEMENT_CLICK = (By.XPATH, "// span[text() = 'Соусы']")
    #элемент набора соусов за который якоримся
    SAUCES_ELEMENT = (By.XPATH, '//h2[text()="Соусы"]')
    #элемент ожидания перед проверкой конструктора слусов
    SAUCES_ELEMENT_WAIT = (By.CLASS_NAME, 'BurgerIngredient_ingredient__priceBox__LVbrB')

    #выбор в конструкторе элемента начинки
    FILLINGS_ELEMENT_CLICK = (By.XPATH, "// span[text() = 'Начинки']")
    #элемент набора начинок за который якоримся
    FILLINGS_ELEMENT = (By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10"]')
    #элемент ожидания перед проверкой конструктора начинки
    FILLINGS_ELEMENT_WAIT = (By.CLASS_NAME, 'BurgerIngredient_ingredient__text__yp3dH')

    #выбор в конструкторе элемента булки
    ROLLS_ELEMENT_CLICK = (By.XPATH, "// span[text() = 'Булки']")
    #элемент набора булки за который якоримся
    ROLLS_ELEMENT = (By.XPATH, '//h2[text()="Булки"]')
    #элемент ожидания перед проверкой конструктора булки
    ROLLS_ELEMENT_WAIT = (By.CLASS_NAME, 'BurgerIngredient_ingredient__text__yp3dH')