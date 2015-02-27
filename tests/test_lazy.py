from larger import larger


@larger
def f(x, y=lambda x: x + 1, z=lambda y: y ** 2):
    """test function"""

    return x, y, z


def test_lazy_basic():
    """Test lazy invocation with only required arguments."""

    assert f(1) == (1, 2, 4)


def test_lazy_with_all_args():
    """Test invocation with all arguments specified."""

    assert f(1, 3, 5) == (1, 3, 5)
