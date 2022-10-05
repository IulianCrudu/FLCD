a := read()
b := read()
while b:
    c := b
    b := a % b
    a := c

print("GCD is: ", a)
