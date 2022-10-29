from scanner import Scanner


if __name__ == "__main__":
    scanner = Scanner()
    try:
        scanner.scan_and_save("p1.txt", "p1.out")
        # scanner.scan_and_save("p2.txt", "p2.out")
        # scanner.scan_and_save("p3.txt", "p3.out")
        # scanner.scan_and_save("p1err.txt", "p1err.out")
        print("Lexically correct")
    except Exception as exc:
        print(exc)
