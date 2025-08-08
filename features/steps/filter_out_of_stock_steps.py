from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Filter by sales status of {value}')
def filter_out_of_stocks(context, value):
    context.app.verification_page.verify_sale_filters(value)

@when ('Click Sale Status')
def click_sale_status(context):
    context.app.off_plan_page.sale_status_tab()


@when('Click Out of Stocks button')
def click_out_of_stocks(context):
    context.app.off_plan_page.click_out_of_stocks_button()

@then('Verify each product contains the Out of Stocks tag on mobile')
def verify_out_of_stocks(context):
    context.app.off_plan_page.verify_out_of_stocks_filter()
