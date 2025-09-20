from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class HomePage(BasePage):
    MAIN_TITLE = (By.XPATH, "//h2[text()='Kartu kredit yang kamu suka']")
    HONEST_POINT_TEXT = (By.XPATH, "//div[contains(@class, 'text-block-6') and normalize-space()='Honest Poin']")
    INTRODUCTION_TITLE = (By.XPATH, "//h2[normalize-space()='Apa itu Honest Card?']")
    PROMO_NAV_TITLE = (By.XPATH, "//div[@class='nav_links_text u-weight-bold' and text()='Promo']")
    HOTEL_AND_FLIGHT_OPTION = (By.XPATH, "//div[@class='nav_dropdown_text u-weight-bold' and normalize-space()='Hotel & Pesawat']")
    HOTEL_AND_FLIGHT_TITLE = (By.XPATH, "//h1[normalize-space()='Hotel & Pesawat']")
    PROMO_LINK = (By.XPATH, "//a[@href='/promos/gratis-satu-malam-di-wyndham-hotels-resorts']")
    PROMO_IMAGE = (By.XPATH, "//img[@alt='Gratis satu malam di Wyndham Hotels & Resorts']")

    def open(self):
        self.driver.get("https://www.honest.co.id/")
        self.driver.maximize_window()
    
    def check_main_title(self):
        return self.wait_for_element(self.MAIN_TITLE)
    
    def check_honest_point_text(self):
        return self.wait_for_element(self.HONEST_POINT_TEXT)

    def check_introduction_title_text(self):
        return self.wait_for_element(self.INTRODUCTION_TITLE)

    def click_promo_nav(self):
        return self.click(self.PROMO_NAV_TITLE)

    def hover_over_promo_nav(self):
        promo_nav = self.wait_for_element(self.PROMO_NAV_TITLE)
        ActionChains(self.driver).move_to_element(promo_nav).pause(2).perform()

    def click_hotel_and_flight_option(self):
        return self.click(self.HOTEL_AND_FLIGHT_OPTION)

    def check_hotel_and_flight_title(self):
        return self.wait_for_element(self.HOTEL_AND_FLIGHT_TITLE)
    
    def click_promo_link(self):
        return self.click(self.PROMO_LINK)
    
    def check_promo_image(self):
        return self.wait_for_element(self.PROMO_IMAGE)
