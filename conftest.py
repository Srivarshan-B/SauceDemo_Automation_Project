import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader

@pytest.fixture
def setup():
    config = ConfigReader()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(config.get("base_url"))
    driver.maximize_window()

    yield driver

    driver.quit()