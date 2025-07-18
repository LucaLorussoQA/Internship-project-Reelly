from behave import then, when
from selenium.webdriver.common.by import By


@then('Verify the right page opens')
def verify_right_page(context):
    PAGE_TITLE = context.driver.find_element(By.CSS_SELECTOR, ".page-title.off_plan").text


@then('Verify each product contains the Out of Stocks tag')
def check_out_of_stock_tags(context):
  STATUS = context.driver.find_element(By.CSS_SELECTOR, "._5-comission")
