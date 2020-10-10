import pytest
from base.webdriver_wrapper import Driver


@pytest.yield_fixture()
def setup(request, browser):
    url = "https://www.saucedemo.com/"
    user_name = "standard_user"
    password = "secret_sauce"
    invalid_user_name = "locked_out_user"
    driver = Driver(browser)
    driver.get_web_driver().maximize_window()
    driver.go_to_url(url)
    yield {"Driver": driver, "UserName": user_name, "Password": password, "InvalidUser": invalid_user_name}


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    driver = request.node.funcargs['setup']['Driver']
    if request.node.rep_setup.failed:
        driver.quit()
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver.take_screenshot(request.node.nodeid)
            driver.quit()

        driver.quit()
