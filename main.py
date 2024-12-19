import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser
driver = webdriver.Chrome()

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")

# # Validate that user has landed on page
homepage_title = driver.find_element(By.TAG_NAME, "h2")
actual_homepage_title = homepage_title.text
assert actual_homepage_title == "Test login"
print("Validate header title")

# Enter username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("student")
print("Entered username.")
time.sleep(2)

# Enter password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Password123")
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
Log_out_button = driver.find_element(By.LINK_TEXT, "Log out")
assert Log_out_button.is_displayed()
Log_out_button.click()
print("Clicked Log out button.")
time.sleep(2)

# # Validate that user has landed on homr page
homepage_title = driver.find_element(By.TAG_NAME, "h2")
actual_homepage_title = homepage_title.text
assert actual_homepage_title == "Test login"
print("Verify that user is taken back to the homepage")