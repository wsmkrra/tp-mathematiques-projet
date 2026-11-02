"""TP6 - Géométrie du plan."""

import math
import random


def vecteur(A, B):
    return B[0] - A[0], B[1] - A[1]


def produit_scalaire(u, v):
    return u[0] * v[0] + u[1] * v[1]


def norme(u):
    return math.sqrt(u[0] * u[0] + u[1] * u[1])


def angle(u, v):
    """Angle entre deux vecteurs, en degrés."""
    if norme(u) == 0 or norme(v) == 0:
        raise ValueError("L'angle d'un vecteur nul n'est pas défini.")
    cosinus = produit_scalaire(u, v) / (norme(u) * norme(v))
    cosinus = max(-1, min(1, cosinus))
    return math.degrees(math.acos(cosinus))


def determinant(u, v):
    """Déterminant 2x2 : son signe indique le sens du virage."""
    return u[0] * v[1] - u[1] * v[0]


def distance_point_droite(P, A, B):
    AB = vecteur(A, B)
    AP = vecteur(A, P)
    if norme(AB) == 0:
        raise ValueError("A et B doivent être deux points différents.")
    return abs(determinant(AB, AP)) / norme(AB)


def orientation(A, B, C):
    """1 si le virage est à gauche, -1 à droite, 0 si aligné."""
    valeur = determinant(vecteur(A, B), vecteur(A, C))
    if abs(valeur) < 1e-12:
        return 0
    if valeur > 0:
        return 1
    return -1


def aire(polygone):
    """Aire d'un polygone avec la formule du lacet."""
    somme = 0
    for i in range(len(polygone)):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % len(polygone)]
        somme += x1 * y2 - x2 * y1
    return abs(somme) / 2


def se_coupent(A, B, C, D):
    """Teste si deux segments se croisent franchement."""
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)
    return o1 * o2 < 0 and o3 * o4 < 0


def intersection(A, B, C, D):
    """Renvoie le point de croisement, ou None si les segments ne se croisent pas."""
    if not se_coupent(A, B, C, D):
        return None

    AB = vecteur(A, B)
    CD = vecteur(C, D)
    AC = vecteur(A, C)
    t = determinant(AC, CD) / determinant(AB, CD)
    return A[0] + t * AB[0], A[1] + t * AB[1]


def point_sur_segment(P, A, B):
    """Vérifie simplement si P est sur le segment [AB]."""
    AB = vecteur(A, B)
    AP = vecteur(A, P)
    if abs(determinant(AB, AP)) > 1e-10:
        return False
    return (min(A[0], B[0]) <= P[0] <= max(A[0], B[0])
            and min(A[1], B[1]) <= P[1] <= max(A[1], B[1]))


def dedans(P, polygone):
    """Décide si P est dans un polygone avec le lancer de rayon."""
    dedans_polygone = False

    for i in range(len(polygone)):
        A = polygone[i]
        B = polygone[(i + 1) % len(polygone)]

        # On choisit de compter le bord comme faisant partie du polygone.
        if point_sur_segment(P, A, B):
            return True

        y_encadre = (A[1] > P[1]) != (B[1] > P[1])
        if y_encadre:
            x_croisement = A[0] + (P[1] - A[1]) * (B[0] - A[0]) / (B[1] - A[1])
            if x_croisement > P[0]:
                dedans_polygone = not dedans_polygone

    return dedans_polygone


def aire_au_hasard(polygone, nombre_points=200_000):
    """Estime l'aire de la maison dans le rectangle [0,2] x [0,2.5]."""
    generateur = random.Random(1)
    points_dedans = 0

    for _ in range(nombre_points):
        x = generateur.uniform(0, 2)
        y = generateur.uniform(0, 2.5)
        if dedans((x, y), polygone):
            points_dedans += 1

    aire_rectangle = 2 * 2.5
    return aire_rectangle * points_dedans / nombre_points


def zone_de(P, zones):
    """Renvoie le numéro de la première zone qui contient P."""
    for i in range(len(zones)):
        if dedans(P, zones[i]):
            return i
    return None


def enveloppe(points):
    """Construit l'enveloppe convexe d'une liste de points."""
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    bas = []
    for point in points:
        while len(bas) >= 2 and orientation(bas[-2], bas[-1], point) <= 0:
            bas.pop()
        bas.append(point)

    haut = []
    for point in reversed(points):
        while len(haut) >= 2 and orientation(haut[-2], haut[-1], point) <= 0:
            haut.pop()
        haut.append(point)

    return bas[:-1] + haut[:-1]


def tracer_polygone(polygone, points):
    """Trace la figure. Cette fonction demande matplotlib."""
    import matplotlib.pyplot as plt

    x = [sommet[0] for sommet in polygone] + [polygone[0][0]]
    y = [sommet[1] for sommet in polygone] + [polygone[0][1]]
    plt.plot(x, y, color="black")
    for point in points:
        couleur = "green" if dedans(point, polygone) else "red"
        plt.scatter(point[0], point[1], color=couleur)
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def demonstrations():
    maison = [(0, 0), (2, 0), (2, 1.5), (1, 2.5), (0, 1.5)]

    print("1. Vecteurs")
    print("Vecteur AB :", vecteur((1, 2), (4, 6)))
    print("Produit scalaire :", produit_scalaire((1, 2), (3, 4)))
    print("Norme de (3,4) :", norme((3, 4)))
    print("Angle entre (1,0) et (1,1) :", angle((1, 0), (1, 1)))
    print("Distance de (0,0) à la droite passant par (0,1) et (1,0) :",
          distance_point_droite((0, 0), (0, 1), (1, 0)))

    print("\n2. Déterminant, aire et orientation")
    print("Déterminant :", determinant((1, 0), (0, 1)))
    print("Aire de la maison :", aire(maison))
    print("Orientation :", orientation((0, 0), (1, 0), (1, 1)))

    print("\n3. Segments")
    A, B = (0, 0), (1, 1)
    C, D = (0, 1), (1, 0)
    print("Se coupent ?", se_coupent(A, B, C, D))
    print("Intersection :", intersection(A, B, C, D))

    print("\n4. Points dans le polygone")
    for point in ((1, 1), (1, 2.4), (3, 1), (0.2, 2.2)):
        print(point, dedans(point, maison))

    print("\n5. Aire par hasard")
    print("Aire estimée :", aire_au_hasard(maison))

    print("\n6. Zones et enveloppe convexe")
    zones = [maison, [(3, 0), (4, 0), (4, 1), (3, 1)]]
    print(zone_de((1, 1), zones), zone_de((3.5, 0.5), zones), zone_de((2.5, 0.5), zones))
    print(enveloppe([(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]))


if __name__ == "__main__":
    demonstrations()
