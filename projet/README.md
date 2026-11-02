# Projet personnel — Cercles et intersections dans le plan

## But

À partir de trois points non alignés, calculer le cercle passant par eux, puis déterminer les intersections de ce cercle avec une droite. Le programme traite les cas de deux intersections, de tangence et d'absence d'intersection, et affiche le résidu numérique du polynôme obtenu.

## Notions mobilisées

- **Géométrie plane :** coordonnées, centre et rayon d'un cercle, droite paramétrée, points d'intersection.
- **Matrices et systèmes linéaires :** le centre est calculé en résolvant un système de deux équations à deux inconnues avec le pivot de Gauss du TP4.
- **Polynômes et racines :** la substitution d'une droite paramétrée dans l'équation du cercle donne un polynôme quadratique en le paramètre t.
- **Calcul numérique et flottants :** formule quadratique stabilisée, discriminant près de zéro, math.fsum, résidu et points presque alignés.
- **Arithmétique :** les coefficients du polynôme sont obtenus à partir des produits et sommes des coordonnées.

## Calculs

Pour trois points A, B et C, on translate l'origine en A. Le centre relatif (u, v) vérifie le système :

    2 (Bx-Ax) u + 2 (By-Ay) v = (Bx-Ax)² + (By-Ay)²
    2 (Cx-Ax) u + 2 (Cy-Ay) v = (Cx-Ax)² + (Cy-Ay)²

Le système est résolu par resoudre du TP4. Le programme normalise les coefficients avant de résoudre pour limiter les problèmes d'échelle et signale les points alignés ou presque alignés.

Une droite P + t V croise le cercle si les racines réelles du polynôme ci-dessous existent :

    a = V·V
    b = 2 (P-centre)·V
    c = |P-centre|² - rayon²
    a t² + b t + c = 0

Les racines donnent ensuite les points d'intersection. Le code réutilise l'évaluation de polynômes du TP3 pour afficher le résidu en chaque racine.

## Exécution

Depuis la racine du dépôt :

    python -m projet.cercles

Le scénario fourni utilise trois points d'un cercle de centre (2, -1) et de rayon 5. La droite y=-1 le coupe en deux points ; deux autres droites illustrent la tangence et l'absence d'intersection.

## Limites

Le programme emploie des nombres flottants. Le seuil du discriminant est donc relatif à la taille des termes du calcul. Des points extrêmement proches d'un alignement peuvent être déclarés presque alignés, car leur cercle est très sensible aux petites variations des coordonnées. Pour des données réelles, il faudrait également documenter l'incertitude de mesure et choisir une tolérance adaptée à l'unité utilisée.
