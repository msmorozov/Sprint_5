import data
import helpers
import locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestRegistration:
    def test_registration_with_test_login(self, driver):
        #переход на "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        #нажатие на конпку зарегистрироваться
        driver.find_element(*locators.TestLocators.REGISTRATION_BUTTON).click()

        #заполнение обязательных полей
        driver.find_element(*locators.TestLocators.REGISTRATION_NAME_FIELD).send_keys(data.user_name)
        driver.find_element(*locators.TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(data.mail)
        driver.find_element(*locators.TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(data.password)
        #регистрация
        driver.find_element(*locators.TestLocators.REGISTRATION_NEW_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        #вносим данные ранее зарегистрированного пользователя
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.mail)
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.password)
        #логинимся
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        #вход в ЛК
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        assert driver.find_element(*locators.TestLocators.NAME_SPACE).get_attribute('value') == data.user_name, (
            "Имя пользователя при регистрации не равно имени пользователя в ЛК после входа, но получен {}")


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

        name_spase = driver.find_element(*locators.TestLocators.REGISTRATION_NAME_FIELD).get_attribute('value')
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register' and name_spase == '', \
            "Удалось зарегистрироваться с пустым именем"

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

        assert driver.find_element(*locators.TestLocators.INVALID_PASSWORD_MESSAGE).is_displayed(), \
            "Сообщение об ошибке 'Некорректный пароль', не отображается"