from pages.login import LoginPage


def test_left_menu(setup):
    login_page = LoginPage(setup["Driver"])
    login_page.actions.login(setup["UserName"], setup["Password"]) \
        .click_on_burger_button() \
        .left_menu_should_be_displayed()


def test_sort_products_name_a_to_z(setup):
    login_page = LoginPage(setup["Driver"])
    login_page.actions.login(setup["UserName"], setup["Password"]) \
        .select_sort_drop_down("Name (A to Z)")
