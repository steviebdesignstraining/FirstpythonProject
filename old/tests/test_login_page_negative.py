import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    # This is pytest mark to execute marks
    @pytest.mark.login
    # This is pytest mark to execute marks
    @pytest.mark.negative
    # Parameterize stores data
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "Password1234", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):  # Fixture is being called from the pytest.fixture to call chrome webdriver

        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-login/")
        homepage_title = driver.find_element(By.TAG_NAME, "h2")
        actual_homepage_title = homepage_title.text
        assert actual_homepage_title == "Test login"
        print("Validate header title")

        # Type username incorrectly into username field
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)
        print(f'Entered', {username})
        time.sleep(2)

        # Type password Password123 into password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        print(f"Entered", {password})
        time.sleep(2)

        # Push Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        print("Clicked submit button.")
        time.sleep(2)

        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed(), "Error message should display, but it should"
        print("Verify error message is displayed")

        # Verify error message text is your username is invalid
        error_message_text = error_message.text
        assert error_message_text == expected_error_message


class TestPasswordNegativeScenarios:
    @pytest.mark.login  # This is pytest mark to execute marks
    @pytest.mark.negative  # This is pytest mark to execute marks
    def test_password_negative_login(self, driver):
        # Open browser
        driver.get("https://practicetestautomation.com/practice-test-login/")
        homepage_title = driver.find_element(By.TAG_NAME, "h2")
        actual_homepage_title = homepage_title.text
        assert actual_homepage_title == "Test login"
        print("Validate header title")

        # Type username incorrectly into username field
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")
        print(f"Entered username.")
        time.sleep(2)

        # Type password Password123 into password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password1234")
        print("Entered password.")
        time.sleep(2)

        # Push Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        print("Clicked submit button.")
        time.sleep(2)

        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed(), "Error message should display, but it should"
        print("Verify error message is displayed")

        # Verify error message text is your username is invalid
        error_message_text = error_message.text
        assert error_message_text == ("Your password is invalid!")
