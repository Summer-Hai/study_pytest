from pythoncode.calc import Calculator
import pytest

class TestCalc:

    @pytest.mark.parametrize(("a","b","result"),[
        (1,2,3),
        (-1,2,1),
        (-1,-2,3),
        (0,0,0),
        (0.5,3,3.5)
    ])
    @pytest.mark.add
    def test_add(self,a,b,result,open):
        cal = Calculator()
        assert cal.add(a,b) == result

    @pytest.mark.parametrize(("a","b","result"), [
        (1, 2, 3),
        (-1, 2, 1),
        (-1, -2, 3),
        (0, 0, 0),
        (0.5, 3, 3.5),
        (1,0,0),
        (0,1,0)
    ])
    @pytest.mark.div
    def test_div(self,a,b,result,open):
        cal = Calculator()
        assert cal.div(a, b) == result

    @pytest.mark.parametrize(("a","b","result"), [
        (1, 2, 3),
        (-1, 2, 1),
        (-1, -2, 3),
        (0, 0, 0),
        (0.5, 3, 3.5),
        (1, 0, 0),
        (0, 1, 0)
    ])
    @pytest.mark.subtraction
    def test_subtraction(self,a,b,result,open):
        cal = Calculator()
        assert cal.subtraction(a, b) == result

    @pytest.mark.parametrize(("a","b","result"), [
        (1, 2, 3),
        (-1, 2, 1),
        (-1, -2, 3),
        (0, 0, 0),
        (0.5, 3, 3.5),
        (1, 0, 0),
        (0, 1, 0)
    ])
    @pytest.mark.multiplication
    def test_multiplication(self,a,b,result,open):
        cal = Calculator()
        assert cal.multiplication(a, b) == result
