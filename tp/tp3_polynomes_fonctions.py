Ex 1.1


def evaluer_naif(P, x):
    total = 0
    for i in range(len(P)):
        total += P[i] * x ** i
    return total

print(evaluer_naif([2, 3, 0, 5], 2))

Ex 2.1 (Horner, nécessite evaluer_naif de 1.1)


def evaluer(P, x):
    resultat = 0
    for c in reversed(P):
        resultat = resultat * x + c
    return resultat

print(evaluer([2, 3, 0, 5], 2))

P = [2, 3, 0, 5, -1, 4]
points = [-2, -1, 0, 1, 2, 3]
print(all(evaluer(P, x) == evaluer_naif(P, x) for x in points))

Ex 2.2 (nécessite evaluer_naif et evaluer)

Écrivez d’abord votre prévision dans une cellule Markdown, avant de lancer la mesure.


import time

def mesure(f, P, x, repet):
    debut = time.perf_counter()
    for _ in range(repet):
        f(P, x)
    return (time.perf_counter() - debut) / repet

for d in [1000, 5000, 20000]:
    P = [1] * (d + 1)
    repet = 200000 // d
    t1 = mesure(evaluer_naif, P, 1.0001, repet)
    t2 = mesure(evaluer, P, 1.0001, repet)
    print(d, f"naif {t1:.6f}  horner {t2:.6f}  rapport {t1 / t2:.2f}")

Ex 2.3 (nécessite mesure de 2.2)


for d in [200, 400, 800]:
    P = [1] * (d + 1)
    t1 = mesure(evaluer_naif, P, 3, 1000)
    t2 = mesure(evaluer, P, 3, 1000)
    print(d, f"naif {t1:.6f}  horner {t2:.6


Ex 3.1
def deriver(P):
    return [i * P[i] for i in range(1, len(P))]
print(deriver([2, 3, 0, 5]))   # [3, 0, 15]

Ex 4.1
def dichotomie(f, a, b, tolerance=1e-10):
    if f(a) * f(b) > 0:
        raise ValueError("pas de changement de signe")
    while b - a > tolerance:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2

def carre_moins_deux(x):
    return x * x - 2

print(dichotomie(carre_moins_deux, 0, 2))   # environ 1.414214

Ex 4.2 (nécessite evaluer et deriver)
Newton renvoie un couple (racine, nombre de tours), ce qui sert pour l’exercice 4.4.


def newton(P, depart, tolerance=1e-12, max_tours=50):
    x = depart
    dP = deriver(P)
    for tour in range(1, max_tours + 1):
        f = evaluer(P, x)
        df = evaluer(dP, x)
        if df == 0:
            raise ZeroDivisionError("dérivée nulle")
        suivant = x - f / df
        if abs(suivant - x) < tolerance:
            return suivant, tour
        x = suivant
    raise RuntimeError("pas de convergence")

racine, tours = newton([-5, -2, 0, 1], 2)
print(racine, tours)   # 2.0945514815... en 5 tours

Ex 4.3 (nécessite newton)


def trajet_newton(P, depart, n):
    x = depart
    dP = deriver(P)
    trajet = [x]
    for _ in range(n):
        x = x - evaluer(P, x) / evaluer(dP, x)
        trajet.append(x)
    return trajet

print(trajet_newton([2, -2, 0, 1], 0, 6))   # 0, 1, 0, 1, ... : ça oscille
try:
    newton([2, -2, 0, 1], 0)
except RuntimeError as e:
    print("erreur :", e)                    # pas de convergence

Ex 4.4 (nécessite newton)


print(newton([-5, -2, 0, 1], 0))   # 20 tours
print(newton([-5, -2, 0, 1], 2))   # 5 tours

Ex 5.1 (nécessite evaluer)
                                      
import matplotlib.pyplot as plt

Q = [-5, -2, 0, 1]          # x^3 - 2x - 5
xs = [i / 100 for i in range(-300, 301)]
ys = [evaluer(Q, x) for x in xs]

plt.figure()
plt.plot(xs, ys, label="x^3 - 2x - 5")
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.ylim(-20, 20)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend()
plt.title("Un polynome et son unique racine reelle")
plt.show()

Réponse à écrire : la courbe ne coupe l’axe qu’une seule fois, au point trouvé par Newton (≈ 2,0946). Les deux autres racines ne sont pas réelles : le discriminant vaut −4p³ − 27q² = −643 < 0, donc ce sont deux racines complexes conjuguées.

Ex 6.1

def somme(P, Q):
    n = max(len(P), len(Q))
    P2 = P + [0] * (n - len(P))
    Q2 = Q + [0] * (n - len(Q))
    return [p + q for p, q in zip(P2, Q2)]

def produit_poly(P, Q):
    R = [0] * (len(P) + len(Q) - 1)
    for i, p in enumerate(P):
        for j, q in enumerate(Q):
            R[i + j] += p * q
    return R

print(produit_poly([1, 1], [1, 1]))    # [1, 2, 1]
print(produit_poly([-1, 1], [1, 1]))   # [-1, 0, 1]

Ex 6.2 (nécessite produit_poly)

python
resultat = [1]
for _ in range(10):
    resultat = produit_poly(resultat, [1, 1])
print(resultat)   # [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

C’est la ligne 10 du triangle de Pascal (coefficients binomiaux).

Ex 7.1

import math

def derivee_avant(f, x, h):
    return (f(x + h) - f(x)) / h

def derivee_centree(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

exacte = math.cos(1)
for k in [1, 2, 4, 6, 8, 10, 12]:
    h = 10 ** (-k)
    e1 = abs(derivee_avant(math.sin, 1, h) - exacte)
    e2 = abs(derivee_centree(math.sin, 1, h) - exacte)
    print(f"h = 1e-{k:<2}  avant : {e1:.2e}   centree : {e2:.2e}")
