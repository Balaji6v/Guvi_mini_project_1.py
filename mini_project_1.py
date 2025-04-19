from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

class GuviTests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://www.guvi.in/"

    def test_case_1(self):
        self.driver.get(self.base_url)
        print("Test Case 1: URL is valid and page loaded.")

    def test_case_2(self):
        expected_title = "GUVI | Learn to code in your native language"
        actual_title = self.driver.title
        print(f"Test Case 2: Page Title = {actual_title}")
        if actual_title == expected_title:
            print("Test Case 2: Title shown")
        else:
            print("Test Case 2 :Title not shown.")

    def test_case_3(self):
        try:
            login_button = self.driver.find_element(By.LINK_TEXT, "Login")
            if login_button.is_displayed() and login_button.is_enabled():
                print("Test Case 3: Login button is visible and clickable.")
            else:
                print("Test Case 3 Failed: Login button not interactive.")
        except NoSuchElementException:
            print("Test Case 3 Failed: Login button not found.")

    def test_case_4(self):
        try:
            sign_up_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign up')]")))
            print("Test Case 4: Sign-Up button is visible and clickable.")
        except TimeoutException:
            print("Test Case 4 Failed: Sign-Up button not found.")

    def test_case_5(self):
        try:
            sign_up_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign up')]")))
            sign_up_btn.click()
            self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
            print("Test Case 5 Passed: Sign-Up modal opened.")
        except Exception as e:
            print("Test Case 5 Error: Sign-Up modal not opened", e)

    def test_case_6(self):
        try:
            self.driver.get("https://www.guvi.in/sign-in/")
            self.wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("balajivenkat132002@gmail.com")
            self.driver.find_element(By.ID, "password").send_keys("Balaji@13")
            self.driver.find_element(By.ID, "login-btn").click()
            time.sleep(3)
            if "dashboard" in self.driver.current_url or "Hi" in self.driver.page_source:
                print("Test Case 6 Passed: Login successful.")
            else:
                print("Test Case 6 Failed: Login unsuccessful.")
        except Exception as e:
            print("Test Case 6 Error:", e)

    def test_case_7(self):
        try:
            self.driver.get("https://www.guvi.in/sign-in/")
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            email_field.send_keys("invalid_email@example.com")
            password_field.send_keys("wrongpassword")
            self.driver.find_element(By.ID, "login-btn").click()

            error_message = self.wait.until( EC.visibility_of_element_located((By.CLASS_NAME, "error-msg")))
            print("Test Case 7 Passed: Error message detected.")
        except TimeoutException:
            print("Test Case 7 Failed:login failed.")
        except NoSuchElementException as e:
            print("Test Case 7 Error: Element not found -", e)
        except Exception as e:
            print("Test Case 7 Error:", e)

    def run_all_tests(self):
        try:
            self.test_case_1()
            self.test_case_2()
            self.test_case_3()
            self.test_case_4()
            self.test_case_5()
            self.test_case_6()
            self.test_case_7()
        finally:
            print("\n Browser closed.")
            self.driver.quit()

if __name__ == "__main__":
    obj = GuviTests()
    obj.run_all_tests()
