from itertools import permutations

# Unique letters
letters = ('E', 'A', 'T', 'H', 'P', 'L')

# Try all possible assignments
for p in permutations(range(10), len(letters)):
    E, A, T, H, P, L = p

    # Leading letters cannot be zero
    if E == 0 or T == 0 or A == 0:
        continue

    # Form the numbers
    EAT = 100 * E + 10 * A + T
    THAT = 1000 * T + 100 * H + 10 * A + T
    APPLE = 10000 * A + 1000 * P + 100 * P + 10 * L + E

    # Check the equation
    if EAT + THAT == APPLE:
        print("Solution Found!")
        print("----------------")
        print("E =", E)
        print("A =", A)
        print("T =", T)
        print("H =", H)
        print("P =", P)
        print("L =", L)
        print()
        print("EAT   =", EAT)
        print("THAT  =", THAT)
        print("APPLE =", APPLE)
        break