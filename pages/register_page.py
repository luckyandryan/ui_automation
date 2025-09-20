from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    MOBILE_PHONE_INPUT = (By.ID, "mobilePhone")
    EMAIL_INPUT = (By.ID, "email")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    TERMS_CHECKBOX = (By.ID, "terms-and-condition")
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[@data-button-name='register-new']",
    )
    KODE_OTP_TERKIRIM_HEADER = (By.XPATH, "//h1[contains(text(),'Pilih Metode Verifikasi')]")

    def open(self):
        self.driver.get("https://www.cermati.com/app/gabung")
        self.driver.maximize_window()

    def enter_mobile_phone(self, phone_number):
        self.type(self.MOBILE_PHONE_INPUT, phone_number)

    def enter_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def enter_first_name(self, first_name):
        self.type(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.type(self.LAST_NAME_INPUT, last_name)

    def agree_to_terms(self):
        self.click(self.TERMS_CHECKBOX)

    def click_register(self):
        self.click(self.REGISTER_BUTTON)

    def is_register_button_enabled(self):
        return self.wait_for_element(self.REGISTER_BUTTON).is_enabled()

    def check_otp_header(self):
        return self.wait_for_element(self.KODE_OTP_TERKIRIM_HEADER)