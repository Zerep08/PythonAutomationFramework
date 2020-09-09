import pytest


@pytest.yield_fixture()
def setup():
    print("Before every method")
    yield
    print("After every method")


@pytest.yield_fixture(scope='class')
def one_time_setup(browser, os_type):
    print("Before module")
    print(browser)
    yield
    print('After module')


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")



