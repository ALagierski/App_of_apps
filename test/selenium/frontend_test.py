import pytest
from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

APPLICATION_URL = environ.get('APPLICATION_URL', 'http://192.168.44.44:5000/')
SELENIUM_URL = environ.get('SELENIUM_URL', 'http://192.168.44.44:4444/wd/hub')

class TestFrontendApp:

    @pytest.fixture
    def driver(self) -> webdriver.Firefox:
        return webdriver.Firefox()

    def test_our_app(self, driver: webdriver.Firefox):
        driver.set_page_load_timeout(5)
        driver.set_script_timeout(5)
        driver.get(APPLICATION_URL)
        name = driver.find_element(By.NAME, "name")
        name.send_keys("Aurora")
        animal = driver.find_element(By.NAME, "animal")
        animal.send_keys("Cat")
        animal.send_keys(Keys.ENTER)
        assert "No results found" not in driver.page_source
        driver.quit()
