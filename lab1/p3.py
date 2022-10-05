def solve(*args):
    s = 0

    for nr in args:
        s += nr

    return s


if __name__ == "__main__":
    print(solve(1, 2, 3, 4, 5, 100))
