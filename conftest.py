import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture()
def browser():
    options = Options()
    options.page_load_strategy="eager"
    service = Service()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    #options.add_argument('--headless')
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    yield browser
    browser.close()
