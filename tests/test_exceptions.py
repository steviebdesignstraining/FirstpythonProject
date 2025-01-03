import time

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


# This is pytest mark to execute marks

class TestExceptionCase01:
    @pytest.mark.positive_exceptions
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

        wait = WebDriverWait(driver, 10)
        row_field_02 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        input_field2 = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert input_field2.is_displayed()
        print("Second input is displayed")

    # This is pytest mark to execute marks
class TestExceptionCase02:
    @pytest.mark.positive_exceptions
    @pytest.mark.parametrize("row_2", [("Chinese",)])
    def test_exception_case02(self, driver, row_2):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        homepage_title = driver.find_element(By.TAG_NAME, "h2")
        actual_homepage_title = homepage_title.text
        assert actual_homepage_title == "Test Exceptions"
        print("Validate header title")

        # Click Add button
        add_button = driver.find_element(By.ID, "add_btn")
        assert add_button.is_displayed()
        add_button.click()
        print("add button was clicked")

        # Wait for Row 2 input field to load
        wait = WebDriverWait(driver, 10)
        row_field_02 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        print("Row 2 input field is found.")

        # Verify Row 2 input field is displayed
        input_field2 = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert input_field2.is_displayed(), "Input field not found"
        print("Second input is displayed")


        # Type text into the input field
        input_field2.click()
        input_field2.send_keys(row_2[0])  # Use row_2[0], as row_2 is a tuple
        print(f"Entered '{row_2[0]}' into the input field")

        # Click on Save
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        # Verify the confirmation message
        confirmation_alert = wait.until(EC.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_alert.text
        assert confirmation_message == "Row 2 was saved", "Confirmation is incorrect or missing"
        print("Verified that Row 2 was successfully saved!")

class TestExceptionCase03:
    @pytest.mark.positive_exceptions
    @pytest.mark.positive_exceptions03
    @pytest.mark.parametrize("row_1", [("Mexican"), ("Caribbean food")])
    def test_exception_case03(self, driver, row_1):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        homepage_title = driver.find_element(By.TAG_NAME, "h2")
        actual_homepage_title = homepage_title.text
        assert actual_homepage_title == "Test Exceptions", "Header title mismatch!"
        print("Validate header title")

        input_field1 = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        assert input_field1.get_attribute("value") == "Pizza", "Input field value is incorrect"

        # Click Edit button
        edit_button = driver.find_element(By.ID, "edit_btn")
        assert edit_button.is_displayed(), "Edit button not displayed"
        edit_button.click()
        print("Edit button was clicked")

        # Wait for Row 1 input field to load
        wait = WebDriverWait(driver, 10)
        row_field_01 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row1']/input")))
        print("Row 2 input field is found.")

        # Type text into the input field
        input_field1 = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        input_field1.clear()
        input_field1.send_keys(row_1[0])  # Use row_2[0], as row_2 is a tuple
        print(f"Entered '{row_1[0]}' into the input field")

        # Click on Save
        driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Save']").click()

        # Verify the confirmation message
        confirmation_alert = wait.until(EC.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_alert.text
        assert confirmation_message == "Row 1 was saved", "Confirmation is incorrect or missing"
        print("Verified that Row 1 was successfully saved!")

        # Verify input field has been updated
        assert input_field1.get_attribute("value") == row_1[0], "Input field value is incorrect"

class TestExceptionCase04:
    @pytest.mark.positive_exceptions
    @pytest.mark.positive_exceptions04
    def test_exception_case02(self, driver):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        homepage_title = driver.find_element(By.TAG_NAME, "h2")
        actual_homepage_title = homepage_title.text
        assert actual_homepage_title == "Test Exceptions"
        print("Validate header title")
        time.sleep(2)

        # Find the instructions text element
        instruction_text = driver.find_element(By.ID, "instructions")
        assert instruction_text.is_displayed(), 'Push “Add” button to add another row'

        # Push add button
        add_button = driver.find_element(By.ID, "add_btn")
        assert add_button.is_displayed()
        add_button.click()
        print("add button was clicked")

        # Wait for the instructions element to no longer be visible
        wait = WebDriverWait(driver, 10)
        instructions = wait.until(EC.invisibility_of_element_located((By.ID, "instructions")), "Instructions text element should not be displayed.")
        print("Instruction text element is no longer displayed.")


class TestExceptionCase05:
    @pytest.mark.positive_exceptions
    @pytest.mark.positive_exceptions05
    def test_exception_case05(self, driver):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        homepage_title = driver.find_element(By.TAG_NAME, "h2")
        actual_homepage_title = homepage_title.text
        assert actual_homepage_title == "Test Exceptions"
        print("Validate header title")
        time.sleep(2)

        # Find the instructions text element
        instruction_text = driver.find_element(By.ID, "instructions")
        assert instruction_text.is_displayed(), 'Push “Add” button to add another row'

        # Push add button
        add_button = driver.find_element(By.ID, "add_btn")

        # Click Add button
        add_button = driver.find_element(By.ID, "add_btn")
        assert add_button.is_displayed()
        add_button.click()
        print("add button was clicked")

        wait = WebDriverWait(driver, 10)
        row_field_02 = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")), "Failed waiting for row 2 input to be visible")

        # Verify Row 2 input field is displayed
        input_field2 = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert input_field2.is_displayed(), "Input field not found"
        print("Second input is displayed")

        # Use WebDriverWait to locate the input field
        wait = WebDriverWait(driver, 10)
        input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#row2 input")))
