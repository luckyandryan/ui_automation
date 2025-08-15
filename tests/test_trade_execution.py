from pages.login_page import LoginPage
from pages.order_page import OrderPage
from pages.trade_now_page import TradeNowPage
from utils.assertions import AssertionHelper
import yfinance as yf

assertion = AssertionHelper()


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("luckyandryan27@gmail.com", "wrongpassword")
    login_page.check_login_failed()
    assertion.assert_equal(login_page.check_login_failed().is_displayed(), True)


def test_order_execution_with_valid_login(driver):
    # Do a valid login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("luckyandryan27@gmail.com", "@Mifxaccount25")

    # Navigate to Trade Now page
    trade_now_page = TradeNowPage(driver)
    trade_now_page.click_buy()
    trade_now_page.increase_lot(4)
    lot_value = trade_now_page.get_lot_value()
    assertion.assert_equal(lot_value, "0.5")

    trade_now_page.toggle_pending_order()
    trade_now_page.set_entry_price("1000")
    trade_now_page.do_order()

    # Verify order execution
    order_page = OrderPage(driver)
    entry_price = order_page.get_entry_price()
    lot_ordered = order_page.get_lot_ordered(lot_value)
    assertion.assert_equal(entry_price, "1000")
    assertion.assert_equal(lot_ordered, f"Buy {lot_value} Lot")


def test_get_nvda_price():
    nvda = yf.Ticker("NVDA")
    price = nvda.history(period="1d")["Close"].iloc[-1]

    print(f"NVDA Last Closing Price: {price}")
    assertion.assert_data_type(price, (float, int))
    assertion.assert_equal(price > 0, True)
