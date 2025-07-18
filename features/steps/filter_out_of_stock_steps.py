from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Filter by sales status of {value}')
def filter_out_of_stocks(context, value):
    context.app.verification_page.sale_filters(value)
