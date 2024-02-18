import data
import helpers
import locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestRegistration:
    def test_registration_with_correct_user(self, driver):
        #переход на "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        #нажатие на конпку зарегистрироваться
        driver.find_element(*locators.TestLocators.REGISTRATION_BUTTON).click()
        #заполнение обязательных полей
        driver.find_element(*locators.TestLocators.REGISTRATION_NAME_FIELD).send_keys(helpers.user_data_generator.generate_name())
        driver.find_element(*locators.TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(helpers.user_data_generator.generate_email())
        driver.find_element(*locators.TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(helpers.PasswordGenerator.generate_password())
        #регистрация
        driver.find_element(*locators.TestLocators.REGISTRATION_NEW_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', (
            "Ожидался URL https://stellarburgers.nomoreparties.site/login, но получен {}".format(driver.current_url))
        print(" Проверка текущего URL после входа выполнена успешно")

        driver.quit()

    def test_registration_with_empty_username(self, driver):
        # переход на "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        # нажатие на конпку зарегистрироваться
        driver.find_element(*locators.TestLocators.REGISTRATION_BUTTON).click()
        # заполнение обязательных полей
        driver.find_element(*locators.TestLocators.REGISTRATION_NAME_FIELD).send_keys(helpers.user_data_generator.generate_empty_name())
        driver.find_element(*locators.TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(helpers.user_data_generator.generate_email())
        driver.find_element(*locators.TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(helpers.PasswordGenerator.generate_password())
        # регистрация
        driver.find_element(*locators.TestLocators.REGISTRATION_NEW_ACCOUNT_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register', (
                "Ожидался URL https://stellarburgers.nomoreparties.site/register, но получен {}".format(
                    driver.current_url))
        print(" Проверка поле «Имя» должно быть не пустым, выполнена успешно")

        driver.quit()

    def test_registration_with_invalid_password(self, driver):
        # переход на "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        # нажатие на конпку зарегистрироваться
        driver.find_element(*locators.TestLocators.REGISTRATION_BUTTON).click()
        # заполнение обязательных полей
        driver.find_element(*locators.TestLocators.REGISTRATION_NAME_FIELD).send_keys(helpers.user_data_generator.generate_name())
        driver.find_element(*locators.TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(helpers.user_data_generator.generate_email())
        driver.find_element(*locators.TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(helpers.PasswordGenerator.generate_wrong_password())
        # регистрация
        driver.find_element(*locators.TestLocators.REGISTRATION_NEW_ACCOUNT_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register', (
                "Ожидался URL https://stellarburgers.nomoreparties.site/register, но получен {}".format(
                    driver.current_url))
        print(" Проверка поле «Пароль» должно быть не менее 6-ти символов, выполнена успешно")

        driver.quit()

class TestLoginTheSite:
    def test_login_to_account_with_button_on_the_main_page(self, driver):
        # переход на "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        # вход зарегистрированным пользователем
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', (
                "Ожидался URL https://stellarburgers.nomoreparties.site/, но получен {}".format(
                    driver.current_url))
        print(" Проверка входа в аккаунт с центральной страницы, выполнена успешно")

        driver.quit()

    def test_login_through_personal_account_button(self, driver):
        #нажатие на ЛК
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        # вход зарегистрированным пользователем
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', (
                "Ожидался URL https://stellarburgers.nomoreparties.site/, но получен {}".format(
                    driver.current_url))
        print(" Проверка входа в аккаунт через Личный Кабинет центральной страницы, выполнена успешно")

        driver.quit()

    def test_registration_with_correct_user(self, driver):
        # переход на "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        # нажатие на конпку зарегистрироваться
        driver.find_element(*locators.TestLocators.REGISTRATION_BUTTON).click()
        # переход на "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()
        # вход зарегистрированным пользователем
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', (
            "Ожидался URL https://stellarburgers.nomoreparties.site/, но получен {}".format(
                driver.current_url))
        print(" Проверка входа в аккаунт через кнопку в форме регистрации, выполнена успешно")

        driver.quit()

    def test_login_from_recovery_form(self, driver):
        # переход на "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        # нажатие на конпку восстановить пароль
        driver.find_element(*locators.TestLocators.PASSWORD_RECOVERY_BUTTON).click()
        # нажатие на конпку "войти в аккаунт" с страницы восстановления пароля
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON_ON_PASSWORD_RECOVERY_PAGE).click()
        # вход зарегистрированным пользователем
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', (
            "Ожидался URL https://stellarburgers.nomoreparties.site/, но получен {}".format(
                driver.current_url))
        print(" Проверка входа через кнопку в форме восстановления пароля, выполнена успешно")

        driver.quit()

class TestMovingToPersonalAccount:
    def test_click_on_personal_account(self, driver):
        #вход на сайт
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        #введение кредов
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        #ожидание редиректа на основною страницу
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        #переход в ЛК
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        #ожидание редиректа на ЛК
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', (
                "Ожидался URL https://stellarburgers.nomoreparties.site/account/profile, но получен {}".format(
                    driver.current_url))
        print("Проверка перехода после авторизации в «Личный кабинет», выполнена успешно")

        driver.quit()

class TestMovingFromAccountToLogo:
    def test_transition_from_personal_account_to_logo_stellar_burgers(self, driver):
        #вход на сайт
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        #введение кредов
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        #ожидание редиректа на основною страницу
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        #переход в ЛК
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        #ожидание редиректа на ЛК
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        #клик на лого Stellar Burgers
        driver.find_element(*locators.TestLocators.STELLAR_BURGER_BUTTON).click()

        # ожидание перехода на гл.страницу
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        #выход из аккаунта
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', (
                "Ожидался URL https://stellarburgers.nomoreparties.site/, но получен {}".format(
                    driver.current_url))
        print("Проверка перехода по клику на логотип Stellar Burgers, выполнена успешно")

        driver.quit()

class TestExit:
    def test_exit_from_personal_account(self, driver):
        #вход на сайт
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        #введение кредов
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        #ожидание редиректа на основною страницу
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        #переход в ЛК
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        #ожидание редиректа на ЛК
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        #выход из аккаунта
        driver.find_element(*locators.TestLocators.LOGOUT_BUTTON).click()

        # ожидание выхода из ЛК
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        #выход из аккаунта
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', (
                "Ожидался URL https://stellarburgers.nomoreparties.site/login, но получен {}".format(
                    driver.current_url))
        print("Проверка выход по кнопке «Выйти» в «Личный кабинет», выполнена успешно")

        driver.quit()

class TestMovingToConstructor:
    def test_moving_to_constructor_fillings(self, driver):
        # Переход на конструктор начинок
        driver.find_element(*locators.TestLocators.FILLINGS_ELEMENT_CLICK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredient_ingredient__text__yp3dH")))

        assert driver.find_element(*locators.TestLocators.FILLINGS_ELEMENT).is_displayed(), \
            "Элемент начинок не найден на странице"

        print("Проверка перехода к разделам 'Начинки', выполнена успешно")

    def test_moving_to_constructor_sauces(self, driver):
        # Переход на конструктор соусов
        driver.find_element(*locators.TestLocators.SAUCES_ELEMENT_CLICK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'BurgerIngredient_ingredient__priceBox__LVbrB')))

        assert driver.find_element(*locators.TestLocators.SAUCES_ELEMENT).is_displayed(), \
            "Элемент соусов не найден на странице"

        print("Проверка перехода к разделам 'Соусы', выполнена успешно")

    def test_moving_to_constructor_rolls(self, driver):
        #объявление элемента
        element = driver.find_element(*locators.TestLocators.SAUCES_ELEMENT)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # Переход на конструктор булок
        driver.find_element(*locators.TestLocators.ROLLS_ELEMENT_CLICK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'BurgerIngredient_ingredient__text__yp3dH')))

        assert driver.find_element(*locators.TestLocators.ROLLS_ELEMENT).is_displayed(), \
            "Элемент булок не найден на странице"

        print("Проверка перехода к разделам 'Булки', выполнена успешно")