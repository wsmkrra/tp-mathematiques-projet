# Solutions des TP1 à TP6

Chaque fichier regroupe les fonctions travaillées pendant la séance et une fonction demonstrations() qui affiche des exemples.

| TP | Sujet | Fichier |
|---|---|---|
| [TP1](https://cours.gclab.fr/outils-fondamentaux/tp1-calcul-numerique/) | Calcul numérique et flottants | [tp1_calcul_numerique.py](tp1_calcul_numerique.py) |
| [TP2](https://cours.gclab.fr/outils-fondamentaux/tp2-arithmetique/) | Arithmétique, primalité et complexité | [tp2_arithmetique.py](tp2_arithmetique.py) |
| [TP3](https://cours.gclab.fr/outils-fondamentaux/tp3-polynomes-fonctions/) | Polynômes, racines et méthodes numériques | [tp3_polynomes_fonctions.py](tp3_polynomes_fonctions.py) |
| [TP4](https://cours.gclab.fr/outils-fondamentaux/tp4-matrices-gauss/) | Matrices et systèmes linéaires | [tp4_matrices_systemes.py](tp4_matrices_systemes.py) |
| [TP5](https://cours.gclab.fr/outils-fondamentaux/tp5-synthese/) | Chiffrement affine et analyse de fréquence | [tp5_synthese.py](tp5_synthese.py) |
| [TP6](https://cours.gclab.fr/outils-fondamentaux/tp6-geometrie-plan/) | Géométrie du plan | [tp6_geometrie_plan.py](tp6_geometrie_plan.py) |

## Observations à retenir

- **TP1 :** les flottants sont des approximations binaires. Une comparaison avec == peut échouer après des opérations pourtant simples ; une formule algébriquement correcte peut aussi perdre de la précision par soustraction de quantités proches. Les fractions permettent une somme exacte lorsque leurs dénominateurs restent raisonnables.
- **TP2 :** Euclide et le test de primalité limité à la racine carrée évitent de parcourir inutilement tous les entiers. Le crible convient pour énumérer beaucoup de premiers. La récursion naïve de Fibonacci recalcule les mêmes valeurs, contrairement à la boucle.
- **TP3 :** Horner réduit le nombre d'opérations pour évaluer un polynôme. La dichotomie est robuste si un changement de signe est connu ; Newton converge vite près d'une racine mais peut osciller ou diverger. Pour x³-2x-5, les deux racines restantes sont complexes et ne se voient pas sur le graphe réel. Pour les dérivées numériques, diminuer indéfiniment le pas finit par amplifier les arrondis.
- **TP4 :** le pivot partiel améliore la stabilité de l'élimination de Gauss. Un système doit être résolu directement, sans calculer l'inverse. Le mauvais conditionnement peut dégrader fortement une solution même si l'algorithme est correct ; les fractions exactes illustrent le coût de supprimer les arrondis.
- **TP5 :** pour que le chiffrement affine soit déchiffrable, a doit être premier avec 26. L'espace de clés de 312 possibilités se parcourt facilement ; les fréquences réduisent encore la recherche, mais restent une heuristique sur les textes courts.
- **TP6 :** le déterminant encode l'aire orientée et les tests d'orientation. Le lancer de rayon marche aussi pour les polygones non convexes ; les cas sur le bord et près d'un sommet demandent un traitement explicite.

Les temps d'exécution dépendent de la machine et de sa charge : ils sont affichés par les scripts au lieu d'être inscrits comme des constantes.

## Réflexions sur les réponses générées

Les pages du cours demandent de confronter les propositions d'un assistant à des cas limites. Ces observations expliquent les précautions prises dans les scripts ; ajoutez vos propres résultats si votre enseignant attend le compte rendu de vos essais.

- **TP1 :** une tolérance absolue fixe ne s'adapte pas à l'échelle. Autour de 1e20, les flottants sont espacés de bien plus que 1e-9 ; une comparaison qui semble précise peut donc masquer des écarts importants. La fonction utilise une tolérance relative et absolue.
- **TP2 :** le test de primalité traite séparément les valeurs inférieures à 2 et le nombre 2, puis ignore les diviseurs pairs. Ces cas évitent des réponses fausses sur 1, les négatifs et le seul nombre premier pair.
- **TP3 :** la méthode naïve et Horner sont toutes deux justes, mais leur coût mesuré dépend du type des coefficients. Les puissances entières très grandes ne coûtent pas le même temps que les puissances flottantes.
- **TP4 :** pour résoudre Ax=b, solve est préférable au calcul de l'inverse suivi d'un produit. Sur une matrice mal conditionnée, les deux peuvent être imprécis ; la méthode par inverse amplifie encore l'erreur.
- **TP5 :** une clé non inversible, comme a=4 modulo 26, chiffre quand même le texte mais fusionne plusieurs lettres. Aucun déchiffrement ne peut alors reconstituer l'information perdue.
- **TP6 :** le lancer de rayon emploie une condition d'encadrement semi-ouverte pour ne compter un sommet qu'une seule fois. Les points sur un côté sont traités à part ; le script les classe comme appartenant au polygone.
