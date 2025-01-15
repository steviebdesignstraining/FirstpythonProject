import time

import pytest
from selenium.webdriver.common.by import By

class TestPositiveScenario:

    # This is pytest mark to execute marks
    @pytest.mark.login
    # This is pytest mark to execute marks
    @pytest.mark.positive
    # Parameterize stores data
    @pytest.mark.parametrize("username, password",
                             [("student", "Password123")])
    def test_positive_login(self, driver, username, password):

        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # # Validate that user has landed on page
        homepage_title = driver.find_element(By.TAG_NAME, "h2")
        actual_homepage_title = homepage_title.text
        assert actual_homepage_title == "Test login"
        print("Validate header title")

        # Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)
        print("Entered username.")
        time.sleep(2)

        # Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        print("Entered password.")
        time.sleep(2)

        # Click on submit
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        print("Clicked submit button.")
        time.sleep(2)

        # Verify new page URL contains https://practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
        print("Verify new page URL")

        # # Validate that user has logged in
        logged_in_title = driver.find_element(By.TAG_NAME, "h1")
        actual_text = logged_in_title.text
        assert actual_text == "Logged In Successfully"
        print("Validate header title")

        # Click on logout
        log_out_button = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_button.is_displayed()
        log_out_button.click()
        print("Clicked Log out button.")
        time.sleep(2)

        # # Validate that user has landed on homr page
        homepage_title = driver.find_element(By.TAG_NAME, "h2")
        actual_homepage_title = homepage_title.text
        assert actual_homepage_title == "Test login"
        print("Verify that user is taken back to the homepage")