import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlaRiskHeatmapPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # --------------------------------------------------
    # MAIN PAGE SCROLL (down → up)
    # --------------------------------------------------
    def scroll_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(2)

    # --------------------------------------------------
    # GENERIC CONTAINER SCROLL
    # --------------------------------------------------
    def scroll_container(self, container):
        self.driver.execute_script(
            """
            arguments[0].scrollTop = arguments[0].scrollHeight;
            """,
            container
        )
        time.sleep(2)

        self.driver.execute_script(
            """
            arguments[0].scrollTop = 0;
            """,
            container
        )
        time.sleep(1)

    # --------------------------------------------------
    # KPI CONTAINER
    # --------------------------------------------------
    def scroll_kpi_container(self):
        kpi_container = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//section[.//h1[contains(text(),'KPI')]]//div[contains(@class,'overflow-y-auto')]")
            )
        )
        self.scroll_container(kpi_container)

    # --------------------------------------------------
    # SLA & RISK HEATMAP CONTAINER
    # --------------------------------------------------
    def scroll_sla_heatmap_container(self):
        heatmap_container = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//section[.//h1[contains(text(),'SLA & Risk')]]//div[contains(@class,'overflow-y-auto')]")
            )
        )
        self.scroll_container(heatmap_container)

    # --------------------------------------------------
    # BOTTLENECK CONTAINER
    # --------------------------------------------------
    def scroll_bottleneck_container(self):
        bottleneck_container = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//section[.//h1[contains(text(),'Bottleneck')]]//div[contains(@class,'overflow-y-auto')]")
            )
        )
        self.scroll_container(bottleneck_container)

    # --------------------------------------------------
    # CLICK INFO ICONS (ONLY AFTER SCROLL)
    # --------------------------------------------------
    def click_section_icon(self, section_title: str):
        """
        Click info (ⓘ) icon for a given section title
        Works with SVG icons (not <img>)
        """

        section = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//section[.//h1[contains(normalize-space(),'{section_title}')]]")
            )
        )

        icon = section.find_element(
            By.XPATH,
            ".//div[contains(@class,'flex') and contains(@class,'justify-between')]"
            "//div[contains(@class,'relative') and contains(@class,'flex')]"
            "//*[name()='svg']"
        )

        self.driver.execute_script("arguments[0].click();", icon)
        time.sleep(2)

    # --------------------------------------------------
    # FULL VALIDATION FLOW
    # --------------------------------------------------
    def validate_full_page(self):
        # 1️⃣ main page
        self.scroll_main_page()

        # 2️⃣ containers
        self.scroll_kpi_container()
        self.scroll_sla_heatmap_container()
        self.scroll_bottleneck_container()

        # 3️⃣ icons (AFTER scrolling)
        self.click_section_icon("SLA & Risk")
        self.click_section_icon("Bottleneck")
