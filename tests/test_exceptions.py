import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.fetch import disable


# This is pytest mark to execute marks
@pytest.mark.positive_exceptions
class TestExceptionCase01:
    def test_exception_case01(self, driver):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        homepage_title = driver.find_element(By.TAG_NAME, "h2")
        actual_homepage_title = homepage_title.text
        assert actual_homepage_title == "Test Exceptions"
        print("Validate header title")
        time.sleep(2)

        # Click Add button
        add_button = driver.find_element(By.ID, "add_btn")
        assert add_button.is_displayed()
        add_button.click()
        print("add button was clicked")
        time.sleep(2)

        # Verify Row 2 input field is displayed
        row_field_02 = driver.find_element(By.ID, "row2")
        assert row_field_02.is_displayed(), "Row 2"
        input_field2 = driver.find_element(By.TAG_NAME, "input")
        assert input_field2.is_displayed()
        print("Second input is displayed")
        time.sleep(2)

        # # This is pytest mark to execute marks
        # @pytest.mark.negative_exceptions
        def test_exception_case02(self, driver):
            # Open browser
            driver.get("https://practicetestautomation.com/practice-test-exceptions/")
            homepage_title = driver.find_element(By.TAG_NAME, "h2")
            actual_homepage_title = homepage_title.text
            assert actual_homepage_title == "Test Exceptions"
            print("Validate header title")
            time.sleep(2)

            # Click Add button
            add_button = driver.find_element(By.ID, "add_btn")
            assert add_button.is_displayed()
            add_button.click()
            print("add button was clicked")
            time.sleep(2)

            # Verify Row 2 input field is displayed
            row_field_02 = driver.find_element(By.ID, "row2")
            assert row_field_02.is_displayed(), "Row 2"
            input_field2 = driver.find_element(By.TAG_NAME, "input")
            assert input_field2.is_displayed()
            print("Second input is displayed")
            time.sleep(2)

            # # Clear input field
            # input_field2.click()
            # # input_field2.clear()
            # print("Clear input field")

            # Type text into the input field
            input_field2 = driver.find_element(By.cssSelector("*input"))
            input_field2.send_keys("Chinese")
            print("Type text into the input field")

            # Click on Save
            save_button = driver.find_element(By.NAME, "Save")
            save_button.is_displayed(), "Save"
            save_button.click()
            print("Click on Save")

            # Verify that the row 2 has been saved
            input_field2.send_keys(disable())
            print("Verify that the row 2 has been saved")

            # Verify confirmation
            confirmation_alert = driver.find_element(By.ID, "confirmation")
            confirmation_alert.is_displayed(), "Row 2 was saved"
            # confirmation_alert = driver.find_element(By.ID, "confirmation")
            print("Verify confirmation")
