import os
from pages.register_page import RegistrationPage
from utils.assertions import AssertionHelper

assertion = AssertionHelper()

def test_registration_form_with_valid_data(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()

    # Fill in the registration form
    registration_page.enter_mobile_phone("081287451105")
    registration_page.enter_email("test@example.com")
    registration_page.enter_first_name("John")
    registration_page.enter_last_name("Doe")
    assertion.assert_equal(registration_page.is_register_button_enabled(), True)
    registration_page.click_register()
    assertion.assert_equal(
        actual=registration_page.check_otp_header().text.strip(),
        expected="Pilih Metode Verifikasi",
    )
    assertion.assert_current_url(
        driver, "https://www.cermati.com/app/verification-methods"
    )


def test_registration_form_with_invalid_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()

    # Fill in the registration form with an invalid email
    registration_page.enter_mobile_phone("081287451105")
    registration_page.enter_email("invalid-email")
    registration_page.enter_first_name("John")
    registration_page.enter_last_name("Doe")
    assertion.assert_equal(registration_page.is_register_button_enabled(), False)


def test_registration_form_with_invalid_phone(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()

    # Fill in the registration form with an invalid phone number
    registration_page.enter_mobile_phone("123")
    registration_page.enter_email("test@example.com")
    registration_page.enter_first_name("John")
    registration_page.enter_last_name("Doe")
    assertion.assert_equal(registration_page.is_register_button_enabled(), False)
