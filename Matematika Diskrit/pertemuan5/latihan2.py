def kuadrat(x):
    return x ** 2

# Menghitung f(0), f(1), f(2), f(-1), f(-2)
domain_test = [0, 1, 2, -1, -2]
hasil = {x: kuadrat(x) for x in domain_test}

for x, fx in hasil.items():
    print(f"f({x}) = {fx}")