Ex 1.1

q, r = divmod(2026, 7)
print(q, r)
print(q * 7 + r)

Ex 1.2
print(123456789 % 10)
print(123456789 // 10)

Ex 2.1
s = 0
for _ in range(1000):
    s += 0.1
print(s)
print(100 - s)

Ex 2.2
def presque_egaux(a, b, tol=1e-9):
    return abs(a - b) < tol

print(presque_egaux(0.1 + 0.2, 0.3))
print(0.1 + 0.2 == 0.3)

Ex 3.1
for k in range(1, 11):
    print(f"7 x {k} = {7 * k}")

Ex 3.2
total = 0
for i in range(1, 101):
    total += i
print(total)
print(total == 100 * 101 // 2)

Ex 4.1
def nombre_de_chiffres(n):
    compte = 1
    while n >= 10:
        n //= 10
        compte += 1
    return compte

print(nombre_de_chiffres(2026))
print(nombre_de_chiffres(7))

Ex 5.1
import math

def heron(a, tol=1e-12):
    x = a
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < tol:
            return y
        x = y

print(heron(2))
print(abs(heron(2) - math.sqrt(2)))

Ex 6.1
def vers_binaire(n):
    if n == 0:
        return "0"
    chiffres = ""
    while n > 0:
        chiffres = str(n % 2) + chiffres
        n //= 2
    return chiffres

print(vers_binaire(37))
print(vers_binaire(0))

Ex 6.2

import sys

eps = 1.0
while 1.0 + eps / 2 != 1.0:
    eps /= 2
print(eps)
print(sys.float_info.epsilon)

Ex 7.1

python
import math

def racines_naif(a, b, c):
    delta = b**2 - 4 * a * c
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    return r1, r2

r1, r2 = racines_naif(1, -1e8, 1)
print(r1, r2)
print(r1 * r2)

