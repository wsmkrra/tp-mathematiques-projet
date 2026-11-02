# Travaux pratiques et projet personnel

Ce dépôt sépare nettement les travaux du module en deux parties :

- [tp/](tp/) contient les solutions des TP1 à TP6, avec un script Python par séance et des exemples à exécuter.
- [projet/](projet/) contient le projet personnel **Cercles et intersections dans le plan**. Il réunit géométrie, matrices et systèmes linéaires, polynômes, arithmétique, calcul numérique et flottants.

Les réponses aux TP sont regroupées dans [tp/README.md](tp/README.md). Le projet, sa méthode et ses limites sont décrits dans [projet/README.md](projet/README.md).

## Exécuter

Depuis la racine du dépôt, avec Python 3 :

    python tp/tp1_calcul_numerique.py
    python tp/tp2_arithmetique.py
    python tp/tp3_polynomes_fonctions.py
    python tp/tp4_matrices_systemes.py
    python tp/tp5_synthese.py
    python tp/tp6_geometrie_plan.py
    python -m projet.cercles

Le TP4 utilise NumPy facultativement pour comparer les résultats aux routines optimisées. Les fonctions de tracé des TP3 et TP6 nécessitent Matplotlib.

## Sources du cours

Les énoncés de référence sont ceux du module [Outils fondamentaux](https://cours.gclab.fr/outils-fondamentaux/). La page JupyterLite fournie est [l'arborescence des carnets](https://cours.gclab.fr/lite/tree/index.html).
