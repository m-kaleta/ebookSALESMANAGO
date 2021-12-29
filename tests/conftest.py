from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest
import time

@pytest.fixture()
def setup(request):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.salesmanago.pl")
    driver.maximize_window()
    time.sleep(1)
    request.cls.driver = driver
    yield
    driver.quit()
