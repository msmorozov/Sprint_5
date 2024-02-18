import data
import helpers
import locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
