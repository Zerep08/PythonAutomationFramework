from pages.login import LoginPage
from utilities.web_element_assert import element_is_displayed, element_list_is_sorted_by_text_asc, \
    element_list_is_sorted_by_text_desc


def test_left_menu(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"]) \
                                       .click_on_burger_button()
    element_is_displayed(inventory_page.left_menu)


def test_sort_products_name_a_to_z(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"]) \
        .select_sort_drop_down("Name (A to Z)")
    element_list_is_sorted_by_text_asc(inventory_page.product_list)


def test_sort_products_name_z_to_a(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"]) \
        .select_sort_drop_down("Name (Z to A)")
    element_list_is_sorted_by_text_desc(inventory_page.product_list)
