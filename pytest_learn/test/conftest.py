
import pytest
import dev.Shape as Shape

# By keeping these in conftest file they are globalised.

@pytest.fixture
def test_rectangle():
    return Shape.Rectangle(20,30)

@pytest.fixture
def defered_rectangle():
    return Shape.Rectangle(10,20)