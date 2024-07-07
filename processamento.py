import matplotlib.pyplot as plt
from numpy import asarray
from PIL import ImageEnhance
import numpy as np
from PIL import Image

def process():
    from varredura import nucleos
    nucleos = nucleos()

    def imagem_300(nucleos):

        data = []

        def redimensionar(imagem):

            tamanho = np.shape(imagem)
            horizontal = 300 - tamanho[0]
            vertical = 300 - tamanho[1]

            linhas = horizontal // 2
            colunas = vertical // 2

            if linhas != horizontal * 2:
                linhas_cima = linhas
                linhas_baixo = horizontal - linhas

            else:
                linhas_cima = linhas
                linhas_baixo = linhas

            if colunas != vertical * 2:
                colunas_esquerda = colunas
                colunas_direita = vertical - colunas

            else:
                colunas_esquerda = colunas
                colunas_direita = colunas

            for i in range(linhas_cima):
                imagem = np.insert(imagem, 0, 255, axis=0)

            for i in range(linhas_baixo):
                imagem = np.insert(imagem, -1, 255, axis=0)

            for i in range(colunas_esquerda):
                imagem = np.insert(imagem, 0, 255, axis=1)

            for i in range(colunas_direita):
                imagem = np.insert(imagem, -1, 255, axis=1)


            return imagem

        for i in nucleos:
            imagem = i
            imagem = ImageEnhance.Brightness(imagem).enhance(1)
            imagem_cinza = imagem.convert(mode='L')
            data.append(redimensionar(asarray(imagem_cinza)))

        cont = 1
        for i in data:
            plt.imshow(i, cmap='gray')
            plt.subplot(10, 10, cont)
            plt.title(f'{cont}', fontsize=9)
            plt.axis('off')
            plt.imshow(i, cmap='gray')
            cont += 1
        plt.subplots_adjust(wspace=0, hspace=1)
        plt.show()
        return data

    imagens_300 = imagem_300(nucleos)
    return imagens_300
