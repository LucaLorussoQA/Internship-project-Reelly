from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class HomePage(Page):


    # OFF_PLAN_TAB = (By.CSS_SELECTOR, "[wized='newOffPlanLink']")
    OFF_PLAN_TAB = (By.CSS_SELECTOR, '.div-block-121')  # FIREFOX LOCATOR .div-block-121   .lucide.lucide-house
    # SECONDARY_TAB = (By.CSS_SELECTOR, ".text-sm.font-semibold")
    SECONDARY_TAB = (By.CSS_SELECTOR, ".pb-5.text-sm.font-semibold.transition-all.border-b-2.border-transparent.whitespace-nowrap.text-muted-foreground") # FIREFOX LOCATOR
    BACK_OFF_PLAN_TAB = (By.ID, "w-node-bf44e609-bef9-12ba-bb17-9e5d5d1e09d0-7f66df43")
    # BACK_OFF_PLAN_TAB = (By.CSS_SELECTOR, ".pb-5.text-sm.transition-all.border-b-2.whitespace-nowrap.font-bold.border-foreground") # FIREFOX LOCATOR


    def off_plan_tab(self):
        # self.wait_for_element_click(*self.OFF_PLAN_TAB)
        sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.OFF_PLAN_TAB)).click()
        sleep(2)#FIREFOX
        self.wait_for_element_click(*self.SECONDARY_TAB)
        sleep(3)
        self.wait_for_element_click(*self.BACK_OFF_PLAN_TAB)
        sleep(2)


        self.driver.save_screenshot("screenshots/03_off_plan_tab.png")