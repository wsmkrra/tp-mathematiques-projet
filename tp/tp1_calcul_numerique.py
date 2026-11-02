"""TP1 - Calcul numerique et nombres flottants.

Les exemples sont volontairement courts : lancez ce fichier pour voir les résultats.
"""

from fractions import Fraction
import math
import sys


def presque_egaux(a, b, tolerance=1e-9):
    """Renvoie True si a et b sont proches à la tolérance choisie."""
    return math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance)


def nombre_de_chiffres(n):
    """Compte les chiffres de n avec des divisions par 10."""
    n = abs(n)
    nombre = 1
    while n >= 10:
        n = n // 10
        nombre += 1
    return nombre


def racine_heron(a):
    """Approche la racine carrée avec la méthode de Héron."""
    if a < 0:
        raise ValueError("Le nombre doit être positif.")
    if a == 0:
        return 0

    estimation = a
    while True:
        nouvelle_estimation = (estimation + a / estimation) / 2
        if abs(nouvelle_estimation - estimation) < 1e-12:
            return nouvelle_estimation
        estimation = nouvelle_estimation


def vers_binaire(n):
    """Convertit un entier positif en binaire sans utiliser bin()."""
    if n < 0:
        raise ValueError("Le nombre doit être positif.")
    if n == 0:
        return "0"

    resultat = ""
    while n > 0:
        chiffre = n % 2
        resultat = str(chiffre) + resultat
        n = n // 2
    return resultat


def epsilon_machine():
    """Trouve la plus petite petite valeur qui change 1.0."""
    epsilon = 1.0
    while 1.0 + epsilon / 2 != 1.0:
        epsilon = epsilon / 2
    return epsilon


def racines_naives(a, b, c):
    """Résout ax²+bx+c=0 avec la formule classique."""
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError("Il n'y a pas de racine réelle.")

    racine_delta = math.sqrt(delta)
    x1 = (-b - racine_delta) / (2 * a)
    x2 = (-b + racine_delta) / (2 * a)
    return x1, x2


def racines_stables(a, b, c):
    """Même calcul, avec une formule qui limite la perte de précision."""
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError("Il n'y a pas de racine réelle.")

    racine_delta = math.sqrt(delta)
    if racine_delta == 0:
        racine = -b / (2 * a)
        return racine, racine

    # Choisir le signe qui évite de soustraire deux nombres proches.
    if b >= 0:
        grande_racine = (-b - racine_delta) / (2 * a)
    else:
        grande_racine = (-b + racine_delta) / (2 * a)

    petite_racine = c / (a * grande_racine)
    return min(petite_racine, grande_racine), max(petite_racine, grande_racine)


def demonstrations():
    print("1. Division euclidienne")
    n = 2026
    diviseur = 7
    quotient = n // diviseur
    reste = n % diviseur
    print(quotient, reste, "recomposition :", quotient * diviseur + reste)

    print("\n2. Chiffres d'un entier")
    print(123456789 % 10, 123456789 // 10)
    print("Nombre de chiffres de 2026 :", nombre_de_chiffres(2026))

    print("\n3. Les flottants")
    print("0.1 + 0.2 =", 0.1 + 0.2)
    print("Egal à 0.3 ?", 0.1 + 0.2 == 0.3)
    print("Proche de 0.3 ?", presque_egaux(0.1 + 0.2, 0.3))
    total = 0.0
    for _ in range(1000):
        total += 0.1
    print("Mille additions de 0.1 :", total, "écart à 100 :", total - 100)

    print("\n4. Boucles et sommes")
    for i in range(1, 11):
        print("7 x", i, "=", 7 * i)
    total = 0
    for i in range(1, 101):
        total += i
    print("Somme par boucle :", total)
    print("Somme par formule :", 100 * 101 // 2)

    print("\n5. Méthode de Héron")
    print("Racine de 2 :", racine_heron(2), "valeur Python :", math.sqrt(2))

    print("\n6. Binaire et précision machine")
    print("37 en binaire :", vers_binaire(37))
    print("Epsilon trouvé :", epsilon_machine())
    print("Epsilon Python :", sys.float_info.epsilon)

    print("\n7. Formule quadratique")
    naive = racines_naives(1.0, -1e8, 1.0)
    stable = racines_stables(1.0, -1e8, 1.0)
    print("Racines naïves :", naive, "produit :", naive[0] * naive[1])
    print("Racines stables :", stable, "produit :", stable[0] * stable[1])

    print("\n8. Fractions exactes")
    total_exact = Fraction(0)
    for _ in range(1000):
        total_exact += Fraction(1, 10)
    print(total_exact, "égal à 100 ?", total_exact == 100)


if __name__ == "__main__":
    demonstrations()
