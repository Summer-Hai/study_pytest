from pythoncode.calc import Calculator

def test_add():
    cal = Calculator()
    assert cal.add(1,1) == 2