from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class CamelodgeRaw():

    def test_validation(self):
        base_url = "https://camelodge.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        '''Signup'''
        signup_link = driver.find_element(By.LINK_TEXT, "Sign Up")
        signup_link.click()

        # Validate signup input is autofocus
        email_field_autofocus = driver.find_element(By.CSS_SELECTOR, "input[autofocus='autofocus']#user_email")
        if email_field_autofocus:
            print("Autofocus is on Email field")
        else:
            print("Autofocus is not on Email field")

        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys("jack.luze@gmail.com")
        password_field = driver.find_element(By.ID, "user_password")
        password = "123456"
        password_field.send_keys(password)
        confirmation_password_field = driver.find_element(By.ID, "user_password_confirmation")
        confirmation_password_field.send_keys(password)
        signup_button = driver.find_element(By.CSS_SELECTOR, "#new_user input[value='Sign up']")
        signup_button.click()

        welcome_message_sign_up = driver.find_element(By.XPATH, "//div[@class='alert-notice'][contains(text(), 'Welcome! You have signed up successfully.')]")
        if welcome_message_sign_up:
            print("Sign up is successful")
        else:
            print("Sign up failed")

        # Validate signout
        log_out = driver.find_element(By.LINK_TEXT, "Log out")
        log_out.click()
        log_out_message = driver.find_element(By.XPATH,
                                              "//div[@class='alert-notice'][contains(text(), 'Signed out successfully.')]")
        time.sleep(5)
        if (driver.current_url == base_url) and (driver.find_element(By.LINK_TEXT, "Sign In")) and log_out_message:
            print("Signed out successfully")
        else:
            print("Sign out failed")

        # Validate sign in
        signin_link = driver.find_element(By.LINK_TEXT, "Sign In")
        signin_link.click()

        # Validate sign in input is autofocus
        email_field_autofocus = driver.find_element(By.CSS_SELECTOR, "input[autofocus='autofocus']#user_email")
        if email_field_autofocus:
            print("Autofocus is on SignIn Email field")
        else:
            print("Autofocus is not on SignIn Email field")
        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys("jack.luze@gmail.com")
        password_field = driver.find_element(By.ID, "user_password")
        password = "123456"
        password_field.send_keys(password)
        signin_button = driver.find_element(By.CSS_SELECTOR, "#new_user input[value='Log in']")
        signin_button.click()

        welcome_message_sign_in = driver.find_element(By.XPATH,
                                              "//div[@class='alert-notice'][contains(text(), 'You have logged in successfully, great job!')]")
        if welcome_message_sign_in:
            print("Sign in is successful")
            # Validate City Search
            city = driver.find_element(By.ID, "city")
            city.clear()
            city.send_keys("Vancouver")
            time.sleep(10)
            for lh in driver.find_elements_by_xpath("//ul[@id='searchresults']//lh"):
                search_tag = lh.text
                search_tag_elements = []
                for element in lh.find_elements_by_xpath("./following-sibling::*"):
                    if element.tag_name == 'lh':
                        break
                    if "Vancouver" in element.text:
                        print("Search result is related to Vancouver")
                    else:
                        print("Search result is not related to Vancouver")
                        print(search_tag, element.text)
                    search_tag_elements.append(element.text)

                print(search_tag, search_tag_elements)
            check_hotel_prices_button = driver.find_element_by_css_selector("input[value='Check Hotel Prices'][name='submit']")
            check_hotel_prices_button.click()
            "#date_from" "#date_to" "input[value='Check Hotel Prices'][name='submit']"
            # by default date from should be current date + 1
            # by default date to should be current date + 2

            # then sorting
        else:
            print("Sign in failed")



        # Validate delete account
        account_settings = driver.find_element(By.LINK_TEXT, "My Account")
        account_settings.click()

        if driver.current_url == "https://camelodge.com/users/edit":
            print("Successfully navigated to User Account Settings page")
            cancel_account_button = driver.find_element(By.CSS_SELECTOR, "input[value='Cancel my account']")
            cancel_account_button.click()
            cancel_account_message = driver.find_element(By.XPATH,
                                     "//div[@class='alert-notice'][contains(text(), 'Bye! Your account has been successfully cancelled. We hope to see you again soon.')]")
            if cancel_account_message:
                print("Cancelled account Successfully")
            else:
                print("Cancel Account Failed")
        else:
            print("Navigation to User Account Settings NOT successful")

        driver.close()
        driver.quit()


ff = CamelodgeRaw()
ff.test_validation()
