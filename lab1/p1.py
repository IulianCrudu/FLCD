def solve(n1, n2, n3):
    m = n1

    if m < n2:
        m = n2

    if m < n3:
        m = n3

    return m


if __name__ == "__main__":
    print(solve(10, 5, 100))
