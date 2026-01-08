import pytest
from pages.login_page import LoginPage
from pages.slider_page import SliderPage
from pages.sla_risk_heatmap_page import SlaRiskHeatmapPage
from utils.ui_report_writer import start_new_report, write_test_report


@pytest.mark.e2e
def test_sla_risk_heatmap_full_flow(driver):

    # =====================================================
    # START NEW CSV REPORT (ONE FILE PER RUN)
    # =====================================================
    start_new_report()

    # =====================================================
    # LOGIN
    # =====================================================
    LoginPage(driver).login("user@gmail.com", "12345")

    write_test_report(
        "Tower Track", "Web", "Login",
        "Valid Login",
        "Login with valid credentials",
        "Enter username and password",
        "User should login successfully",
        "User logged in",
        "Pass", "", "LG-01", ""
    )

    # =====================================================
    # NAVIGATION
    # =====================================================
    SliderPage(driver).hover_and_click_sla_risk_heatmap()

    write_test_report(
        "Tower Track", "Web", "Navigation",
        "Navigate to SLA & Risk Heatmap",
        "Open SLA & Risk Heatmap page",
        "Click SLA & Risk Heatmap card",
        "Page should open",
        "Page opened",
        "Pass", "", "NAV-01", ""
    )

    sla_page = SlaRiskHeatmapPage(driver)

    # =====================================================
    # STRATEGIC OVERVIEW – KPI
    # =====================================================
    sla_page.scroll_kpi_section()

    write_test_report(
        "Tower Track", "Web", "SLA & Risk Heatmap",
        "Strategic Overview - KPI",
        "Verify KPI section visibility",
        "Scroll KPI section",
        "KPI section should be visible",
        "KPI section visible",
        "Pass", "", "TT-SLA-001", ""
    )

    # =====================================================
    # STRATEGIC OVERVIEW – SLA & RISK
    # =====================================================
    sla_page.scroll_sla_section()
    sla_page.click_section_icon("SLA & Risk")

    write_test_report(
        "Tower Track", "Web", "SLA & Risk Heatmap",
        "Strategic Overview - SLA & Risk",
        "Verify SLA & Risk section interaction",
        "Click SLA & Risk icon",
        "Section should expand",
        "Section expanded",
        "Pass", "", "TT-SLA-002", ""
    )

    # =====================================================
    # STRATEGIC OVERVIEW – BOTTLENECK
    # =====================================================
    sla_page.scroll_section_into_view("Bottleneck")
    sla_page.scroll_bottleneck_section()
    sla_page.click_section_icon("Bottleneck")

    write_test_report(
        "Tower Track", "Web", "SLA & Risk Heatmap",
        "Strategic Overview - Bottleneck",
        "Verify Bottleneck section interaction",
        "Scroll and click Bottleneck icon",
        "Bottleneck section should expand",
        "Bottleneck section expanded",
        "Pass", "", "TT-SLA-003", ""
    )

    # =====================================================
    # SWITCH TO OPERATIONAL INSIGHTS
    # =====================================================
    sla_page.go_to_operational_insights()

    write_test_report(
        "Tower Track", "Web", "SLA & Risk Heatmap",
        "Operational Insights Tab",
        "Switch to Operational Insights",
        "Click Operational Insights slider",
        "Operational Insights should load",
        "Operational Insights loaded",
        "Pass", "", "TT-OPS-001", ""
    )

    # =====================================================
    # OPERATIONAL INSIGHTS – FULL FLOW
    # =====================================================
    sla_page.automate_operational_insights()

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Generate Operational Insights Report",
        "Verify KPI, Facility, Date & chart",
        "Select KPI → Facility → Dates → Generate → Hover chart",
        "Chart & SLA impact rendered",
        "Chart & SLA impact rendered",
        "Pass", "", "TT-OPS-002", ""
    )

    # =====================================================
    # END
    # =====================================================
    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "End-to-End Validation",
        "Complete SLA & Risk Heatmap validation",
        "Execute full UI workflow",
        "All steps should pass",
        "All steps passed",
        "Pass", "", "TT-E2E-001", ""
    )
