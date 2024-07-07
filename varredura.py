import numpy as np
import matplotlib.pyplot as plt
from carregar_abrir_converter_imagem import carregar_imagem, abrir_imagem, converter_para_matriz
from PIL import ImageEnhance
from sys import stdout
import analise
from corte import imagem_corte

def nucleos():
    def imagem_brilho(diretorio, brilho, coord):
        imagem = abrir_imagem(diretorio)
        imagem_recorte = imagem.crop(coord)
        imagem_recorte = ImageEnhance.Brightness(imagem_recorte).enhance(brilho)
        matriz = imagem_recorte.convert(mode='L')
        imagem_matriz = converter_para_matriz(matriz)
        return imagem_matriz


    def indice_max(eventos_xy):
        valor = []
        for i in range(len(eventos_xy)):
            tamanho = eventos_xy[i][1] - eventos_xy[i][0]
            valor.append(tamanho)
        indice = valor.index(max(valor))
        return indice


    def varredura(diretorio, margem = 100):
        #abre imagem
        imagem = abrir_imagem(diretorio)

        #retorna as coordenadas da imagem formato medidas = x, y, x1, y1
        medidas = 0, 0, np.shape(imagem)[1], np.shape(imagem)[0]
        for r in range(2):
            #se o indice r for = 0 nenhuma iteração foi realizada logo as coordenadas serão iqual ao tamanho total da imagem
            if r == 0:
                coord = (medidas)
            #um recorte da imagem será feito nas coodenadas atuais
            imagem_recorte = imagem.crop(coord)
            linhas = np.shape(imagem_recorte)[0]
            colunas = np.shape(imagem_recorte)[1]
            soma_linhas = 255 * colunas
            soma_colunas = 255 * linhas
            brilho = 2
            somalinhas_y = []
            somacolunas_x = []
            eventos_y = []
            eventos_x = []
            y_si = []
            x_de = []
            while True:
                imagem_matriz = imagem_brilho(diretorio, brilho, coord)


                inicio_y = 0
                inicio_x = 0
                for n in range(linhas):
                    somalinhas_y.append(sum(imagem_matriz[n]) - soma_linhas)
                for m in range(colunas):
                    somacolunas_x.append(sum(imagem_matriz[:, m]) - soma_colunas)
                for i in range(linhas):
                    if somalinhas_y[i - 1] == 0 and somalinhas_y[i] != 0:
                        inicio_y = i
                    elif somalinhas_y[i - 1] != 0 and somalinhas_y[i] == 0:
                        fim_y = i - 1
                        eventos_y.append([inicio_y, fim_y])
                for j in range(colunas):
                    if somacolunas_x[j - 1] == 0 and somacolunas_x[j] != 0:
                        inicio_x = j
                    elif somacolunas_x[j - 1] != 0 and somacolunas_x[j] == 0:
                        fim_x = j - 1
                        eventos_x.append([inicio_x, fim_x])
                if r == 0 and len(eventos_y) <= 4 and len(eventos_x) <= 4:
                    break
                elif r == 1 and len(eventos_y) <= 2 and len(eventos_x) <= 2:
                    break
                else:
                    brilho += 1
                    somalinhas_y.clear()
                    somacolunas_x.clear()
                    eventos_y.clear()
                    eventos_x.clear()

            if eventos_x == [] or eventos_y == []:
                eventos_x = [[0, 100]]
                eventos_y = [[0, 50]]

            y_si.append(eventos_y[indice_max(eventos_y)])
            x_de.append(eventos_x[indice_max(eventos_x)])

            if r == 0:
                registro_coord = x_de[0][0] - margem, y_si[0][0] - margem, x_de[0][1] + margem,  y_si[0][1] + margem
            if r == 0:
                coord = x_de[0][0] - margem, y_si[0][0] - margem, x_de[0][1] + margem, y_si[0][1] + margem
            elif r == 1:
                coord = registro_coord[0] + x_de[0][0] - margem, registro_coord[1] + y_si[0][0] - margem, \
                        registro_coord[0] + x_de[0][1] + margem, registro_coord[1] + y_si[0][1] + margem

            y_si.clear()
            x_de.clear()
            margem = 10
        recorte = imagem.crop(coord)
        return recorte

    diret = carregar_imagem()
    imagens = []
    """print(imagens)
    print(diret)"""
    n = 1
    for i in diret:
        corte = varredura(i)
        imagens.append(corte)
        stdout.write("\r%d" % n + '%')
        stdout.flush()
        n += 1
    """print(imagens)"""

    """select = input('deseja continuar?: ')"""

    cont = 1
    for i in imagens:
        plt.subplot(10, 10, cont)
        plt.title(f'{cont}', fontsize=9)
        plt.axis('off')
        plt.imshow(i)
        cont += 1
    plt.subplots_adjust(wspace=0, hspace=1)
    plt.show()

    verif = analise.verificacao()

    if verif != []:
        for i in verif:
            indice = i - 1
            rc = imagem_corte(diret[indice])
            corden = rc[0][0] * 4, rc[0][1] * 4, rc[0][2] * 4, rc[0][3] * 4
            print(f'As cordenadas (x1, y1, x2 y2) são: {corden}')
            imagem = abrir_imagem(diret[indice])
            recorte = imagem.crop(corden)

            imagens[indice] = recorte

    cont = 1
    for i in imagens:
        plt.subplot(10, 10, cont)
        plt.title(f'{cont}', fontsize=9)
        plt.axis('off')
        plt.imshow(i)
        cont += 1
    plt.subplots_adjust(wspace=0, hspace=1)
    plt.show()

    return imagens
