import pytest
from pages.login_page import LoginPage
from pages.slider_page import SliderPage
from pages.sla_risk_heatmap_page import SlaRiskHeatmapPage


@pytest.mark.e2e
def test_sla_risk_heatmap_full_flow(driver):
    """
    Login → Part Allocation → SLA & Risk Heatmap
    Scroll all containers → Click icons
    """

    # ---------- LOGIN ----------
    LoginPage(driver).login("user@gmail.com", "12345")

    # ---------- NAVIGATION ----------
    SliderPage(driver).hover_and_click_sla_risk_heatmap()

    # ---------- VALIDATION ----------
    SlaRiskHeatmapPage(driver).validate_full_page()
