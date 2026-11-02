"""TP2 - Arithmétique et nombres premiers."""

import time


def diviseurs(n):
    """Renvoie les diviseurs positifs de n."""
    resultat = []
    for d in range(1, n + 1):
        if n % d == 0:
            resultat.append(d)
    return resultat


def pgcd_naif(a, b):
    """Cherche le PGCD en essayant tous les entiers possibles."""
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    meilleur = 1
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            meilleur = d
    return meilleur


def pgcd(a, b):
    """Calcule le PGCD avec l'algorithme d'Euclide."""
    a = abs(a)
    b = abs(b)
    while b != 0:
        reste = a % b
        a = b
        b = reste
    return abs(a)


def est_premier_naif(n):
    """Teste si n est premier en essayant tous les diviseurs."""
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def est_premier(n):
    """Teste les diviseurs jusqu'à la racine carrée de n."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def crible(limite):
    """Renvoie tous les nombres premiers jusqu'à limite."""
    est_premier_tab = [True] * (limite + 1)
    if limite >= 0:
        est_premier_tab[0] = False
    if limite >= 1:
        est_premier_tab[1] = False

    d = 2
    while d * d <= limite:
        if est_premier_tab[d]:
            multiple = d * d
            while multiple <= limite:
                est_premier_tab[multiple] = False
                multiple += d
        d += 1

    resultat = []
    for n in range(limite + 1):
        if est_premier_tab[n]:
            resultat.append(n)
    return resultat


def facteurs_premiers(n):
    """Décompose n en facteurs premiers, avec répétitions."""
    resultat = []
    diviseur = 2
    while diviseur * diviseur <= n:
        while n % diviseur == 0:
            resultat.append(diviseur)
            n = n // diviseur
        diviseur += 1
    if n > 1:
        resultat.append(n)
    return resultat


def fibonacci_recursif(n):
    """Version simple mais lente de Fibonacci."""
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)


def fibonacci(n):
    """Version rapide de Fibonacci avec une boucle."""
    precedent = 0
    courant = 1
    for _ in range(n):
        precedent, courant = courant, precedent + courant
    return precedent


def euclide_etendu(a, b):
    """Renvoie g,u,v tels que a*u + b*v = g = pgcd(a,b)."""
    if b == 0:
        return a, 1, 0
    g, u, v = euclide_etendu(b, a % b)
    return g, v, u - (a // b) * v


def puissance_modulaire(a, exposant, modulo):
    """Calcule a puissance exposant modulo modulo, sans grand nombre intermédiaire."""
    resultat = 1
    a = a % modulo
    while exposant > 0:
        if exposant % 2 == 1:
            resultat = (resultat * a) % modulo
        a = (a * a) % modulo
        exposant = exposant // 2
    return resultat


def temps_de_vol_syracuse(n):
    """Compte les étapes de Syracuse jusqu'à 1."""
    etapes = 0
    while n != 1 and etapes < 10_000:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        etapes += 1
    if n != 1:
        raise ValueError("Le nombre d'étapes maximal est atteint.")
    return etapes


def puissance_modulaire_naive(a, exposant, modulo):
    """Version lente : multiplie a exposant fois."""
    resultat = 1
    for _ in range(exposant):
        resultat = (resultat * a) % modulo
    return resultat


def demonstrations():
    print("1. Diviseurs")
    print(diviseurs(28))

    print("\n2. PGCD")
    print("Naïf et Euclide :", pgcd_naif(1071, 462), pgcd(1071, 462))

    print("\n3. Nombres premiers")
    print("97 :", est_premier(97), "91 :", est_premier(91))
    for n in (10_007, 100_003, 1_000_003):
        debut = time.perf_counter()
        est_premier_naif(n)
        temps_naif = time.perf_counter() - debut
        debut = time.perf_counter()
        est_premier(n)
        temps_rapide = time.perf_counter() - debut
        print(n, "naïf :", temps_naif, "rapide :", temps_rapide)

    print("\n4. Crible")
    premiers = crible(100_000)
    print("Nombre de premiers jusqu'à 100000 :", len(premiers))

    print("\n5. Factorisation")
    facteurs = facteurs_premiers(360)
    produit = 1
    for facteur in facteurs:
        produit *= facteur
    print(facteurs, "produit :", produit)

    print("\n6. Fibonacci")
    for n in (20, 25, 30):
        debut = time.perf_counter()
        fibonacci_recursif(n)
        print("Temps récursif pour", n, ":", time.perf_counter() - debut)
    print("F(10000) contient", len(str(fibonacci(10_000))), "chiffres")

    print("\n7. Calcul modulo")
    g, u, v = euclide_etendu(1071, 462)
    print("Euclide étendu :", g, u, v, "vérification :", 1071 * u + 462 * v)
    print("7 puissance 100000 modulo 1000003 :",
          puissance_modulaire(7, 100_000, 1_000_003))
    print("Syracuse de 27, nombre d'étapes :", temps_de_vol_syracuse(27))
    plus_long_depart = 1
    plus_long_vol = 0
    for depart in range(1, 10_000):
        vol = temps_de_vol_syracuse(depart)
        if vol > plus_long_vol:
            plus_long_depart = depart
            plus_long_vol = vol
    print("Vol le plus long sous 10000 :", plus_long_depart, plus_long_vol)
    print("Puissance modulo naïve / rapide :",
          puissance_modulaire_naive(7, 100_000, 1_000_003),
          puissance_modulaire(7, 100_000, 1_000_003))


if __name__ == "__main__":
    demonstrations()
