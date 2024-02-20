import data
import helpers
import locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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


    def test_registration_with_test_login(self, driver):
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
