import math

"""
200, 333,  467
A: 533 bananas
"""


def f_nr_drumuri(nr_ban) -> int:
    cap_camila: int = 1000
    return math.ceil(nr_ban / 1000)


def nr_banane_max():
    nr_ban: int = 3000
    dist: int = 1000
    nr_drumuri_prev = 0
    for i in range(dist):
        nr_drumuri = f_nr_drumuri(nr_ban)
        if nr_drumuri != nr_drumuri_prev:
            print(
                f" change nr dr from : {nr_drumuri_prev} to {nr_drumuri} after {i} km and {nr_ban} left"
            )
            nr_drumuri_prev = nr_drumuri
        consum = 2 * nr_drumuri
        consum = consum - 1
        nr_ban = nr_ban - consum
        # print(i)
    return nr_ban


assert f_nr_drumuri(3000) == 3
assert f_nr_drumuri(1001) == 2
assert f_nr_drumuri(1000) == 1
assert f_nr_drumuri(999) == 1

nr_ban = nr_banane_max()
print(f" Nr banane : {nr_ban}")
print(f"A: 533 bananas : {533-nr_ban}")
