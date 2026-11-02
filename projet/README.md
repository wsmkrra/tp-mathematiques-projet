# Projet de géométrie : cercles et droites

## Objectif

Le programme calcule le cercle passant par trois points, puis cherche où une droite le coupe.

## Calculs géométriques

- Le centre du cercle est calculé à partir des trois points.
- Pour la droite, le programme trouve le point le plus proche du centre. La distance à ce point permet de savoir si la droite ne coupe pas le cercle, le touche ou le traverse.

## Lancer le programme

Depuis la racine du dépôt :

```bash
python -m projet.cercles
```

Les exemples montrent une sécante, une tangente, une droite extérieure et un cas de trois points presque alignés.

## Limites

Les calculs utilisent des nombres flottants. Quand les trois points sont presque alignés, le cercle calculé devient très sensible aux petites erreurs.

Ce projet se concentre sur la géométrie. Il ne couvre pas à lui seul toutes les notions demandées pour le projet du module.

