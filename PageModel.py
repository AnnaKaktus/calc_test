from appium import webdriver

class PageModel:
    def __init__(self, desired_caps, path):
        self.driver = webdriver.Remote(path, desired_caps)
        self.locators = dict(
            input_field_left = self.driver.find_element(value="com.vbanthia.androidsampleapp:id/inputFieldLeft"),
            input_field_right = self.driver.find_element(value="com.vbanthia.androidsampleapp:id/inputFieldRight"),
            result_text_view = self.driver.find_element(value="com.vbanthia.androidsampleapp:id/resultTextView"),
            reset_button = self.driver.find_element(value="com.vbanthia.androidsampleapp:id/resetButton"),
            addition_button = self.driver.find_element(value="com.vbanthia.androidsampleapp:id/additionButton"),
            substract_button = self.driver.find_element(value="com.vbanthia.androidsampleapp:id/subtractButton"),
            multiplication_button = self.driver.find_element(value="com.vbanthia.androidsampleapp:id/multiplicationButton"),
            division_button = self.driver.find_element(value="com.vbanthia.androidsampleapp:id/divisionButton"),
        )

    def __del__(self):
        if (self.driver != None):
            self.driver.quit()

    def set_left_input(self, keys):
        self.locators["input_field_left"].send_keys(keys)

    def set_right_input(self, keys):
        self.locators["input_field_right"].send_keys(keys)

    def get_result_field_text(self):
        return self.locators["result_text_view"].text

    def reset(self):
        self.locators["reset_button"].click()

    def click_addition(self):
        self.locators["addition_button"].click()

    def click_substract(self):
        self.locators["substract_button"].click()

    def click_multiplication(self):
        self.locators["multiplication_button"].click()

    def click_division(self):
        self.locators["division_button"].click()
