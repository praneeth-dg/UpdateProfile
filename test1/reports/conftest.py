import pytest


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path="E:/Selenium/NaukriUpdate/drivers/chromedriver.exe")

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    print("Test Completed")
