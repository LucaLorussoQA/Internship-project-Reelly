from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

from pages.base_page import Page




class OffPlanPage(Page):

    OFF_PLAN_TXT = (By.XPATH,"//button[text()='Off-plan']")
    SALE_STATUS_TAB = (By.XPATH,"//button[text()='Sale Status']")
    OUT_OF_STOCK_FILTER_BUTTON = (By.XPATH, "//div[text()='Out of stock']")
    OUT_OF_STOCK_FILTER_BUTTON_MOBILE = (By.XPATH,"//div[text()='Out of Stock']")
    PRODUCT_STATUS_MOBILE = (By.XPATH, "//span[text()='Out of stock']")

    def sale_status_tab(self):
        self.wait_for_element_click(*self.SALE_STATUS_TAB)
        self.driver.save_screenshot("screenshots/05_sale_status_tab.png")


    def verify_off_plan_page_opened(self):
        self.verify_text("Off-plan",*self.OFF_PLAN_TXT)
        self.driver.save_screenshot("screenshots/04_off_plan_opened.png")

    def apply_out_of_stock_filter(self):
        self.click(*self.OUT_OF_STOCK_FILTER_BUTTON)
        self.wait_for_element_click()

    def click_out_of_stocks_button(self):
        self.click(*self.OUT_OF_STOCK_FILTER_BUTTON_MOBILE)

    def verify_out_of_stocks_filter(self):
        sleep(3)
        products = self.driver.find_elements(*self.PRODUCT_STATUS_MOBILE)
        for product in products[:317]:
            sleep(3)
            status = product.find_element(*self.PRODUCT_STATUS_MOBILE)
            assert status, 'Product status not shown'
            print(status)
