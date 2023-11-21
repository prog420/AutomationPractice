import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--headless", action="store_true")
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="session")
def config(request: pytest.FixtureRequest):
    """
    Additional information on '--no-sandbox' and '--disable-shm-usage'
    arguments:
    https://petertc.medium.com/pro-tips-for-selenium-setup-1855a11f88f8
    https://www.google.com/googlebooks/chrome/med_26.html
    """
    headless: bool = request.config.getoption("--headless")
    browser: str = request.config.getoption("--browser")

    options = None
    if browser.lower() == "chrome":
        options = ChromeOptions()
        # Install ad block extension
        options.add_extension("external_files/extensions/uBlock0_1.52.0.chromium.zip")
    else:
        raise ValueError(f"Browser {browser} is not supported.")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.set_capability("pageLoadStrategy", "normal")
    # options.set_capability("pageLoadStrategy", "eager")

    if headless:
        options.add_argument("-headless")

    return {"browser": browser, "headless": headless, "options": options}


@pytest.fixture(scope="function")
def driver(config):
    driver = None
    browser = config.get("browser")
    options = config.get("options")
    executable_path = ChromeDriverManager().install()
    # executable_path = "external_files/drivers/chromedriver_119.exe"

    if browser == "chrome":
        driver = webdriver.Chrome(
            options=options, service=ChromeService(executable_path)
        )
    yield driver
    driver.quit()
