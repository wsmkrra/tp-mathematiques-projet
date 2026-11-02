
Ex 1.1
def transposee(A):
    return [list(colonne) for colonne in zip(*A)]

print(transposee([[1, 2, 3], [4, 5, 6]]))   # [[1, 4], [2, 5], [3, 6]]


Ex 2.1
def produit(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C

print(produit([[1, 2], [3, 4]], [[1, 0], [0, 1]]))   # [[1, 2], [3, 4]] : l'identité ne change rien
print(produit([[1, 2], [3, 4]], [[0, 1], [1, 0]]))   # [[2, 1], [4, 3]] : vérifié de tête


Ex 2.2
import random
import time

def matrice_aleatoire(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

for n in [40, 80, 120]:
    A = matrice_aleatoire(n)
    B = matrice_aleatoire(n)
    debut = time.perf_counter()
    produit(A, B)
    print(n, round(time.perf_counter() - debut, 4))



Ex 3.1
import numpy as np

n = 120
A = matrice_aleatoire(n)
B = matrice_aleatoire(n)
A_np = np.array(A)
B_np = np.array(B)

debut = time.perf_counter()
produit(A, B)
t_python = time.perf_counter() - debut

debut = time.perf_counter()
for _ in range(100):
    A_np @ B_np
t_numpy = (time.perf_counter() - debut) / 100

print("python :", round(t_python, 4), "s")
print("numpy  :", round(t_numpy, 7), "s")
print("rapport:", round(t_python / t_numpy))

Ex 4.1
def resoudre(A, b):
    n = len(A)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    # élimination avec pivot partiel
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(M[i][k]))
        if M[p][k] == 0:
            raise ValueError("système singulier")
        M[k], M[p] = M[p], M[k]
        for i in range(k + 1, n):
            facteur = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= facteur * M[k][j]
    # remontée
    x = [0] * n
    for i in range(n - 1, -1, -1):
        somme = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - somme) / M[i][i]
    return x

A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
b = [2, -1, 8]
x = resoudre(A, b)
print([round(v, 10) for v in x])                                              # [3.0, -1.0, 0.5]
print([round(sum(A[i][j] * x[j] for j in range(3)), 10) for i in range(3)])   # [2.0, -1.0, 8.0] = b

Ex 4.2
import numpy as np

rng = np.random.default_rng(0)
n = 50
A_np = rng.standard_normal((n, n))
b_np = rng.standard_normal(n)

x_mine = np.array(resoudre(A_np.tolist(), b_np.tolist()))
x_numpy = np.linalg.solve(A_np, b_np)
print(np.max(np.abs(x_mine - x_numpy)))   # environ 1e-13, donc inférieur à 1e-9

Ex 5.1
import numpy as np

def hilbert(n):
    return np.array([[1.0 / (i + j + 1) for j in range(n)] for i in range(n)])

n = 12
H = hilbert(n)
x_vrai = np.ones(n)
b = H @ x_vrai
x_solve = np.linalg.solve(H, b)
x_inverse = np.linalg.inv(H) @ b
print("erreur avec solve   :", float(np.max(np.abs(x_solve - x_vrai))))
print("erreur avec inv @ b :", float(np.max(np.abs(x_inverse - x_vrai))))
print("conditionnement     : {:.3e}".format(float(np.linalg.cond(H))))

Ex 6.1
import numpy as np

def rotation(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s], [s, c]])

print(np.allclose(rotation(np.pi / 3) @ rotation(np.pi / 6), rotation(np.pi / 2)))   # True

Ex 7.1
def determinant(A):
    n = len(A)
    M = [list(map(float, ligne)) for ligne in A]
    det = 1.0
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(M[i][k]))
        if M[p][k] == 0:
            return 0.0
        if p != k:
            M[k], M[p] = M[p], M[k]
            det = -det
        det *= M[k][k]
        for i in range(k + 1, n):
            facteur = M[i][k] / M[k][k]
            for j in range(k, n):
                M[i][j] -= facteur * M[k][j]
    return det

import numpy as np

A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
print(round(determinant(A), 10), round(float(np.linalg.det(np.array(A, dtype=float))), 10))   # -2.0 -2.0
print(determinant([[1, 2], [2, 4]]))   # 0.0
