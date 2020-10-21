from pages.login import LoginPage
from utilities.web_element_assert import element_is_displayed, element_is_equal_to_text


def test_product_details(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    inventory_item_page = inventory_page.actions.click_on_random_product()
    element_is_displayed(inventory_item_page.banner.cart_icon)
    element_is_displayed(inventory_item_page.banner.burger_button)
    element_is_displayed(inventory_item_page.product_title)
    element_is_displayed(inventory_item_page.product_image)
    element_is_displayed(inventory_item_page.product_description)
    element_is_displayed(inventory_item_page.product_price)
    element_is_displayed(inventory_item_page.back_button)
    element_is_displayed(inventory_item_page.add_to_cart_button)


def test_remove_button_displayed_for_product_already_added_in_inventory_page(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    inventory_item_page = inventory_page.actions.add_random_product_to_cart_and_open_details()
    element_is_displayed(inventory_item_page.remove_button)
    element_is_equal_to_text(inventory_item_page.remove_button, "REMOVE")


def test_go_back_from_inventory_item_page_to_inventory_page(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    inventory_item_page = inventory_page.actions.click_on_random_product()
    inventory_item_page.actions.click_on_back_button()
