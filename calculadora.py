

def produtos_notaveis_soma_diferença(termo_1, termo_2, termo_3, termo_4):
    t13 = termo_1 * termo_3
    t14 = termo_1 * termo_4
    t23 = termo_2 * termo_3
    t24 = termo_2 * termo_4
    soma = t13 - t14 - t23 + t24
    return soma
