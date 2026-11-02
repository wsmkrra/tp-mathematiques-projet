"""Quelques calculs de géométrie : cercles, droites et intersections."""

import math


def cercle_par_trois_points(A, B, C, tolerance=1e-12):
    """Calcule le centre et le rayon du cercle passant par A, B et C."""
    ax, ay = A

    # On place temporairement A à l'origine pour simplifier les formules.
    bx, by = B[0] - ax, B[1] - ay
    cx, cy = C[0] - ax, C[1] - ay
    echelle = max(abs(bx), abs(by), abs(cx), abs(cy))
    if echelle == 0:
        raise ValueError("les trois points doivent être distincts")

    # La formule du centre dépend du déterminant des deux directions.
    bx, by = bx / echelle, by / echelle
    cx, cy = cx / echelle, cy / echelle
    determinant = 2 * (bx * cy - by * cx)
    if abs(determinant) <= tolerance:
        raise ValueError("les points sont alignés ou presque alignés")

    longueur_b2 = bx * bx + by * by
    longueur_c2 = cx * cx + cy * cy
    centre_x_relatif = echelle * (longueur_b2 * cy - longueur_c2 * by) / determinant
    centre_y_relatif = echelle * (bx * longueur_c2 - cx * longueur_b2) / determinant

    centre = (ax + centre_x_relatif, ay + centre_y_relatif)
    rayon = math.hypot(centre_x_relatif, centre_y_relatif)
    return centre, rayon


def intersections_droite_cercle(centre, rayon, origine, direction,
                                tolerance=1e-12):
    """Renvoie les points où une droite coupe un cercle, s'il y en a."""
    if rayon < 0:
        raise ValueError("le rayon ne peut pas être négatif")

    longueur_direction = math.hypot(direction[0], direction[1])
    if longueur_direction == 0:
        raise ValueError("la direction de la droite doit être non nulle")

    # La direction unitaire permet de trouver le point de la droite
    # le plus proche du centre.
    ux = direction[0] / longueur_direction
    uy = direction[1] / longueur_direction
    vx = origine[0] - centre[0]
    vy = origine[1] - centre[1]
    position_proche = -(vx * ux + vy * uy)
    point_proche = (origine[0] + position_proche * ux,
                    origine[1] + position_proche * uy)

    distance = math.hypot(point_proche[0] - centre[0],
                          point_proche[1] - centre[1])
    demi_corde2 = rayon * rayon - distance * distance
    echelle = max(rayon * rayon, distance * distance)
    seuil = tolerance * echelle

    if demi_corde2 < -seuil:
        return []
    if abs(demi_corde2) <= seuil:
        return [point_proche]

    demi_corde = math.sqrt(demi_corde2)
    return [
        (point_proche[0] - demi_corde * ux,
         point_proche[1] - demi_corde * uy),
        (point_proche[0] + demi_corde * ux,
         point_proche[1] + demi_corde * uy),
    ]


def demonstrations():
    points = [(7.0, -1.0), (2.0, 4.0), (-3.0, -1.0)]
    centre, rayon = cercle_par_trois_points(*points)
    print("Points :", points)
    print("Centre du cercle :", centre)
    print("Rayon :", rayon)

    cas = [
        ("Sécante", (-6.0, -1.0), (1.0, 0.0)),
        ("Tangente", (-6.0, 4.0), (1.0, 0.0)),
        ("Droite extérieure", (-6.0, 5.0), (1.0, 0.0)),
    ]
    for nom, origine, direction in cas:
        points_intersection = intersections_droite_cercle(
            centre, rayon, origine, direction
        )
        print(f"{nom} : {points_intersection}")

    try:
        cercle_par_trois_points((0, 0), (1, 1), (2, 2 + 1e-15))
    except ValueError as erreur:
        print("Trois points presque alignés :", erreur)


if __name__ == "__main__":
    demonstrations()

