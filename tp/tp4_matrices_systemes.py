"""TP4 - Matrices et systèmes linéaires."""

from fractions import Fraction
import math
import random
import time


def transposee(A):
    """Échange les lignes et les colonnes."""
    resultat = []
    for j in range(len(A[0])):
        nouvelle_ligne = []
        for i in range(len(A)):
            nouvelle_ligne.append(A[i][j])
        resultat.append(nouvelle_ligne)
    return resultat


def produit(A, B):
    """Multiplie deux matrices avec trois boucles."""
    lignes_A = len(A)
    colonnes_A = len(A[0])
    colonnes_B = len(B[0])

    if colonnes_A != len(B):
        raise ValueError("Les dimensions ne correspondent pas.")

    resultat = []
    for i in range(lignes_A):
        ligne = []
        for j in range(colonnes_B):
            somme = 0
            for k in range(colonnes_A):
                somme += A[i][k] * B[k][j]
            ligne.append(somme)
        resultat.append(ligne)
    return resultat


def resoudre(A, b, tolerance=1e-14):
    """Résout A*x=b avec le pivot de Gauss et un pivot partiel."""
    n = len(A)
    matrice = []

    # Copier A et ajouter b à droite pour former [A | b].
    for i in range(n):
        matrice.append(A[i][:] + [b[i]])

    # Élimination : rendre nuls les nombres sous la diagonale.
    for k in range(n):
        ligne_pivot = k
        for i in range(k + 1, n):
            if abs(matrice[i][k]) > abs(matrice[ligne_pivot][k]):
                ligne_pivot = i

        if abs(matrice[ligne_pivot][k]) <= tolerance:
            raise ValueError("Le système n'a pas de solution unique.")

        matrice[k], matrice[ligne_pivot] = matrice[ligne_pivot], matrice[k]

        for i in range(k + 1, n):
            facteur = matrice[i][k] / matrice[k][k]
            for j in range(k, n + 1):
                matrice[i][j] -= facteur * matrice[k][j]

    # Remontée : calculer les inconnues de la dernière à la première.
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        somme = matrice[i][n]
        for j in range(i + 1, n):
            somme -= matrice[i][j] * solution[j]
        solution[i] = somme / matrice[i][i]
    return solution


def determinant(A, tolerance=1e-14):
    """Calcule le déterminant par élimination de Gauss."""
    n = len(A)
    matrice = [ligne[:] for ligne in A]
    resultat = 1

    for k in range(n):
        ligne_pivot = k
        for i in range(k + 1, n):
            if abs(matrice[i][k]) > abs(matrice[ligne_pivot][k]):
                ligne_pivot = i

        if abs(matrice[ligne_pivot][k]) <= tolerance:
            return 0

        if ligne_pivot != k:
            matrice[k], matrice[ligne_pivot] = matrice[ligne_pivot], matrice[k]
            resultat = -resultat

        pivot = matrice[k][k]
        resultat *= pivot
        for i in range(k + 1, n):
            facteur = matrice[i][k] / pivot
            for j in range(k + 1, n):
                matrice[i][j] -= facteur * matrice[k][j]
    return resultat


def inverse(A, tolerance=1e-14):
    """Inverse une matrice avec Gauss-Jordan (exercice complémentaire)."""
    n = len(A)
    matrice = []
    for i in range(n):
        ligne = A[i][:] + [0] * n
        ligne[n + i] = 1
        matrice.append(ligne)

    for k in range(n):
        ligne_pivot = k
        for i in range(k + 1, n):
            if abs(matrice[i][k]) > abs(matrice[ligne_pivot][k]):
                ligne_pivot = i
        if abs(matrice[ligne_pivot][k]) <= tolerance:
            raise ValueError("La matrice n'est pas inversible.")
        matrice[k], matrice[ligne_pivot] = matrice[ligne_pivot], matrice[k]

        pivot = matrice[k][k]
        for j in range(2 * n):
            matrice[k][j] /= pivot

        for i in range(n):
            if i != k:
                facteur = matrice[i][k]
                for j in range(2 * n):
                    matrice[i][j] -= facteur * matrice[k][j]

    resultat = []
    for i in range(n):
        resultat.append(matrice[i][n:])
    return resultat


def hilbert(n):
    """Construit la matrice de Hilbert avec des flottants."""
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(1.0 / (i + j + 1))
        resultat.append(ligne)
    return resultat


def hilbert_exacte(n):
    """Même matrice avec des fractions exactes."""
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(Fraction(1, i + j + 1))
        resultat.append(ligne)
    return resultat


def rotation(angle):
    """Matrice 2x2 de rotation, angle en radians."""
    c = math.cos(angle)
    s = math.sin(angle)
    return [[c, -s], [s, c]]


def translation(tx, ty):
    """Matrice de translation en coordonnées homogènes."""
    return [[1, 0, tx], [0, 1, ty], [0, 0, 1]]


def rotation_h(angle):
    """Matrice de rotation en coordonnées homogènes."""
    c = math.cos(angle)
    s = math.sin(angle)
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]


def appliquer(T, point):
    """Applique une transformation homogène au point (x,y)."""
    x, y = point
    p = [x, y, 1]
    resultat = []
    for i in range(3):
        valeur = 0
        for j in range(3):
            valeur += T[i][j] * p[j]
        resultat.append(valeur)
    return resultat[0] / resultat[2], resultat[1] / resultat[2]


def demonstrations():
    print("1. Transposée et produit")
    print(transposee([[1, 2, 3], [4, 5, 6]]))
    A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
    identite = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("A fois identité :", produit(A, identite))

    print("\n2. Résolution d'un système")
    b = [2, -1, 8]
    x = resoudre(A, b)
    print("Solution :", x)
    print("A*x :", [sum(A[i][j] * x[j] for j in range(3)) for i in range(3)])

    print("\n3. Déterminant et inverse")
    print("Déterminant :", determinant(A))
    print("Première ligne de l'inverse :", inverse(A)[0])

    print("\n4. Matrices exactes")
    H = hilbert_exacte(12)
    second_membre = [sum(ligne) for ligne in H]
    print("Solution exacte :", resoudre(H, second_membre, tolerance=0))

    print("\n5. Rotation puis translation")
    T = translation(3, 1)
    R = rotation_h(math.pi / 2)
    print("Translation puis rotation :", appliquer(produit(R, T), (1, 0)))
    print("Rotation puis translation :", appliquer(produit(T, R), (1, 0)))

    print("\n6. Comparaison simple avec NumPy, si installé")
    try:
        import numpy as np
        matrice = np.array(A, dtype=float)
        debut = time.perf_counter()
        solution_numpy = np.linalg.solve(matrice, np.array(b, dtype=float))
        print("Temps NumPy :", time.perf_counter() - debut)
        print("Solution manuelle / NumPy :", x, solution_numpy)
        print("Condition de la matrice de Hilbert :", np.linalg.cond(np.array(hilbert(12))))
    except ImportError:
        print("NumPy n'est pas installé; les exercices en Python pur fonctionnent quand même.")


if __name__ == "__main__":
    demonstrations()
