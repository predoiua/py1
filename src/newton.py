"""
i1 = ( nr / i0 + i0 ) / 2

"""


def newton_sq(nr):
    epsilon = 0.00001
    guess = 1.0
    while True:
        next_quess = (nr / guess + guess) / 2
        if abs(next_quess - guess) < epsilon:
            return next_quess
        guess = next_quess


if __name__ == "__main__":
    print(newton_sq(2))
    print(newton_sq(3))
