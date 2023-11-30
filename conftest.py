from dataclasses import dataclass, field
from enum import Enum
from typing import Union

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class PageLoadStrategy(Enum):
    """
    More info about page load strategies:
    https://www.lambdatest.com/blog/selenium-page-load-strategy/
    https://www.selenium.dev/documentation/webdriver/drivers/options/
    """
    NONE = "none"
    NORMAL = "normal"
    EAGER = "eager"


@dataclass
class Config:
    headless: bool = None
    browser: str = None
    cookie_enabled: bool = None
    options: Union[ChromeOptions] = None


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--headless", action="store_true")
    parser.addoption("--no-cookies", action="store_true")
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="session")
def config(request: pytest.FixtureRequest):
    """
    Additional information on '--no-sandbox' and '--disable-shm-usage'
    arguments:
    https://petertc.medium.com/pro-tips-for-selenium-setup-1855a11f88f8
    https://www.google.com/googlebooks/chrome/med_26.html
    """
    config = Config()
    config.headless = request.config.getoption("--headless")
    config.browser = request.config.getoption("--browser")
    config.cookie_enabled = not request.config.getoption("--no-cookies")

    if config.browser.lower() == "chrome":
        options = ChromeOptions()
        # Install ad block extension
        options.add_extension(
            "external_files/extensions/uBlock0_1.52.0.chromium.zip"
        )
        if not config.cookie_enabled:
            options.add_experimental_option(
                "prefs",
                {"profile.default_content_setting_values.cookies": 2}
            )
    else:
        raise ValueError(f"Browser {config.browser} is not supported.")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.set_capability("pageLoadStrategy", PageLoadStrategy.NORMAL.value)

    if config.headless:
        options.add_argument("-headless")

    config.options = options
    return config


@pytest.fixture(scope="function")
def driver(config):
    driver = None
    executable_path = ChromeDriverManager().install()
    # executable_path = "external_files/drivers/chromedriver_119.exe"

    if config.browser == "chrome":
        driver = webdriver.Chrome(
            options=config.options, service=ChromeService(executable_path)
        )
    yield driver
    driver.quit()
