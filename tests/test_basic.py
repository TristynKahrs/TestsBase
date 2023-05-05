import pytest


def test_valid():
    assert 1 / 1 == 1


@pytest.mark.parametrize("test_input", [
    (0),
    (1),
    (2)
])
def test_parametrized(test_input):
    assert test_input == test_input


@pytest.mark.skip(reason="reason")
def test_skip():
    assert 1 / 0 == 1


@pytest.mark.xfail
def test_expected_fail():
    assert 1 / 0 == 1


def test_invalid():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
