# UI Automation Test

Automated **UI testing** for [MIFX](https://mifx.com) using **Python**, **Pytest**, and **Selenium WebDriver**.  
Also includes an integration with [Yahoo Finance](https://finance.yahoo.com/quote/NVDA/?guccounter=1) to fetch the latest **NVDA** stock price.

---

## 🤖 Tech Stack
```
Python 3.8+
Pytest – Test framework
Selenium – Browser automation
WebDriver Manager – Automatic ChromeDriver installation
yfinance – Yahoo Finance data fetching
```

---

## 🔧 Setup

1. 📥 **Clone the Repository**  
    ```bash
    git clone https://github.com/luckyandryan/ui_automation.git
    ```

2. ➡️ **Move to the project directory**  
    ```bash
    cd mifx_automation
    ```

3. 🐍 **Install Python** *(if not already installed)*  
    Download and install Python 3.8+ from the [official Python website](https://www.python.org/downloads/).  
    *After installation, confirm with:*
    ```bash
    python --version
    ```

4. 🔧 **Install Dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` is missing, install manually:
    ```bash
    pip install selenium pytest webdriver-manager yfinance python-dotenv
    ```
---


## 🚀 Run Tests

To execute the test, run command below:
```
source tests/execute_test.sh
```

---

## 📁 Project Structure
```
ui_automation/
├── pages/
│   ├── base_page.py              # Base methods for all page objects
│   ├── login_page.py             # Login page locators & actions
│   ├── order_page.py             # Order verification locators & actions
│   └── trade_now_page.py         # Trade locators & actions
├── tests/
│   ├── conftest.py               # Pytest fixtures for WebDriver setup
│   ├── execute_test.sh           # Shell script to execute tests
│   ├── pytest.ini                # Pytest config for logger
│   └── test_trade_execution.py   # Main UI test cases + NVDA price check
├── README.md
└── requirements.txt              # Dependencies

```
