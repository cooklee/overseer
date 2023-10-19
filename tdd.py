import pytest


def prime_numbers(n):
    lst = []
    devider = 2
    while n > 1:
        while n % devider == 0:
            lst.append(devider)
            n = n // devider
        devider += 1
    return lst



@pytest.mark.parametrize('n, lst', [
    (1,[]),
    (2,[2]),
    (3,[3]),
    (4,[2,2]),
    (5,[5]),
    (6,[2,3]),
    (7,[7]),
    (8,[2,2,2]),
    (9,[3,3]),
    (2*2*2*2*3*3*5*7*11, [2,2,2,2,3,3,5,7,11]),
    (-6,[])
])
def test_prime_number(n,lst):
    assert prime_numbers(n) == lst