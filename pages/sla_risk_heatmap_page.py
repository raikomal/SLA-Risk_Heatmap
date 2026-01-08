import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SlaRiskHeatmapPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    # =========================
    # GENERIC CONTAINER SCROLL
    # =========================
    def scroll_container(self, container):
        # down
        self.driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight",
            container
        )
        time.sleep(1)

        # up
        self.driver.execute_script(
            "arguments[0].scrollTop = 0",
            container
        )
        time.sleep(1)

    # =========================
    # KPI SECTION
    # =========================
    def scroll_kpi_section(self):
        section = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//section[.//h1[contains(text(),'KPI')]]")
            )
        )
        container = section.find_element(
            By.XPATH, ".//div[contains(@class,'overflow-y-auto')]"
        )
        self.scroll_container(container)

    # =========================
    # SLA & RISK HEATMAP SECTION
    # =========================
    def scroll_sla_section(self):
        section = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//section[.//h1[contains(text(),'SLA & Risk')]]")
            )
        )
        container = section.find_element(
            By.XPATH, ".//div[contains(@class,'overflow-y-auto')]"
        )
        self.scroll_container(container)

    # =========================
    # BOTTLENECK SECTION
    # =========================
    def scroll_bottleneck_section(self):
        section = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//section[.//h1[contains(text(),'Bottleneck')]]")
            )
        )
        container = section.find_element(
            By.XPATH, ".//div[contains(@class,'overflow-y-auto')]"
        )
        self.scroll_container(container)

    # =========================
    # SVG ICON CLICK (CRITICAL)
    # =========================
    def click_section_icon(self, section_text):
        section = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//section[.//h1[contains(text(),'{section_text}')]]")
            )
        )

        svg_icon = section.find_element(
            By.XPATH,
            ".//div[contains(@class,'relative')]//*[name()='svg']"
        )

        ActionChains(self.driver)\
            .move_to_element(svg_icon)\
            .pause(0.5)\
            .click()\
            .perform()

        time.sleep(1)

    # =========================
    # MASTER FLOW
    # =========================
    def validate_full_page(self):
        # -------- 1. KPI (already visible) --------
        self.scroll_kpi_section()

        # -------- 2. SLA & Risk (already visible) --------
        self.scroll_sla_section()
        self.click_section_icon("SLA & Risk")

        # -------- 3. MAIN PAGE SCROLL (CRITICAL) --------
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(2)

        # -------- 4. WAIT FOR BOTTLENECK SECTION TO RENDER --------
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//section[.//h1[contains(text(),'Bottleneck')]]")
            )
        )

        # -------- 5. NOW SCROLL BOTTLENECK CONTAINER --------
        self.scroll_bottleneck_section()
        self.click_section_icon("Bottleneck")
