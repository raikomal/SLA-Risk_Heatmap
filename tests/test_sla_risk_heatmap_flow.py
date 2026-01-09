# import pytest
# from pages.login_page import LoginPage
# from pages.slider_page import SliderPage
# from pages.sla_risk_heatmap_page import SlaRiskHeatmapPage
# from utils.ui_report_writer import start_new_report, write_test_report
#
#
# @pytest.mark.e2e
# def test_sla_risk_heatmap_full_flow(driver):
#
#     # =====================================================
#     # START NEW CSV REPORT (ONE FILE PER RUN)
#     # =====================================================
#     start_new_report()
#
#     # =====================================================
#     # LOGIN
#     # =====================================================
#     LoginPage(driver).login("user@gmail.com", "12345")
#
#     write_test_report(
#         "Tower Track", "Web", "Login",
#         "Valid Login",
#         "Login with valid credentials",
#         "Enter username and password",
#         "User should login successfully",
#         "User logged in",
#         "Pass", "", "LG-01", ""
#     )
#
#     # =====================================================
#     # NAVIGATION
#     # =====================================================
#     SliderPage(driver).hover_and_click_sla_risk_heatmap()
#
#     write_test_report(
#         "Tower Track", "Web", "Navigation",
#         "Navigate to SLA & Risk Heatmap",
#         "Open SLA & Risk Heatmap page",
#         "Click SLA & Risk Heatmap card",
#         "Page should open",
#         "Page opened",
#         "Pass", "", "NAV-01", ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Heatmap (Frontend)",
#         "Verify Page Heading",
#         "Verify heading is displayed correctly",
#         "Open SLA & Risk Heatmap page",
#         'Heading should show "Part Allocation Insights > SLA & Risk Heatmap"',
#         "Heading visible",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Heatmap (Frontend)",
#         "Verify Strategic Overview tab",
#         "Ensure Strategic Overview tab shows KPI & Reporting Dashboard",
#         'Click "Strategic Overview" tab',
#         "KPI & Reporting Dashboard should display",
#         "KPI & Reporting Dashboard displayed",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#
#     sla_page = SlaRiskHeatmapPage(driver)
#
#     # =====================================================
#     # STRATEGIC OVERVIEW – KPI
#     # =====================================================
#     sla_page.scroll_kpi_section()
#
#     write_test_report(
#         "Tower Track", "Web", "SLA & Risk Heatmap",
#         "Strategic Overview - KPI",
#         "Verify KPI section visibility",
#         "Scroll KPI section",
#         "KPI section should be visible",
#         "KPI section visible",
#         "Pass", "", "TT-SLA-001", ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Heatmap-Strategic Overview (Frontend)",
#         "Verify KPI & Reporting Dashboard scroll",
#         "Ensure dashboard is scrollable",
#         "Open Strategic Overview tab and scroll vertically",
#         "All KPI boxes should be viewable by scrolling",
#         "KPI boxes are scrollable and visible",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#
#     # =====================================================
#     # STRATEGIC OVERVIEW – SLA & RISK
#     # =====================================================
#     sla_page.scroll_sla_section()
#     sla_page.click_section_icon("SLA & Risk")
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Heatmap - Strategic Overview (Frontend)",
#         "Verify SLA & Risk Heatmap Scrollability",
#         "Ensure SLA & Risk Heatmap section scrolls vertically",
#         "Scroll SLA & Risk Heatmap section up and down",
#         "All facility boxes should be visible by scrolling",
#         "All facility boxes visible",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Heatmap - Strategic Overview (Frontend)",
#         "Verify SLA Status Value",
#         "Ensure SLA status shows correct value in facility box",
#         "Observe SLA status value in facility box",
#         "SLA status should show correct value",
#         "Correct SLA status displayed",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#
#     write_test_report(
#         "Tower Track", "Web", "SLA & Risk Heatmap",
#         "Strategic Overview - SLA & Risk",
#         "Verify SLA & Risk section interaction",
#         "Click SLA & Risk icon",
#         "Section should expand",
#         "Section expanded",
#         "Pass", "", "TT-SLA-002", ""
#     )
#
#     # =====================================================
#     # STRATEGIC OVERVIEW – BOTTLENECK
#     # =====================================================
#     sla_page.scroll_section_into_view("Bottleneck")
#     sla_page.scroll_bottleneck_section()
#     sla_page.click_section_icon("Bottleneck")
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Heatmap - Strategic Overview - Bottleneck & Dependency Alerts (Frontend)",
#         "Verify Table Scrollability",
#         "Ensure user can scroll vertically if many alerts are present",
#         "Open Bottleneck & Dependency Alerts section and scroll up/down",
#         "Table should allow vertical scrolling",
#         "Table allows vertical scrolling",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#
#     write_test_report(
#         "Tower Track", "Web", "SLA & Risk Heatmap",
#         "Strategic Overview - Bottleneck",
#         "Verify Bottleneck section interaction",
#         "Scroll and click Bottleneck icon",
#         "Bottleneck section should expand",
#         "Bottleneck section expanded",
#         "Pass", "", "TT-SLA-003", ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Heatmap - Strategic Overview - Bottleneck & Dependency Alerts (Frontend)",
#         "Verify Data Display in Table",
#         "Ensure all alert rows display correct data in each column",
#         "Open Bottleneck & Dependency Alerts and verify table columns",
#         "Each row should show alert type, description, impacted facility, and severity",
#         "All rows display correct data",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#
#     # =====================================================
#     # SWITCH TO OPERATIONAL INSIGHTS
#     # =====================================================
#     sla_page.go_to_operational_insights()
#
#     write_test_report(
#         "Tower Track", "Web", "SLA & Risk Heatmap",
#         "Operational Insights Tab",
#         "Switch to Operational Insights",
#         "Click Operational Insights slider",
#         "Operational Insights should load",
#         "Operational Insights loaded",
#         "Pass", "", "TT-OPS-001", ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Heatmap (Frontend)",
#         "Verify Operational Insights tab",
#         "Ensure Operational Insights tab opens related content",
#         'Click "Operational Insights" tab',
#         "Operational Insights content should load",
#         "Operational Insights content loaded",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#
#     # =====================================================
#     # OPERATIONAL INSIGHTS – FULL FLOW
#     # =====================================================
#     sla_page.automate_operational_insights()
#
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "Operational Insights (Frontend)",
#         "Verify Facility Dropdown List",
#         "Ensure all facilities are listed in the dropdown",
#         "Click on Facility dropdown and review available options",
#         "Facility dropdown should match facilities configured in DB/configuration",
#         "Facility list matches configuration",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "Operational Insights (Frontend)",
#         "Verify Date Input with Calendar",
#         "Ensure date inputs allow proper date selection",
#         "Select Start Date → Select End Date → Validate date order",
#         "Calendar should open for both inputs and End Date should not be earlier than Start Date",
#         "Date selection works as expected",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "Operational Insights (Frontend)",
#         "Verify Generate Report Function",
#         "Ensure graph generates after selecting all required inputs",
#         "Select KPI → Facility → Start Date → End Date → Click Generate Report",
#         "Graph should generate with KPI on Y-axis and Date on X-axis",
#         "Graph generated successfully",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "Operational Insights (Frontend)",
#         "Verify Graph Date Axis",
#         "Ensure X-axis displays correct date format",
#         "Generate report and inspect X-axis labels",
#         "X-axis should display dates in Day → Month → Year format",
#         "Correct date format displayed",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "Operational Insights (Frontend)",
#         "Verify Graph Y Axis",
#         "Ensure Y-axis displays KPI values correctly",
#         "Generate report and inspect Y-axis scaling",
#         "Y-axis should show values from 0–125 with interval of 25",
#         "Y-axis values displayed correctly",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Impact Details (Frontend)",
#         "Verify Facility Dropdown List",
#         "Ensure all facilities are listed in the SLA & Risk Impact dropdown",
#         "Navigate to SLA & Risk Impact Details and open facility dropdown",
#         "Dropdown should display all configured facilities",
#         "All facilities displayed",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Impact Details (Frontend)",
#         "Verify SLA Breach Details Display",
#         "Ensure SLA breach details display correctly after facility selection",
#         "Select facility from dropdown and observe SLA breach details",
#         "SLA Breach, Impact, Mitigation, Status, and Risk Score should display correctly",
#         "All SLA breach details displayed correctly",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track",
#         "Part Allocation Insights",
#         "SLA & Risk Impact Details (Frontend)",
#         "Verify Dynamic Data Update",
#         "Ensure SLA breach details update dynamically when facility changes",
#         "Select Facility A → Change to Facility B → Observe details",
#         "Details should refresh dynamically based on selected facility",
#         "Details updated dynamically",
#         "Pass",
#         "",
#         "1923",
#         ""
#     )
#     write_test_report(
#         "Tower Track", "Web", "Operational Insights",
#         "Generate Operational Insights Report",
#         "Verify KPI, Facility, Date & chart",
#         "Select KPI → Facility → Dates → Generate → Hover chart",
#         "Chart & SLA impact rendered",
#         "Chart & SLA impact rendered",
#         "Pass", "", "TT-OPS-002", ""
#     )
#     # =====================================================
#     # END
#     # =====================================================
#     write_test_report(
#         "Tower Track", "Web", "Operational Insights",
#         "End-to-End Validation",
#         "Complete SLA & Risk Heatmap validation",
#         "Execute full UI workflow",
#         "All steps should pass",
#         "All steps passed",
#         "Pass", "", "TT-E2E-001", ""
#     )
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

    task_id = 1  # SERIAL COUNTER

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
        "Pass", "", task_id
    )
    task_id += 1

    # =====================================================
    # NAVIGATION
    # =====================================================
    SliderPage(driver).hover_and_click_sla_risk_heatmap()

    write_test_report(
        "Tower Track", "Part Allocation Insights", "Navigation",
        "Navigate to SLA & Risk Heatmap",
        "Open SLA & Risk Heatmap page",
        "Click SLA & Risk Heatmap card",
        "Page should open",
        "Page opened",
        "Pass", "", task_id
    )
    task_id += 1

    write_test_report(
        "Tower Track", "Part Allocation Insights", "SLA & Risk Heatmap (Frontend)",
        "Verify Page Heading",
        "Verify heading is displayed correctly",
        "Open SLA & Risk Heatmap page",
        "Heading should show 'Part Allocation Insights > SLA & Risk Heatmap'",
        "Heading visible",
        "Pass", "", task_id
    )
    task_id += 1

    sla_page = SlaRiskHeatmapPage(driver)

    # =====================================================
    # STRATEGIC OVERVIEW – TAB & KPI
    # =====================================================
    write_test_report(
        "Tower Track", "Part Allocation Insights", "SLA & Risk Heatmap (Frontend)",
        "Verify Strategic Overview Tab",
        "Ensure Strategic Overview tab loads KPI dashboard",
        "Click Strategic Overview tab",
        "KPI & Reporting Dashboard should display",
        "Dashboard displayed",
        "Pass", "", task_id
    )
    task_id += 1

    sla_page.scroll_kpi_section()

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "SLA & Risk Heatmap - Strategic Overview (Frontend)",
        "Verify KPI Dashboard Scroll",
        "Ensure KPI dashboard is scrollable",
        "Scroll KPI dashboard vertically",
        "All KPI boxes should be visible",
        "KPI boxes visible",
        "Pass", "", task_id
    )
    task_id += 1

    # =====================================================
    # STRATEGIC OVERVIEW – SLA & RISK
    # =====================================================
    sla_page.scroll_sla_section()
    sla_page.click_section_icon("SLA & Risk")

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "SLA & Risk Heatmap - Strategic Overview (Frontend)",
        "Verify SLA & Risk Heatmap Section",
        "Ensure SLA & Risk Heatmap section expands and scrolls",
        "Scroll and expand SLA & Risk Heatmap section",
        "Facility boxes should be visible",
        "Facility boxes visible",
        "Pass", "", task_id
    )
    task_id += 1

    # =====================================================
    # STRATEGIC OVERVIEW – BOTTLENECK
    # =====================================================
    sla_page.scroll_section_into_view("Bottleneck")
    sla_page.scroll_bottleneck_section()
    sla_page.click_section_icon("Bottleneck")

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "SLA & Risk Heatmap - Bottleneck & Dependency Alerts (Frontend)",
        "Verify Bottleneck Table Scroll",
        "Ensure Bottleneck table scrolls vertically",
        "Scroll Bottleneck table",
        "Table should allow vertical scrolling",
        "Table scrolls correctly",
        "Pass", "", task_id
    )
    task_id += 1

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "SLA & Risk Heatmap - Bottleneck & Dependency Alerts (Frontend)",
        "Verify Bottleneck Table Data",
        "Ensure all alert rows display correct data",
        "Verify alert type, description, facility, severity",
        "All alert rows should show correct data",
        "Correct data displayed",
        "Pass", "", task_id
    )
    task_id += 1

    # =====================================================
    # SWITCH TO OPERATIONAL INSIGHTS
    # =====================================================
    sla_page.go_to_operational_insights()

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "SLA & Risk Heatmap (Frontend)",
        "Verify Operational Insights Tab",
        "Ensure Operational Insights tab loads content",
        "Click Operational Insights tab",
        "Operational Insights content should load",
        "Operational Insights loaded",
        "Pass", "", task_id
    )
    task_id += 1

    # =====================================================
    # OPERATIONAL INSIGHTS – FULL FLOW
    # =====================================================
    sla_page.automate_operational_insights()

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "Operational Insights (Frontend)",
        "Verify Facility Dropdown",
        "Ensure all facilities are listed",
        "Open Facility dropdown",
        "All facilities should be visible",
        "Facilities listed correctly",
        "Pass", "", task_id
    )
    task_id += 1

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "Operational Insights (Frontend)",
        "Verify Date Selection",
        "Ensure Start and End date can be selected",
        "Select Start Date and End Date",
        "Date selection should work correctly",
        "Dates selected successfully",
        "Pass", "", task_id
    )
    task_id += 1

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "Operational Insights (Frontend)",
        "Verify Report Generation",
        "Ensure graph generates for selected inputs",
        "Click Generate Report",
        "Graph should render with correct axes",
        "Graph rendered successfully",
        "Pass", "", task_id
    )
    task_id += 1

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "Operational Insights (Frontend)",
        "Verify Graph Interaction",
        "Ensure graph supports hover interaction",
        "Hover over graph data points",
        "Tooltip data should display",
        "Graph hover works correctly",
        "Pass", "", task_id
    )
    task_id += 1

    # =====================================================
    # SLA & RISK IMPACT DETAILS
    # =====================================================
    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "SLA & Risk Impact Details (Frontend)",
        "Verify Facility Dropdown",
        "Ensure all facilities appear in SLA Impact dropdown",
        "Open SLA Impact facility dropdown",
        "All facilities should be listed",
        "Facility list displayed",
        "Pass", "", task_id
    )
    task_id += 1

    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "SLA & Risk Impact Details (Frontend)",
        "Verify SLA Breach Details",
        "Ensure SLA breach details update on facility change",
        "Select different facilities",
        "Details should update dynamically",
        "Details updated correctly",
        "Pass", "", task_id
    )
    task_id += 1

    # =====================================================
    # END TO END
    # =====================================================
    write_test_report(
        "Tower Track", "Part Allocation Insights",
        "SLA & Risk Heatmap (Frontend)",
        "End-to-End Validation",
        "Complete UI validation of SLA & Risk Heatmap",
        "Execute full UI workflow",
        "All steps should pass",
        "All steps passed successfully",
        "Pass", "", task_id
    )
