import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SlaRiskHeatmapPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def pause(self, seconds=2, reason=""):
        if reason:
            print(f"⏸ {reason} — waiting {seconds}s")
        time.sleep(seconds)

    # -------------------------------------------------
    # REACT-SAFE DATE INPUT  ✅ FIXED LOCATION
    # -------------------------------------------------
    def set_date_input(self, label_text, value):
        input_box = self.wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                f"//label[contains(text(),'{label_text}')]/following::input[1]"
            ))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", input_box
        )

        self.driver.execute_script("""
            arguments[0].value = '';
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, input_box, value)

        time.sleep(0.5)

    # =========================
    # SCROLL HELPERS
    # =========================
    def scroll_section_into_view(self, section_text):
        section = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//section[.//h1[contains(text(),'{section_text}')]]")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", section
        )
        time.sleep(0.5)

    def scroll_container(self, container):
        self.driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", container
        )
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].scrollTop = 0", container)
        time.sleep(0.5)

    # =========================
    # STRATEGIC OVERVIEW
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
    # ICON CLICK
    # =========================
    def click_section_icon(self, section_text):
        svg_icon = self.wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                f"//section[.//h1[contains(text(),'{section_text}')]]"
                "//div[contains(@class,'relative')]//*[name()='svg']"
            ))
        )

        ActionChains(self.driver) \
            .move_to_element(svg_icon) \
            .pause(0.3) \
            .click() \
            .perform()

        time.sleep(0.5)

    # =========================
    # OPERATIONAL INSIGHTS TAB
    # =========================
    def go_to_operational_insights(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Operational Insights']")
            )
        )
        btn.click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[normalize-space()='Trend Analysis']")
            )
        )

    # =========================
    # OPERATIONAL INSIGHTS FLOW
    # =========================
    def automate_operational_insights(self):
        # ---------------- ASSERT CONTEXT ----------------
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[normalize-space()='Trend Analysis']")
            )
        )
        self.pause(2, "Operational Insights loaded")

        # ---------------- KPI ----------------
        kpi = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[normalize-space()='KPI:']/following::select[1]")
            )
        )
        Select(kpi).select_by_visible_text("Misallocation Rate")
        self.pause(2, "KPI selected")

        # ---------------- FACILITY ----------------
        facility = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[normalize-space()='Facility:']/following::select[1]")
            )
        )
        Select(facility).select_by_visible_text("CHI1 (Aurora, IL)")
        self.pause(2, "Facility selected")

        # ---------------- START DATE ----------------
        self.set_date_input("Start Date", "2024-12-04")
        self.pause(1, "Start date set")

        # ---------------- END DATE ----------------
        self.set_date_input("End Date", "2025-07-30")
        self.pause(1, "End date set")

        # ---------------- GENERATE REPORT ----------------
        generate_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Generate Report']")
            )
        )
        generate_btn.click()
        self.pause(4, "Waiting for chart generation")

        # ---------------- CHART ASSERT ----------------
        chart = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@id,'highcharts')]//*[name()='svg']")
            )
        )
        self.pause(2, "Chart rendered")
        self.hover_highchart_data()

        # # ---------------- INTERACT WITH CHART ----------------
        # for i in range(3):
        #     self.driver.execute_script(
        #         "arguments[0].dispatchEvent(new MouseEvent('click',{bubbles:true}));",
        #         chart
        #     )
        #     self.pause(1, f"Chart click {i + 1}")

        print("✅ Operational Insights fully automated (VISIBLE + REAL)")

    def hover_highchart_data(self):
        paths = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH,
                 "//div[contains(@id,'highcharts')]//*[name()='path' and @aria-label]")
            )
        )

        actions = ActionChains(self.driver)

        for idx, path in enumerate(paths[:5], start=1):
            label = path.get_attribute("aria-label")
            print(f"⏸ Hover {idx}: {label}")
            actions.move_to_element(path).perform()
            time.sleep(1.5)

    # =========================
    # MASTER FLOW
    # =========================
    def validate_full_page(self):

        self.scroll_kpi_section()
        self.scroll_sla_section()
        self.click_section_icon("SLA & Risk")

        self.scroll_section_into_view("Bottleneck")
        self.scroll_bottleneck_section()
        self.click_section_icon("Bottleneck")

        self.go_to_operational_insights()
        self.automate_operational_insights()
