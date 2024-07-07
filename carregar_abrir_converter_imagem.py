import matplotlib.pyplot as plt
import numpy as np


def carregar_imagem():
    """
    Permite a seleção de varios arquivos de imagem em uma caixa de
    diálogo e retorna os respectivos diretórios como tupla.
    :return: uma tupla com os nomes dos diretórios das imagens.
    """
    from tkinter import filedialog
    diretorio = filedialog.askopenfilenames()
    return diretorio


def abrir_imagem(diretorio):
    """
    Recebe um diretório e abre a imagem.
    :param diretorio:
    :return: imagem
    """
    from PIL import Image
    imagem = Image.open(diretorio)
    return imagem


def converter_para_matriz(imagem):
    """
    Converte a imagem em uma matriz numpy.
    :param imagem:
    :return: retorna uma matriz numpy.
    """
    import numpy as np
    matriz_imagem = np.asarray(imagem)
    return matriz_imagem

def varredura():
    from PIL import ImageEnhance
    import numpy as np
    diretorio = carregar_imagem()[0]
    imagem = abrir_imagem(diretorio)
    linhas = np.shape(imagem)[0]
    colunas = np.shape(imagem)[1]
    soma = 255 * linhas
    eventos = 0
    ponto = 0
    cor = 1
    nitidez = 1
    brilho = 2
    while True:
        imagem = abrir_imagem(diretorio)
        imagem = ImageEnhance.Color(imagem).enhance(cor)
        imagem = ImageEnhance.Sharpness(imagem).enhance(nitidez)
        imagem = ImageEnhance.Brightness(imagem).enhance(brilho)
        matriz = imagem.convert(mode='L')
        imagem_matriz = converter_para_matriz(matriz)
        while True:
            limite = 0
            for m in range(ponto, colunas):
                limite = m
                soma_colunas = sum(imagem_matriz[:, m])
                if soma_colunas != soma:
                    eventos += 1
                    for j in range(ponto, colunas):
                        soma_colunas = sum(imagem_matriz[:, j])
                        if soma_colunas == soma:
                            eventos += 1
                            break
                        else:
                            ponto += 1
                    break
                else:
                    ponto += 1
            if limite == colunas - 1:
                ponto = 0
                break
        print(eventos)
        plt.imshow(imagem_matriz)
        plt.show()
        if eventos > 2:
            brilho += 1
            eventos = 0
        elif eventos == 0:
            brilho = 2
            nitidez += 1
            cor += 1
        elif eventos == 2:
            break
    return cor, nitidez, brilho


def limpa_fundo():
    from PIL import ImageEnhance
    diretorio = carregar_imagem()[0]
    parametros = varredura(diretorio)
    imagem = abrir_imagem(diretorio)
    imagem = ImageEnhance.Color(imagem).enhance(parametros[0])
    imagem = ImageEnhance.Contrast(imagem).enhance(1)
    imagem = ImageEnhance.Sharpness(imagem).enhance(parametros[1])
    imagem = ImageEnhance.Brightness(imagem).enhance(parametros[2])
    matriz = imagem.convert(mode='L')
    imagem_matriz = converter_para_matriz(matriz)
    return imagem_matriz

def recortar(imagem_matriz):
    linhas = np.shape(imagem_matriz)[0]
    colunas = np.shape(imagem_matriz)[1]
    ys = 0
    yi = linhas
    xe = 0
    xd = colunas
    for n in range(linhas):
        soma_linhas = sum(imagem_matriz[n])
        ys += 1
        if soma_linhas != 255 * colunas:
            break
    for m in range(colunas):
        soma_colunas = sum(imagem_matriz[:, m])
        xe += 1
        if soma_colunas != 255 * linhas:
            break
    for i in range(linhas):
        soma_linhas = sum(imagem_matriz[-i])
        yi -= 1
        if soma_linhas != 255 * colunas:
            break
    for j in range(colunas):
        soma_colunas = sum(imagem_matriz[:, -j])
        xd -= 1
        if soma_colunas != 255 * linhas:
            break

    return xe - 20, ys - 20, xd + 20, yi + 20

