from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TradeNowPage(BasePage):
    BUY_BUTTON = (By.XPATH, "//div[@id='direction-buy']")
    SELL_BUTTON = (By.XPATH, "//div[@id='direction-sell']")
    INCREASE_LOT_BUTTON = (By.XPATH, "//div[@id='i_defStepVal']")
    LOT_INPUT = (By.ID, "qty")
    ORDER_BUTTON = (By.XPATH, "//button[@name='btnSubmit' and @value='order']")
    PENDING_ORDER_TOGGLE = (
        By.XPATH,
        "//input[@id='isPending']/following-sibling::span[@class='slider round']",
    )
    ENTRY_PRICE_INPUT = (By.XPATH, "//input[@id='price_limit']")

    def click_buy(self):
        self.click(self.BUY_BUTTON)

    def click_sell(self):
        self.click(self.SELL_BUTTON)

    def increase_lot(self, times=1):
        for _ in range(times):
            self.click(self.INCREASE_LOT_BUTTON)

    def get_lot_value(self):
        return self.wait_for_element(self.LOT_INPUT).get_attribute("value")

    def do_order(self):
        self.click(self.ORDER_BUTTON)

    def toggle_pending_order(self):
        self.click(self.PENDING_ORDER_TOGGLE)

    def set_entry_price(self, price):
        self.type(self.ENTRY_PRICE_INPUT, price)

    def get_entry_price(self):
        return self.wait_for_element(self.ENTRY_PRICE_INPUT).get_attribute("value")
