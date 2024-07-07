import numpy as np
import math


def cortar_matriz(matriz_imagem, n_divisões=0):
    divisão_horizontal = np.hsplit(matriz_imagem, n_divisões)
    conta_pixel = 0
    conta_caixa = 0
    for i in range(len(divisão_horizontal)):
        divisão_vertical = np.vsplit(divisão_horizontal[i], n_divisões)
        for e in divisão_vertical:
            valores_n = []
            for n in e.flat:
                valores_n.append(n)
            if sum(valores_n) != 255 * len(valores_n):
                conta_pixel += 1
            conta_caixa += 1
    return [conta_caixa, conta_pixel]


#Retorna uma lista de numeos inteiros que dividem a horizontal e vertical de uma imagem.
def divisores_vh(img):
    tamanho_imagem = img.size
    divisores = []
    for i in range(1, tamanho_imagem[0] + 1):
        if tamanho_imagem[0] % i == 0 and tamanho_imagem[1] % i == 0:
            divisores.append(i)
    return divisores


def converter_para_matriz(img):
    matriz = np.asarray(img)
    return matriz


def extrair_dados(imagem):
    matriz_imagem = converter_para_matriz(imagem)
    divisores = divisores_vh(imagem)
    tamanho_imagem = imagem.size

    log_tamanhodascaixas = []
    log_ncaixas_imagens = []

    for e in divisores:
        c = cortar_matriz(matriz_imagem, e)
        log_ncaixas_imagens.append(math.log(c[1], 10))

    for i in range(len(divisores)):
        log_tamanhodascaixas.append(math.log((1 / (tamanho_imagem[0] / divisores[i])), 10))

    return [log_tamanhodascaixas, log_ncaixas_imagens]