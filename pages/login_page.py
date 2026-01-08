from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Stable Login Page Object (Direct Login)
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ================= LOCATORS =================
    username_input = "//input[@placeholder='Username or email']"
    password_input = "//input[@placeholder='Password']"
    login_button = "//button[normalize-space()='LOGIN']"

    remember_me_label = "//label[normalize-space()='Remember Me']"
    remember_me_checkbox = (
        "//label[normalize-space()='Remember Me']/preceding-sibling::input | "
        "//label[normalize-space()='Remember Me']/input"
    )

    # ================= BASIC ACTIONS =================
    def clear_fields(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.username_input))
        ).clear()
        self.driver.find_element(By.XPATH, self.password_input).clear()

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.login_button))
        ).click()

    # ================= REMEMBER ME =================
    def click_remember_me_if_not_selected(self):
        """
        Reliable Remember Me click for React / styled checkboxes
        """

        try:
            # This targets the visible clickable area
            remember_me_container = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//label[normalize-space()='Remember Me'] | //span[contains(text(),'Remember')]"
                ))
            )

            remember_me_container.click()
            print("✅ Remember Me clicked")

        except Exception as e:
            print("⚠️ Remember Me click failed:", e)

    # ================= LOGIN FLOW =================
    def login(self, username, password, remember_me=False):
        self.clear_fields()

        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)

        if remember_me:
            self.click_remember_me_if_not_selected()

        self.click_login()

        # ✅ STABLE WAIT: any page navigation after login
        self.wait.until(EC.url_changes(self.driver.current_url))

    # ================= ALERT HANDLING =================
    def accept_alert_if_present(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            print("⚠️ Alert accepted")
        except NoAlertPresentException:
            pass
