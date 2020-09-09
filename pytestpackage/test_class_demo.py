import pytest
from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("one_time_setup", "setup")
class TestClassDemo:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.abc = SomeClassToTest(10)

    def test_sum_method(self):
        result = self.abc.sum_number(10, 5)
        assert result == 25
