"""TP5 - Chiffrement affine et analyse des lettres."""

from collections import Counter
import random
import unicodedata


def nettoyer(texte):
    """Met en majuscules, retire les accents et les espaces."""
    texte = unicodedata.normalize("NFD", texte.upper())
    resultat = ""
    for caractere in texte:
        if unicodedata.category(caractere) == "Mn":
            continue
        if "A" <= caractere <= "Z":
            resultat += caractere
    return resultat


def lettre_vers_nombre(lettre):
    return ord(lettre) - ord("A")


def nombre_vers_lettre(nombre):
    return chr(nombre % 26 + ord("A"))


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def cles_a_valides():
    """Les valeurs de a doivent être premières avec 26."""
    resultat = []
    for a in range(1, 26):
        if pgcd(a, 26) == 1:
            resultat.append(a)
    return resultat


def chiffrer(texte, a, b):
    """Applique E(x)=(a*x+b) modulo 26."""
    texte = nettoyer(texte)
    resultat = ""
    for lettre in texte:
        x = lettre_vers_nombre(lettre)
        y = (a * x + b) % 26
        resultat += nombre_vers_lettre(y)
    return resultat


def inverse_modulaire(a, modulo):
    """Cherche un nombre qui multiplié par a donne 1 modulo n."""
    for candidat in range(1, modulo):
        if (a * candidat) % modulo == 1:
            return candidat
    raise ValueError("Cette clé ne peut pas être inversée.")


def dechiffrer(texte, a, b):
    inverse = inverse_modulaire(a, 26)
    texte = nettoyer(texte)
    resultat = ""
    for lettre in texte:
        y = lettre_vers_nombre(lettre)
        x = (inverse * (y - b)) % 26
        resultat += nombre_vers_lettre(x)
    return resultat


def toutes_les_clefs(secret):
    """Essaie toutes les clés inversibles."""
    resultat = []
    for a in cles_a_valides():
        for b in range(26):
            resultat.append((a, b, dechiffrer(secret, a, b)))
    return resultat


def candidats_frequence(secret):
    """Suppose que la lettre chiffrée la plus courante vient de E."""
    secret = nettoyer(secret)
    frequences = Counter(secret)
    lettre_courante = frequences.most_common(1)[0][0]
    numero_courant = lettre_vers_nombre(lettre_courante)

    candidats = []
    for a in cles_a_valides():
        b = (numero_courant - 4 * a) % 26
        candidats.append((a, b, dechiffrer(secret, a, b)))
    return candidats


def indice_coincidence(texte):
    """Mesure la probabilité de tirer deux fois la même lettre."""
    texte = nettoyer(texte)
    n = len(texte)
    if n < 2:
        return 0
    comptes = Counter(texte)
    total = 0
    for nombre in comptes.values():
        total += nombre * (nombre - 1)
    return total / (n * (n - 1))


def vigenere(texte, cle):
    """Chiffre chaque lettre avec le décalage indiqué par la clé."""
    texte = nettoyer(texte)
    cle = nettoyer(cle)
    if len(cle) == 0:
        raise ValueError("La clé ne peut pas être vide.")

    resultat = ""
    for i in range(len(texte)):
        x = lettre_vers_nombre(texte[i])
        decalage = lettre_vers_nombre(cle[i % len(cle)])
        resultat += nombre_vers_lettre(x + decalage)
    return resultat


def demonstrations():
    print("1. Chiffrer et déchiffrer")
    message = nettoyer("Attaque à l'aube")
    secret = chiffrer(message, 5, 8)
    print("Message :", message)
    print("Chiffré :", secret)
    print("Déchiffré :", dechiffrer(secret, 5, 8))

    print("\n2. Clés possibles")
    print(cles_a_valides(), "il y en a", len(cles_a_valides()))
    print("Inverse de 5 modulo 26 :", inverse_modulaire(5, 26))

    print("\n3. Force brute")
    essais = toutes_les_clefs(secret)
    print("Nombre de clés testées :", len(essais))
    for a, b, texte in essais:
        if texte == message:
            print("Bonne clé trouvée :", a, b)

    print("\n4. Analyse de fréquences")
    texte_long = nettoyer(
        "Le chiffrement affine remplace les lettres par d'autres lettres "
        "et conserve les frequences du texte."
    )
    secret_long = chiffrer(texte_long, 7, 12)
    for candidat in candidats_frequence(secret_long):
        print(candidat)

    print("\n5. Indice de coïncidence")
    generateur = random.Random(1)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hasard = ""
    for _ in range(len(texte_long)):
        hasard += generateur.choice(alphabet)
    print("Texte clair :", indice_coincidence(texte_long))
    print("Texte chiffré :", indice_coincidence(secret_long))
    print("Lettres au hasard :", indice_coincidence(hasard))

    print("\n6. Vigenère")
    secret_vigenere = vigenere(texte_long * 4, "CLE")
    print("Indice :", indice_coincidence(secret_vigenere))


if __name__ == "__main__":
    demonstrations()
