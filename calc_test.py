from PageModel import PageModel

# change to real path to apk
PATH_TO_APK = "app-debug.apk"

desired_caps = {
    "platformName":"Android",
    "platformVersion":"8",
    "deviceName":"pixel3",
    "app":PATH_TO_APK,
}

page_model = PageModel(desired_caps, "http://0.0.0.0:4723/wd/hub")

def addition(left, right):
    page_model.reset()
    page_model.set_left_input(left)
    page_model.set_right_input(right)
    page_model.click_addition()

def substract(left, right):
    page_model.reset()
    page_model.set_left_input(left)
    page_model.set_right_input(right)
    page_model.click_substract()

def multiplication(left, right):
    page_model.reset()
    page_model.set_left_input(left)
    page_model.set_right_input(right)
    page_model.click_multiplication()

def division(left, right):
    page_model.reset()
    page_model.set_left_input(left)
    page_model.set_right_input(right)
    page_model.click_division()

def test_addition_smoke():
    addition("3", "2")
    assert page_model.get_result_field_text() == "3.00 + 2.00 = 5.00"

def test_substract_smoke():
    substract("3", "2")
    assert page_model.get_result_field_text() == "3.00 - 2.00 = 1.00"

def test_multiplication_smoke():
    multiplication("3", "2")
    assert page_model.get_result_field_text() == "3.00 * 2.00 = 6.00"

def test_division_smoke():
    division("3", "2")
    assert page_model.get_result_field_text() == "3.00 / 2.00 = 1.50"


