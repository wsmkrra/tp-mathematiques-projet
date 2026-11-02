"""TP3 - Polynômes, racines et calcul numérique."""

import math
import time


def evaluer_naif(P, x):
    """Calcule P(x) terme par terme."""
    resultat = 0
    for i in range(len(P)):
        resultat += P[i] * x ** i
    return resultat


def evaluer(P, x):
    """Calcule P(x) avec le schéma de Horner."""
    resultat = 0
    for coefficient in reversed(P):
        resultat = resultat * x + coefficient
    return resultat


def deriver(P):
    """Renvoie les coefficients de la dérivée."""
    resultat = []
    for i in range(1, len(P)):
        resultat.append(i * P[i])
    return resultat


def dichotomie(f, a, b, tolerance=1e-12):
    """Cherche une racine entre a et b si les signes sont différents."""
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if f(a) * f(b) > 0:
        raise ValueError("Les valeurs aux bornes doivent avoir des signes différents.")

    while b - a > tolerance:
        milieu = (a + b) / 2
        if f(a) * f(milieu) <= 0:
            b = milieu
        else:
            a = milieu
    return (a + b) / 2


def newton(P, depart, tolerance=1e-12):
    """Cherche une racine de P par la méthode de Newton."""
    derivee = deriver(P)
    x = depart
    for _ in range(100):
        valeur = evaluer(P, x)
        pente = evaluer(derivee, x)
        if pente == 0:
            raise ValueError("La dérivée est nulle.")
        nouveau_x = x - valeur / pente
        if abs(nouveau_x - x) < tolerance:
            return nouveau_x
        x = nouveau_x
    raise ValueError("La méthode de Newton n'a pas convergé.")


def trajet_newton(P, depart, nombre_etapes):
    """Montre les premiers x obtenus par Newton, même s'ils oscillent."""
    derivee = deriver(P)
    x = depart
    trajet = [x]
    for _ in range(nombre_etapes):
        pente = evaluer(derivee, x)
        if pente == 0:
            break
        x = x - evaluer(P, x) / pente
        trajet.append(x)
    return trajet


def somme_polynomes(P, Q):
    """Additionne deux polynômes dont les coefficients sont des listes."""
    resultat = []
    longueur = max(len(P), len(Q))
    for i in range(longueur):
        a = P[i] if i < len(P) else 0
        b = Q[i] if i < len(Q) else 0
        resultat.append(a + b)
    return resultat


def produit_polynomes(P, Q):
    """Multiplie deux polynômes."""
    if len(P) == 0 or len(Q) == 0:
        return []
    resultat = [0] * (len(P) + len(Q) - 1)
    for i in range(len(P)):
        for j in range(len(Q)):
            resultat[i + j] += P[i] * Q[j]
    return resultat


def derivee_avant(f, x, h):
    return (f(x + h) - f(x)) / h


def derivee_centree(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def rectangles(f, a, b, n):
    h = (b - a) / n
    somme = 0
    for i in range(n):
        somme += f(a + i * h)
    return h * somme


def trapezes(f, a, b, n):
    h = (b - a) / n
    somme = (f(a) + f(b)) / 2
    for i in range(1, n):
        somme += f(a + i * h)
    return h * somme


def simpson(f, a, b, n):
    """La méthode de Simpson demande un nombre pair de morceaux."""
    if n % 2 != 0:
        raise ValueError("n doit être pair.")
    h = (b - a) / n
    somme = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            somme += 2 * f(a + i * h)
        else:
            somme += 4 * f(a + i * h)
    return h * somme / 3


def tracer_polynome(P):
    """Trace P. Installer matplotlib pour utiliser cette fonction."""
    import matplotlib.pyplot as plt

    x = []
    y = []
    for i in range(-300, 301):
        valeur_x = i / 100
        x.append(valeur_x)
        y.append(evaluer(P, valeur_x))
    plt.plot(x, y)
    plt.axhline(0, color="black")
    plt.grid(True)
    plt.show()


def demonstrations():
    P = [2, 3, 0, 5]
    print("1. Polynôme évalué en 2 :", evaluer_naif(P, 2), evaluer(P, 2))
    print("Dérivée :", deriver(P))

    print("\n2. Racines")
    racine = dichotomie(lambda x: x * x - 2, 0, 2)
    print("Racine de 2 par dichotomie :", racine)
    Q = [-5, -2, 0, 1]
    print("Racine de x^3-2x-5 par Newton :", newton(Q, 2))
    print("Newton peut osciller :", trajet_newton([2, -2, 0, 1], 0, 8))

    print("\n3. Addition et multiplication")
    print(somme_polynomes([1, 2], [3, 4, 5]))
    print(" (1+x)^2 :", produit_polynomes([1, 1], [1, 1]))

    print("\n4. Dérivée numérique de sin(1)")
    exacte = math.cos(1)
    for h in (1e-2, 1e-4, 1e-6, 1e-8):
        avant = derivee_avant(math.sin, 1, h)
        centree = derivee_centree(math.sin, 1, h)
        print(h, "erreurs :", abs(avant - exacte), abs(centree - exacte))

    print("\n5. Intégrale de x² entre 0 et 1 (valeur exacte : 1/3)")
    for n in (10, 100, 1000):
        f = lambda x: x * x
        print(n, rectangles(f, 0, 1, n), trapezes(f, 0, 1, n), simpson(f, 0, 1, n))

    print("\n6. Temps de calcul : Horner et méthode naïve")
    P = [1] * 1001
    debut = time.perf_counter()
    evaluer_naif(P, 1.0001)
    temps_naif = time.perf_counter() - debut
    debut = time.perf_counter()
    evaluer(P, 1.0001)
    temps_horner = time.perf_counter() - debut
    print("Naïf :", temps_naif, "Horner :", temps_horner)


if __name__ == "__main__":
    demonstrations()
