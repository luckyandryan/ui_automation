from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "LiveTmp_password")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit' and @value='LOG IN']")
    LOGIN_FAILED_INDICATOR = (
        By.XPATH,
        "//div[contains(., 'Akun atau kata sandi salah')]",
    )

    def open(self):
        self.driver.get("https://mifx.com/clientarea/trade-now")
        self.driver.maximize_window()

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def check_login_failed(self):
        return self.wait_for_element(self.LOGIN_FAILED_INDICATOR)
