from appium import webdriver
from page_model import PageModel

# change to real path to apk
PATH_TO_APK = "app-debug.apk"

desired_caps = {
    "platformName":"Android",
    "platformVersion":"8",
    "deviceName":"pixel3",
    "app":PATH_TO_APK,
}

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

page_model = PageModel(driver)

def test_addition_smoke():
    page_model.addition("3", "2")
    assert page_model.get_result_field_text() == "3.00 + 2.00 = 5.00"

def test_substract_smoke():
    page_model.substract("3", "2")
    assert page_model.get_result_field_text() == "3.00 - 2.00 = 1.00"

def test_multiplication_smoke():
    page_model.multiplication("3", "2")
    assert page_model.get_result_field_text() == "3.00 * 2.00 = 6.00"

def test_division_smoke():
    page_model.division("3", "2")
    assert page_model.get_result_field_text() == "3.00 / 2.00 = 1.50"

