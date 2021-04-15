import pytest

# 1. pomijanie testu @pytest.mark.skip


@pytest.mark.parametrize('wartosc, suma', [(5, 10), (2, 4)])
def test_dodawanie(wartosc, suma):
    assert wartosc + wartosc == suma


@pytest.mark.skip
@pytest.mark.parametrize('wartosc, roznica', [(5, 0), (2, 0)])
def test_odejmowanie(wartosc, roznica):
    assert wartosc - wartosc == roznica

# po uruchomieniu testów otrzymujemy output o pomięciu 2 testów metody test_odejmowanie()
# używany pomijanie testów np. kiedy są one dedykowane do konkretnego środowiska


# 2. oznaczanie testow failujacych @pytest.mark.xfail

@pytest.mark.xfail
@pytest.mark.parametrize('wartosc, iloczyn', [(5, 0), (2, 7)])
def test_iloczyn(wartosc, iloczyn):
    assert wartosc * wartosc == iloczyn

# @pytest.mark.xfail używamy w przypadkach kiedy wiemmy że jest błąd w aplikacji i test nie zakończy się sukcesem

# output wszystkich powyższych testów, uzywamy flagi -v:
# test_4_pomijanie_skipowanie_testow.py::test_dodawanie[5-10] PASSED                                                                                                                 [ 16%]
# test_4_pomijanie_skipowanie_testow.py::test_dodawanie[2-4] PASSED                                                                                                                  [ 33%]
# test_4_pomijanie_skipowanie_testow.py::test_odejmowanie[5-0] SKIPPED (unconditional skip)                                                                                          [ 50%]
# test_4_pomijanie_skipowanie_testow.py::test_odejmowanie[2-0] SKIPPED (unconditional skip)                                                                                          [ 66%]
# test_4_pomijanie_skipowanie_testow.py::test_iloczyn[5-0] XFAIL                                                                                                                     [ 83%]
# test_4_pomijanie_skipowanie_testow.py::test_iloczyn[2-7] XFAIL