Ex 1.1
import math

def vecteur(A, B):
    return (B[0] - A[0], B[1] - A[1])

def produit_scalaire(u, v):
    return u[0] * v[0] + u[1] * v[1]

def norme(u):
    return math.sqrt(produit_scalaire(u, u))

def angle(u, v):
    cos_theta = produit_scalaire(u, v) / (norme(u) * norme(v))
    cos_theta = max(-1.0, min(1.0, cos_theta))   # évite un cos hors de [-1, 1] à cause des arrondis
    return math.degrees(math.acos(cos_theta))

print(norme((3, 4)))                        # 5.0
print(produit_scalaire((1, 2), (3, 4)))     # 11
print(round(angle((1, 0), (1, 1)), 6))      # 45.0
print(angle((1, 0), (0, 1)))                # 90.0

Ex 1.2
def determinant(u, v):
    return u[0] * v[1] - u[1] * v[0]

def distance_point_droite(P, A, B):
    return abs(determinant(vecteur(A, B), vecteur(A, P))) / norme(vecteur(A, B))

print(distance_point_droite((0, 0), (0, 1), (1, 0)))   # 0.7071...
print(distance_point_droite((3, 4), (0, 0), (1, 0)))   # 4.0

Ex 2.1
EPS = 1e-12   # un déterminant de flottants n'est pas comparé exactement à zéro

def orientation(A, B, C):
    d = determinant(vecteur(A, B), vecteur(A, C))
    if d > EPS:
        return 1
    if d < -EPS:
        return -1
    return 0

print(orientation((0, 0), (1, 0), (1, 1)))    # 1
print(orientation((0, 0), (1, 0), (1, -1)))   # -1
print(orientation((0, 0), (1, 1), (2, 2)))    # 0

Ex 2.2
def aire(polygone):
    n = len(polygone)
    somme = 0
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        somme += x1 * y2 - x2 * y1
    return abs(somme) / 2

maison = [(0, 0), (2, 0), (2, 1.5), (1, 2.5), (0, 1.5)]

print(aire([(0, 0), (1, 0), (1, 1), (0, 1)]))   # 1.0
print(aire([(0, 0), (4, 0), (0, 3)]))           # 6.0
print(aire(maison))                             # 4.0

Ex 3.1
def se_coupent(A, B, C, D):
    """Renvoie True si les segments [AB] et [CD] se coupent.
    Les cas où trois points sont alignés ne sont pas traités : renvoie False."""
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)
    return o1 * o2 < 0 and o3 * o4 < 0

print(se_coupent((0, 0), (1, 1), (0, 1), (1, 0)))   # True
print(se_coupent((0, 0), (1, 0), (0, 1), (1, 1)))   # False
print(se_coupent((0, 0), (1, 1), (2, 2), (3, 3)))   # False

Ex 3.2
def intersection(A, B, C, D):
    AB = vecteur(A, B)
    CD = vecteur(C, D)
    AC = vecteur(A, C)
    denom = determinant(AB, CD)
    if abs(denom) < EPS:
        return None
    t = determinant(AC, CD) / denom
    u = determinant(AC, AB) / denom
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (A[0] + t * AB[0], A[1] + t * AB[1])
    return None

print(intersection((0, 0), (2, 2), (0, 2), (2, 0)))   # (1.0, 1.0)
print(intersection((0, 0), (1, 0), (0, 1), (1, 1)))   # None

Ex 4.1
def dedans(P, polygone):
    x, y = P
    n = len(polygone)
    resultat = False
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        if (y1 > y) != (y2 > y):                        # le côté traverse l'horizontale de P
            x_croise = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_croise:                             # croisement à droite de P
                resultat = not resultat
    return resultat

print([dedans(P, maison) for P in [(1, 1), (1, 2.4), (3, 1), (0.2, 2.2)]])
# [True, True, False, False]


Ex 4.2
import random

random.seed(0)   # sans cette ligne, le résultat change à chaque exécution
N = 200_000
compte = 0
for _ in range(N):
    P = (random.uniform(0, 2), random.uniform(0, 2.5))
    if dedans(P, maison):
        compte += 1
print(2 * 2.5 * compte / N)   # ≈ 4.0

Ex 5.1
L_forme = [(0, 0), (3, 0), (3, 1), (1, 1), (1, 3), (0, 3)]

print(dedans((0.5, 2), L_forme))   # True
print(dedans((2, 2), L_forme))     # False : dans le creux du L
print(aire(L_forme))               # 5.0

import matplotlib.pyplot as plt

def tracer_polygone(polygone, points=()):
    xs = [s[0] for s in polygone] + [polygone[0][0]]
    ys = [s[1] for s in polygone] + [polygone[0][1]]
    plt.figure(figsize=(5, 5))
    plt.plot(xs, ys, color="black")
    for P in points:
        couleur = "green" if dedans(P, polygone) else "red"
        plt.scatter([P[0]], [P[1]], color=couleur)
    plt.axis("equal")
    plt.title("Vert : dedans, rouge : dehors")
    plt.show()

random.seed(1)
nuage = [(random.uniform(-0.5, 3.5), random.uniform(-0.5, 3.5)) for _ in range(60)]
tracer_polygone(L_forme, nuage)

Ex 6.1
def zone_de(P, zones):
    for i, zone in enumerate(zones):
        if dedans(P, zone):
            return i
    return None

zones = [maison, [(3, 0), (4, 0), (4, 1), (3, 1)]]
print(zone_de((1, 1), zones))       # 0
print(zone_de((3.5, 0.5), zones))   # 1
print(zone_de((2.5, 0.5), zones))   # None



