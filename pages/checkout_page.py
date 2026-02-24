from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def complete_checkout(self, fname, lname, zip_code):
        self.send_keys(self.FIRST_NAME, fname)
        self.send_keys(self.LAST_NAME, lname)
        self.send_keys(self.ZIP, zip_code)
        self.click(self.CONTINUE)
        self.click(self.FINISH)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)