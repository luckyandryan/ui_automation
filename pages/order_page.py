from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):
    ENTRY_PRICE_TEXT = (By.XPATH, "//span[@id='i_harga_entry_2_value']")
    LOT_ORDERED_TEXT = "//div[normalize-space(.)='Buy {} Lot']"

    def get_entry_price(self):
        self.driver.refresh()
        entry_price = (
            self.wait_for_element(self.ENTRY_PRICE_TEXT)
            .text.replace(",", "")
            .replace(".00", "")
        )
        return entry_price

    def get_lot_ordered(self, lot_value):
        locator = (By.XPATH, self.LOT_ORDERED_TEXT.format(lot_value))
        lot_ordered = self.wait_for_element(locator).text
        return lot_ordered
