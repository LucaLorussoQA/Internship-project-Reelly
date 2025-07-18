from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

from pages.base_page import Page




class OffPlanPage(Page):

    OFF_PLAN_TXT = (By.XPATH,"//button[text()='Off-plan']")
    SALE_STATUS_TAB = (By.XPATH,"//button[text()='Sale Status']")
    OUT_OF_STOCK_FILTER_BUTTON = (By.XPATH,"//*[@wized='saleStatusFilter']")

    def sale_status_tab(self):
        self.wait_for_element_click(*self.SALE_STATUS_TAB)
        self.driver.save_screenshot("screenshots/05_sale_status_tab.png")


    def verify_off_plan_page_opened(self):
        self.verify_text("Off-plan",*self.OFF_PLAN_TXT)
        self.driver.save_screenshot("screenshots/04_off_plan_opened.png")

    def apply_out_of_stock_filter(self):
        self.click(*self.OUT_OF_STOCK_FILTER_BUTTON)
        self.wait_for_element_click()