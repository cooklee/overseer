from datetime import datetime

import pytest


def add(a, b):
    return a + b


def sqrt(x):
    if x < 0:
        raise ValueError('nie ma pierwiastkow z liczb < od zera \n'
                         'a przynajmnie nie do studiów')
    return x


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 == 1 else "female"
    month = int(pesel[2:4])
    day = pesel[4:6]
    year = pesel[0: 2]
    years = ['19','20','21','22','18']
    prefix = years[month//20]
    month = month % 20
    year = int(prefix + year)
    birth_date = datetime(year, int(month), int(day))
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result


@pytest.mark.parametrize("x, y, result", [
    (1, 1, 2),
    (0, 0, 0),
    (2, 2, 4),
    (-2, 2, 0),
    (-2, -2, -4),
    (5, 5, 10),
    (100, 100, 200),
])
def test_add(x, y, result):
    assert add(x, y) == result


def test_squr_raise_exep():
    with pytest.raises(ValueError) as vr:
        sqrt(-1)
    datetime(1, 2, 3)


men_pesel = """
61051736733
52030448994
64071222734
52020175295
89051675496
""".split()

women_pesel = """
82112059521
71080734369
07311241586
52030655189
54101452369
""".split()


def test_analyze_pesel_pesel():
    for pesel in men_pesel + women_pesel:
        assert analyze_pesel(pesel)['pesel'] == pesel


def test_analyze_pesel_valid():
    for pesel in men_pesel + women_pesel:
        assert analyze_pesel(pesel)['valid']


def test_analyze_pesel_invalid():
    for pesel in men_pesel + women_pesel:
        pesel = pesel[:-1] + '8'
        assert not analyze_pesel(pesel)['valid']


def test_analyze_pesel_genre_men():
    for pesel in men_pesel:
        assert analyze_pesel(pesel)['gender'] == 'male'


def test_analyze_pesel_genre_women():
    for pesel in women_pesel:
        assert analyze_pesel(pesel)['gender'] == 'female'


@pytest.mark.parametrize('pesel, date', [
    ('61051736733', datetime(1961, 5, 17)),
    ('52030448994', datetime(1952, 3, 4)),
    ('64071222734', datetime(1964, 7, 12)),
    ('52020175295', datetime(1952, 2, 1)),
    ('89051675496', datetime(1989, 5, 16)),
    ('82112059521', datetime(1982, 11, 20)),
    ('71080734369', datetime(1971, 8, 7)),
    ('07311241586', datetime(2007, 11, 12)),
    ('52030655189', datetime(1952, 3, 6)),
    ('54101452369', datetime(1954, 10, 14)),
])
def test_analyze_pesel_birth_date(pesel, date):
    assert analyze_pesel(pesel)['birth_date'] == date
