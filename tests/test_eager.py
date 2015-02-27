from larger import larger


@larger
def f(x, y=2, z=3):

    return x, y, z


def test_eager_basic():
    """Test basic invocation with only eager arguments."""

    assert f(1) == (1, 2, 3)


def test_eager_with_args():
    """Test invocation with keyword arguments specified."""

    assert f(1, 3, 5) == (1, 3, 5)
