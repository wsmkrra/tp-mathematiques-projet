# Géométrie du plan : cercles, droites et intersections

Petit module Python qui calcule :

- le cercle passant par trois points ;
- les points d'intersection d'une droite et d'un cercle.

Aucune dépendance : seul le module `math` de la bibliothèque standard est utilisé.

## Contenu du projet

| Fichier        | Rôle                                                        |
| -------------- | ----------------------------------------------------------- |
| `geometrie.py` | Les deux fonctions et une démonstration (`demonstrations`). |
| `README.md`    | Ce fichier.                                                 |

## Lancer la démonstration

```bash
python3 geometrie.py
```

Sortie attendue :

```
Centre : (2.0, -1.0)  rayon : 5.0
Sécante : [(-3.0, -1.0), (7.0, -1.0)]
Tangente : [(2.0, 4.0)]
Extérieure : []
Presque alignés : les points sont alignés ou presque alignés
```

## Utilisation dans votre code

```python
from geometrie import cercle_par_trois_points, intersections_droite_cercle

centre, rayon = cercle_par_trois_points((7, -1), (2, 4), (-3, -1))

points = intersections_droite_cercle(
    centre, rayon, origine=(-6, -1), direction=(1, 0)
)
print(points)   # [(-3.0, -1.0), (7.0, -1.0)]
```

## Fonctions

### `cercle_par_trois_points(A, B, C, tolerance=1e-12)`

Renvoie `(centre, rayon)` : `centre` est un couple `(x, y)`, `rayon` un flottant.

- Lève `ValueError` si deux des points sont confondus.
- Lève `ValueError` si les trois points sont alignés ou presque alignés.

### `intersections_droite_cercle(centre, rayon, origine, direction, tolerance=1e-12)`

Renvoie la liste des points d'intersection de la droite qui passe par `origine` et a pour vecteur directeur `direction`, avec le cercle.

| Résultat          | Signification         |
| ----------------- | --------------------- |
| `[]`              | pas d'intersection    |
| un point          | droite tangente       |
| deux points       | droite sécante        |

- Lève `ValueError` si le rayon est négatif ou si `direction` est le vecteur nul.

## Tolérance

Les calculs se font en nombres flottants, donc les cas limites (tangence, alignement) sont tranchés avec une tolérance relative :

- **Cercle.** Le produit en croix de `AB` et `AC` est comparé à `tolerance × |AB| × |AC|`. Les trois points sont donc rejetés quand le sinus de l'angle en `A` est inférieur à `tolerance`.
- **Droite.** La droite est tangente quand `|r² − d²| ≤ tolerance × r²`, où `d` est la distance du centre à la droite.

## Limites

- Le module ne travaille que dans le plan (pas de 3D).
- Les points sont donnés comme des couples de nombres `(x, y)`.
- La précision est de l'ordre de 10⁻¹¹ en relatif, limitée par les flottants.
