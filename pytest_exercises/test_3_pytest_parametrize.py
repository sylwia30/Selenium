import pytest

@pytest.mark.parametrize('wartosc, suma', [(5, 10), (2, 4)])
def test_dodawanie(wartosc, suma):
    assert wartosc + wartosc == suma