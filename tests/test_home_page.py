import os
from pages.home_page import HomePage
from utils.assertions import AssertionHelper


assertion = AssertionHelper()


def test_verify_homepage(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.check_main_title()
    assertion.assert_equal(home_page.check_honest_point_text().is_displayed(), True)
    assertion.assert_equal(
        actual=home_page.check_main_title().text.strip(),
        expected="Kartu kredit yang kamu suka"
    )

    home_page.check_honest_point_text()
    assertion.assert_equal(home_page.check_introduction_title_text().is_displayed(), True)
    assertion.assert_equal(
        actual=home_page.check_honest_point_text().text.strip(),
        expected="Honest Poin"
    )

    home_page.check_introduction_title_text()
    assertion.assert_equal(home_page.check_main_title().is_displayed(), True)
    assertion.assert_equal(
        actual=home_page.check_introduction_title_text().text.strip(),
        expected="Apa itu Honest Card?"
    )

    home_page.click_promo_nav()
    home_page.hover_over_promo_nav()
    home_page.click_hotel_and_flight_option()
    assertion.assert_current_url("https://www.honest.co.id/promo/hotel-tiket-pesawat-kartu-kredit")

    home_page.check_hotel_and_flight_title()
    assertion.assert_equal(home_page.check_hotel_and_flight_title().is_displayed(), True)
    assertion.assert_equal(
        actual=home_page.check_hotel_and_flight_title().text.strip(),
        expected="Hotel & Pesawat"
    )

    home_page.click_promo_link()
    assertion.assert_current_url("https://www.honest.co.id/promos/gratis-satu-malam-di-wyndham-hotels-resorts")
    home_page.check_promo_image()
    assertion.assert_equal(home_page.check_promo_image().is_displayed(), True)
    assertion.assert_equal(
        actual=home_page.check_promo_image().get_attribute("alt"),
        expected="Gratis satu malam di Wyndham Hotels & Resorts"
    )