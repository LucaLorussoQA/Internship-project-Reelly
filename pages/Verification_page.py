from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import Page


class VerificationPage(Page):
    # PAGE_TITLE = (By.CSS_SELECTOR, ".page-title.off_plan")
    SALES_FILTER = (By.XPATH, "//*[@wized='saleStatusFilter']")
    # HEADER = (By.XPATH, "//h1[text()=' {SUBSTR}']")
    # OUT_OF_STOCK_FILTER = (By.CSS_SELECTOR, "//*[@wized='saleStatusFilter']")

    def verify_url(self):
        self.wait_for_url_contains(*self, 'pricePer=unit&withDealBonus=false&handoverOnly=false&handoverMonths=1')

    def sale_filters(self, value):
        SF = self.find_element(*self.SALES_FILTER)
        select = Select(SF)
        select.select_by_value(value)








# 1 def _get_header_locator(self, expected_text):
#         return [self.HEADER[0], self.HEADER[1].replace('{SUBSTR}', expected_text)]

# 1 def filter_sale(self, expected_text):
#         locator = self._get_header_locator(expected_text)
#         self.wait_for_element(*locator)

    # def apply_filters(self):
    #     self.click(*self.OUT_OF_STOCK_FILTER)


        # def wait_for_page_to_visible(self, expected_text):
    #     element = self.wait_for_page_to_visible(*self.PAGE_TITLE)
    #     return expected_text in element.text
    #
