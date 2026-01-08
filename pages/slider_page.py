from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


class SliderPage:
    """
    Slider navigation for Tower Track
    Reused logic from Facility Status Tracker
    Extended safely for SLA & Risk Heatmap
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # =========================================================
    # BACKWARD COMPATIBILITY (DO NOT REMOVE)
    # =========================================================
    def click_slider(self, slider_name: str):
        """
        Legacy method used by older tests
        """
        self.click_slider_button(slider_name)

    def hover_and_click_facility_status_tracker(self):
        """
        Legacy combined navigation used by Facility Status tests
        """
        self.navigate_to_part_allocation_insights()
        self.open_facility_status_tracker()

    # =========================================================
    # SLIDER BUTTON NAVIGATION ONLY
    # =========================================================
    def click_slider_button(self, name: str):
        """
        Click slider button by exact text
        NO hover
        NO mouse movement
        """
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[normalize-space()='{name}']")
            )
        )
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    def navigate_to_part_allocation_insights(self):
        """
        As per UI flow:
        Demand → Capacity → Supply → Part Allocation
        """
        self.click_slider_button("Demand Insights")
        self.click_slider_button("Capacity Insights")
        self.click_slider_button("Supply Insights")
        self.click_slider_button("Part Allocation Insights")

    # =========================================================
    # FACILITY STATUS TRACKER (EXISTING – DO NOT CHANGE)
    # =========================================================
    def open_facility_status_tracker(self):
        """
        Direct click on Facility Status Tracker image
        NO hover
        """
        tracker_img = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//img[@alt='Facility Status Tracker']")
            )
        )
        self.driver.execute_script("arguments[0].click();", tracker_img)
        time.sleep(2)

    # =========================================================
    # SLA & RISK HEATMAP (NEW – REUSED PATTERN)
    # =========================================================
    def hover_and_click_sla_risk_heatmap(self):
        """
        Navigate to SLA & Risk Heatmap
        Reuses Facility Status hover pattern
        """

        # Ensure Part Allocation is active
        self.navigate_to_part_allocation_insights()

        # ✅ EXACT locator
        sla_risk_img = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt='SLA & Risk Heatmap']")
            )
        )

        actions = ActionChains(self.driver)

        # Hover (important)
        actions.move_to_element(sla_risk_img).perform()
        time.sleep(2)

        # Click
        sla_risk_img.click()
        time.sleep(2)

