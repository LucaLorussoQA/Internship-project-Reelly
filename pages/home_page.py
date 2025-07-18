from selenium.webdriver.common.by import By

from pages.base_page import Page


class HomePage(Page):

    # MENU_OFF_PLAN = (By.CSS_SELECTOR, '.menu-off-plan')
    OFF_PLAN_TAB = (By.CSS_SELECTOR, "[wized='newOffPlanLink']")
    SECONDARY_TAB = (By.CSS_SELECTOR, ".text-sm.font-semibold")
    BACK_OFF_PLAN_TAB = (By.ID, "w-node-bf44e609-bef9-12ba-bb17-9e5d5d1e09d0-7f66df43")

    def off_plan_tab(self):
        self.wait_for_element_click(*self.OFF_PLAN_TAB)
        self.wait_for_element_click(*self.SECONDARY_TAB)
        self.wait_for_element_click(*self.BACK_OFF_PLAN_TAB)
        self.driver.save_screenshot("screenshots/03_off_plan_tab.png")