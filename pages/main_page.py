from pages.base_page import Page


class MainPage(Page):

    def open_main_page(self):
        self.open_url()
        self.driver.save_screenshot('screenshots/01_main_page.png')