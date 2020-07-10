from pythoncode.calc import Calculator
import pytest


def setup_module():
    print("模块级别setup")


def teardown_module():
    print("模块级别teardown")


def setup_function():
    print("函数级别setup")


def teardown_function():
    print("函数级别teardown")


@pytest.mark.add
def test_add4():
    cal = Calculator()
    assert cal.add(3, 4) == 7


class TestCalc:

    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def setup_method(self):
        print("方法的setup")

    def teardown_method(self):
        print("方法的teardown")

    @pytest.mark.add
    def test_add(self):
        cal = Calculator()
        assert cal.add(1, 1) == 2

    @pytest.mark.parametrize(("a", "b", "result"), [
        (1, 2, 3),
        (2, 3, 5),
        (5, 6, 11)
    ])
    @pytest.mark.add
    def test_add1(self, a, b, result):
        cal = Calculator()
        assert cal.add(a, b) == result

    @pytest.mark.div
    def test_div(self):
        cal = Calculator()
        assert cal.div(4, 2) == 2