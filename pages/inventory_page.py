from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):


    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_product(self):
        self.click(self.ADD_TO_CART)   # ✅ correct

    def open_cart(self):
        self.click(self.CART_ICON)     # ✅ correct