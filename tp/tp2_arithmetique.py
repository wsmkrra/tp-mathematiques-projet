def diviseurs(n):
    return [d for d in range(1, n + 1) if n % d == 0]

print(diviseurs(28))

Ex 2.1
def pgcd_naif(a, b):
    meilleur = 1
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            meilleur = d
    return meilleur

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(pgcd(1071, 462), pgcd_naif(1071, 462))
print(pgcd(1071, 462) == pgcd_naif(1071, 462))

Ex 3.1
import time

def est_premier_naif(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def est_premier(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def mesure(f, n, repet):
    debut = time.perf_counter()
    for _ in range(repet):
        f(n)
    return (time.perf_counter() - debut) / repet

print(f"{'n':>10} {'naif (s)':>12} {'racine (s)':>12}")
for n in [10007, 100003, 1000003]:
    t1 = mesure(est_premier_naif, n, 3)
    t2 = mesure(est_premier, n, 1000)
    print(f"{n:>10} {t1:>12.6f} {t2:>12.8f}")

# Réponse : la version naïve croît linéairement (temps ×10 quand n ×10),
# la version à racine carrée croît en racine de n (temps ×3 environ).

Ex 4.1 (nécessite est_premier de l’exercice 3.1)
import time

def crible(N):
    est = [True] * (N + 1)
    est[0] = est[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if est[i]:
            for j in range(i * i, N + 1, i):
                est[j] = False
    return [i for i in range(N + 1) if est[i]]

debut = time.perf_counter()
premiers = crible(100000)
print(len(premiers), time.perf_counter() - debut)

debut = time.perf_counter()
nb = sum(1 for n in range(100000) if est_premier(n))
print(nb, time.perf_counter() - debut)

Ex 5.1

import math

def facteurs(n):
    res = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            res.append(d)
            n //= d
        d += 1
    if n > 1:
        res.append(n)
    return res

print(facteurs(360))
print(math.prod(facteurs(360)))
