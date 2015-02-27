import pytest

from larger import larger


@larger
def f(x, y=lambda z: z + 1, z=lambda y: y ** 2):
    """test function"""

    return x, y, z


def test_lazy_basic():
    """Test invocation with only required arguments."""

    with pytest.raises(ValueError) as e:
        f(1)

    assert str(e.value) == "Unable to resolve input for 'y': 'z'"
