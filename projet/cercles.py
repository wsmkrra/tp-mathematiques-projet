"""Projet : ajustement d'un cercle et intersections avec une droite."""

import math

from tp.tp3_polynomes_fonctions import evaluer
from tp.tp4_matrices_systemes import resoudre


def cercle_par_trois_points(A, B, C):
    """Renvoie (centre, rayon) du cercle défini par trois points non alignés."""
    x0, y0 = A
    deplacements = [(B[0] - x0, B[1] - y0), (C[0] - x0, C[1] - y0)]
    echelle = max(abs(coord) for vecteur in deplacements for coord in vecteur)
    if echelle == 0:
        raise ValueError("les points ne définissent pas un cercle unique")

    # On décale l'origine en A et normalise les lignes du système.
    matrice = [[dx / echelle, dy / echelle] for dx, dy in deplacements]
    second_membre = [(dx * dx + dy * dy) / (2 * echelle)
                     for dx, dy in deplacements]
    try:
        u, v = resoudre(matrice, second_membre, tolerance=1e-14)
    except ValueError as erreur:
        raise ValueError("points alignés ou presque alignés") from erreur

    centre = (x0 + u, y0 + v)
    rayon = math.hypot(u, v)
    return centre, rayon


def polynome_intersection(centre, rayon, origine, direction):
    """Coefficients (c,b,a) de |origine+t*direction-centre|²=rayon²."""
    if direction == (0, 0):
        raise ValueError("la direction de la droite doit être non nulle")
    dx, dy = direction
    ox, oy = origine[0] - centre[0], origine[1] - centre[1]
    a = math.fsum((dx * dx, dy * dy))
    b = 2 * math.fsum((ox * dx, oy * dy))
    c = math.fsum((ox * ox, oy * oy, -(rayon * rayon)))
    return c, b, a


def racines_quadratiques_stables(a, b, c, tolerance=1e-14):
    """Racines réelles avec réduction de l'annulation dans la formule usuelle."""
    discriminant = math.fsum((b * b, -4 * a * c))
    echelle = abs(b * b) + abs(4 * a * c)
    seuil = tolerance * echelle
    if discriminant < -seuil:
        return ()
    if abs(discriminant) <= seuil:
        return (-b / (2 * a),)

    racine = math.sqrt(discriminant)
    q = -0.5 * (b + math.copysign(racine, b))
    if q == 0:
        return (-b / (2 * a),)
    return tuple(sorted((q / a, c / q)))


def intersections_droite_cercle(centre, rayon, origine, direction):
    """Renvoie les points où la droite paramétrée coupe le cercle."""
    c, b, a = polynome_intersection(centre, rayon, origine, direction)
    parametres = racines_quadratiques_stables(a, b, c)
    points = []
    for t in parametres:
        point = (origine[0] + t * direction[0],
                 origine[1] + t * direction[1])
        residu = evaluer([c, b, a], t)
        points.append((t, point, residu))
    return points


def demonstrations():
    points_mesures = [(7.0, -1.0), (2.0, 4.0), (-3.0, -1.0)]
    centre, rayon = cercle_par_trois_points(*points_mesures)
    print("Points utilisés :", points_mesures)
    print("Cercle calculé, centre et rayon :", centre, rayon)

    # La droite y=-1 traverse le cercle en (-3,-1) et (7,-1).
    intersections = intersections_droite_cercle(
        centre, rayon, origine=(-6.0, -1.0), direction=(1.0, 0.0)
    )
    print("Intersections avec la droite y=-1 :")
    for t, point, residu in intersections:
        distance = math.hypot(point[0] - centre[0], point[1] - centre[1])
        print(f"t={t:.12g}, point={point}, distance={distance:.12g}, "
              f"résidu du polynôme={residu:.3e}")

    print("Tangence avec la droite y=4 :",
          intersections_droite_cercle(
              centre, rayon, origine=(-6.0, 4.0), direction=(1.0, 0.0)
          ))
    print("Droite extérieure y=5 :",
          intersections_droite_cercle(
              centre, rayon, origine=(-6.0, 5.0), direction=(1.0, 0.0)
          ))

    try:
        cercle_par_trois_points((0, 0), (1, 1), (2, 2 + 1e-15))
    except ValueError as erreur:
        print("Cas presque aligné refusé :", erreur)


if __name__ == "__main__":
    demonstrations()
