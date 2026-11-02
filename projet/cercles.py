
import math


def cercle_par_trois_points(A, B, C, tolerance=1e-12):
    """Renvoie (centre, rayon) du cercle passant par les points A, B et C."""
    if A == B or B == C or A == C:
        raise ValueError("les trois points doivent être distincts")

    # Coordonnées relatives à A.
    bx, by = B[0] - A[0], B[1] - A[1]
    cx, cy = C[0] - A[0], C[1] - A[1]

    # Le produit en croix est nul quand les points sont alignés.
    # On le compare à la taille des vecteurs : c'est un test d'angle presque nul.
    cross = bx * cy - by * cx
    if abs(cross) <= tolerance * math.hypot(bx, by) * math.hypot(cx, cy):
        raise ValueError("les points sont alignés ou presque alignés")

    b2 = bx * bx + by * by
    c2 = cx * cx + cy * cy
    ux = (cy * b2 - by * c2) / (2 * cross)
    uy = (bx * c2 - cx * b2) / (2 * cross)

    centre = (A[0] + ux, A[1] + uy)
    return centre, math.hypot(ux, uy)


def intersections_droite_cercle(centre, rayon, origine, direction, tolerance=1e-12):
    """Renvoie les points d'intersection (0, 1 ou 2) d'une droite et d'un cercle.

    La droite passe par `origine` et a pour vecteur directeur `direction`.
    """
    if rayon < 0:
        raise ValueError("le rayon ne peut pas être négatif")
    norme = math.hypot(direction[0], direction[1])
    if norme == 0:
        raise ValueError("la direction de la droite doit être non nulle")

    ux, uy = direction[0] / norme, direction[1] / norme

    # Projection orthogonale du centre sur la droite.
    t = (centre[0] - origine[0]) * ux + (centre[1] - origine[1]) * uy
    px, py = origine[0] + t * ux, origine[1] + t * uy

    # Pythagore : la demi-corde vaut sqrt(rayon² - distance²).
    ecart = rayon * rayon - (px - centre[0]) ** 2 - (py - centre[1]) ** 2
    seuil = tolerance * rayon * rayon
    if ecart < -seuil:
        return []
    if abs(ecart) <= seuil:
        return [(px, py)]

    demi_corde = math.sqrt(ecart)
    return [(px - demi_corde * ux, py - demi_corde * uy),
            (px + demi_corde * ux, py + demi_corde * uy)]


def demonstrations():
    centre, rayon = cercle_par_trois_points((7.0, -1.0), (2.0, 4.0), (-3.0, -1.0))
    print("Centre :", centre, " rayon :", rayon)

    cas = [
        ("Sécante", (-6.0, -1.0)),
        ("Tangente", (-6.0, 4.0)),
        ("Extérieure", (-6.0, 5.0)),
    ]
    for nom, origine in cas:
        print(f"{nom} :", intersections_droite_cercle(centre, rayon, origine, (1.0, 0.0)))

    try:
        cercle_par_trois_points((0, 0), (1, 1), (2, 2 + 1e-15))
    except ValueError as erreur:
        print("Presque alignés :", erreur)


if __name__ == "__main__":
    demonstrations()
