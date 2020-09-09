import pytest


@pytest.mark.run(order=2)
def test_method_a(one_time_setup, setup):
    print("Hello")


@pytest.mark.run(order=1)
def test_method_b(one_time_setup, setup):
    print("World")
