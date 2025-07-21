from selenium.webdriver.common.by import By
from behave import given, then, when
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_STATUS = (By.XPATH,"//div[text()='Out of stock']")
LISTINGS = (By.XPATH, "//a[@wized='cardOfProperty']")
PRODUCT_IMG = (By.CSS_SELECTOR, '.project-image')

@then('Verify the right page opens')
def verify_right_page(context):
    PAGE_TITLE = context.driver.find_element(By.CSS_SELECTOR, ".page-title.off_plan").text


@then('Verify each product contains the Out of Stocks tag')
def verify_out_of_stock_filter(context):

    sleep(3)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(3)

    products = context.driver.find_elements(*LISTINGS)

    for product in products [:24]:
        status = product.find_element(*PRODUCT_STATUS)
        assert status, 'Product status not shown'
        print(status)
        product.find_element(*PRODUCT_IMG)


