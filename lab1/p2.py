def solve(a, b):
    while b:
        c = b
        b = a % b
        a = c

    return a


if __name__ == "__main__":
    print(solve(100, 40))
