import pytest

from tests.conftest import User


@pytest.mark.check
def test_change_name(user: User):
    assert user.name == 'Iryna'


@pytest.mark.check
def test_change_second_name(user: User):
    assert user.second_name == 'Lipska'
