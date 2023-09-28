def calc_num(num: float):
    return num + 100


def test_calc_num():
    assert calc_num(100) == 200.0
    assert calc_num(100) == 100
