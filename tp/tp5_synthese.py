Ex 1.1
import unicodedata

def lettre_vers_nombre(c):
    return ord(c) - ord("A")

def nombre_vers_lettre(n):
    return chr(n + ord("A"))

print(lettre_vers_nombre("C"), nombre_vers_lettre(2))   # 2 C

Ex 1.2
def nettoyer(texte):
    texte = unicodedata.normalize("NFD", texte)   # sépare les accents des lettres
    resultat = ""
    for c in texte.upper():
        if "A" <= c <= "Z":
            resultat += c
    return resultat

print(nettoyer("Été, à Paris !"))   # ETEAPARIS

Ex 2.1
def chiffrer(texte, a, b):
    resultat = ""
    for c in texte:
        y = (a * lettre_vers_nombre(c) + b) % 26
        resultat += nombre_vers_lettre(y)
    return resultat

print(chiffrer("ATTAQUEALAUBE", 5, 8))   # IZZIKECILIENC

Ex 3.1
from math import gcd

cles_valides = [a for a in range(1, 26) if gcd(a, 26) == 1]
print(cles_valides, len(cles_valides))   # 12 valeurs, toutes impaires, sans 13

Ex 3.2
def inverse_modulaire(a, n):
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    raise ValueError(f"{a} n'a pas d'inverse modulo {n}")

print(inverse_modulaire(5, 26))   # 21

Ex 4.1
def dechiffrer(texte, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("clé invalide : a doit être premier avec 26")
    a_inv = inverse_modulaire(a, 26)
    resultat = ""
    for c in texte:
        x = (a_inv * (lettre_vers_nombre(c) - b)) % 26
        resultat += nombre_vers_lettre(x)
    return resultat

print(dechiffrer(chiffrer("ATTAQUEALAUBE", 5, 8), 5, 8))   # ATTAQUEALAUBE
# dechiffrer("ABC", 4, 7) lève une erreur : 4 n'est pas premier avec 26

Ex 5.1
def toutes_les_clefs(secret):
    resultats = []
    for a in range(1, 26):
        if gcd(a, 26) == 1:
            for b in range(26):
                resultats.append(((a, b), dechiffrer(secret, a, b)))
    return resultats

for cle, clair in toutes_les_clefs(secret):
    print(cle, clair[:40])   # une seule ligne est du français : (7, 3)

Ex 6.1
def casser_par_frequences(secret):
    lettre_frequente = Counter(secret).most_common(1)[0][0]
    y_E = lettre_vers_nombre(lettre_frequente)
    candidats = []
    for a in range(1, 26):
        if gcd(a, 26) == 1:
            b = (y_E - a * lettre_vers_nombre("E")) % 26
            candidats.append(((a, b), dechiffrer(secret, a, b)))
    return candidats

for cle, clair in casser_par_frequences(secret):
    print(cle, clair[:40])   # 12 candidats, dont (7, 3)

Ex 7.1
def indice_coincidence(texte):
    N = len(texte)
    comptes = Counter(texte)
    return sum(n * (n - 1) for n in comptes.values()) / (N * (N - 1))

hasard = "".join(random.choices(string.ascii_uppercase, k=len(texte_long)))
print(indice_coincidence(texte_long))    
print(indice_coincidence(secret_long))   
print(indice_coincidence(hasard))       

Ex 8.1
def vigenere(texte, cle):
    cle = nettoyer(cle)
    resultat = ""
    for i, c in enumerate(texte):
        decalage = lettre_vers_nombre(cle[i % len(cle)])
        resultat += nombre_vers_lettre((lettre_vers_nombre(c) + decalage) % 26)
    return resultat

chiffre_vig = vigenere(texte_long, "CLE")
print(indice_coincidence(chiffre_vig))   

Ex 8.2
def indice_moyen_colonnes(texte, L):
    colonnes = [texte[i::L] for i in range(L)]
    return sum(indice_coincidence(col) for col in colonnes) / L

for L in range(1, 8):
    print(L, round(indice_moyen_colonnes(chiffre_vig, L), 4))
# chez moi : ≈ 0,087 pour L = 3 et L = 6, ≈ 0,05 pour les autres

