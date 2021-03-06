from pages.login import LoginPage
from utilities.web_element_assert import element_is_displayed, element_list_is_sorted_by_text_asc, \
    element_list_is_sorted_by_text_desc, element_list_is_sorted_by_price_asc,\
    element_list_is_sorted_by_price_desc, element_is_equal_to_text
from assertpy import assert_that


def test_left_menu(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    inventory_page.banner.actions.click_on_burger_button()
    element_is_displayed(inventory_page.banner.left_menu)


def test_sort_products_name_a_to_z(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    inventory_page.actions.select_sort_drop_down("Name (A to Z)")
    element_list_is_sorted_by_text_asc(inventory_page.product_list)


def test_sort_products_name_z_to_a(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    inventory_page.actions.select_sort_drop_down("Name (Z to A)")
    element_list_is_sorted_by_text_desc(inventory_page.product_list)


def test_sort_products_price_lower_to_high(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    inventory_page.actions.select_sort_drop_down("Price (low to high)")
    element_list_is_sorted_by_price_asc(inventory_page.product_list)


def test_sort_products_price_high_to_lower(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    inventory_page.actions.select_sort_drop_down("Price (high to low)")
    element_list_is_sorted_by_price_desc(inventory_page.product_list)


def test_add_product_to_cart(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    actual_cart_badge_number = inventory_page.banner.actions.get_cart_badge_number()
    product_information = inventory_page.actions.add_random_product_to_cart()
    element_is_equal_to_text(product_information["button"], "REMOVE")
    expected_cart_badge_number = inventory_page.banner.actions.get_cart_badge_number()
    assert_that(expected_cart_badge_number).is_greater_than(actual_cart_badge_number)
    cart_page = inventory_page.banner.actions.click_on_cart_icon()
    product_label = cart_page.actions.get_cart_items_label()
    product_price = cart_page.actions.get_cart_items_price()
    assert_that(product_information["name"]).is_equal_to(product_label[0])
    assert_that(product_information["price"]).is_equal_to(product_price[0])
