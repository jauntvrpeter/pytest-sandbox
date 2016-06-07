import pytest

@pytest.mark.smoke
def test_hello_world1():
    pass

def not_a_test():
    pass

@pytest.mark.smoke
@pytest.mark.foobar
def test_hello_world2():
    pass

def test_hello_world3():
    pass

def test_some_hello_world_test():
    pass
