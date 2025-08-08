from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import Page


class VerificationPage(Page):

    # PAGE_TITLE = (By.CSS_SELECTOR, ".page-title.off_plan")
    SALES_FILTER = (By.XPATH, "//*[@wized='saleStatusFilter']")
    # SALES_FILTER = (By.XPATH, "//div[text()='Out of Stock']") #MOBILE
    # HEADER = (By.XPATH, "//h1[text()=' {SUBSTR}']")

    def verify_url(self):
        self.wait_for_url_contains(*self, 'pricePer=unit&withDealBonus=false&handoverOnly=false&handoverMonths=1')

    def verify_sale_filters(self, value):
        SF = self.find_element(*self.SALES_FILTER)
        select = Select(SF)
        select.select_by_value(value)
