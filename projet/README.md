# Projet : cercles et intersections

## Que fait le programme ?

À partir de trois points, il calcule le cercle qui passe par eux. Il cherche ensuite où une droite coupe ce cercle : en deux points, en un point ou pas du tout.

## Notions utilisées

- Géométrie : cercles, droites et points d'intersection.
- Matrices : le centre du cercle est trouvé avec la méthode du TP4.
- Polynômes : les intersections sont calculées en résolvant un polynôme du second degré.
- Flottants : le programme limite certaines erreurs d'arrondi et repère les points presque alignés.
- Arithmétique : les calculs utilisent les opérations sur les coordonnées. Les notions du TP2, comme le PGCD ou le modulo, restent à ajouter.

## Lancer

Depuis la racine du dépôt :

```bash
python -m projet.cercles
```

Le programme affiche des exemples de sécante, de tangente, de droite sans intersection et de points presque alignés.

## Limites

Les calculs utilisent des nombres flottants. Quand les trois points sont presque alignés, le cercle est très sensible aux petites erreurs de mesure.
