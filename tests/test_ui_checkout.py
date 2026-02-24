from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_order(setup):
    driver = setup

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.complete_checkout("John", "Doe", "12345")

    assert "Thank you" in checkout.get_success_message()