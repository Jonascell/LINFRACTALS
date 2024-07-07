import processamento
import math

def fractal():
    imagens_analise = processamento.process()

    def comprimento_matriz(matriz):
        comprimento = len(matriz)
        return comprimento


    def divisores(comprimento):
        divisores = []
        for i in range(1, comprimento + 1):
            if comprimento % i == 0:
                divisores.append(int(i))
        return divisores


    def seletor(matriz):
        numero_itens = (len(matriz)) ** 2
        itens = 0
        for n in matriz.flat:
            if n == 255:
                itens += 1
        if itens == numero_itens:
            return True


    def box(matriz):
        comprimento = comprimento_matriz(matriz)
        divisor = divisores(comprimento_matriz(matriz))
        caixa = 0
        numero_caixas = []
        lado_caixas = []
        for e in divisor:
            passo = e
            frequencia = comprimento // passo
            linha1 = coluna1 = 0
            linha2 = coluna2 = passo
            for l in range(frequencia):
                for c in range(frequencia):
                    analise = matriz[linha1:linha2, coluna1:coluna2]
                    if seletor(analise) != True:
                        caixa += 1
                    coluna1 += passo
                    coluna2 += passo
                coluna1 = 0
                coluna2 = passo
                linha1 += passo
                linha2 += passo
            numero_caixas.append(math.log(caixa, 10))
            lado_caixas.append(math.log(passo,10))
            caixa = 0
        #print(f'{lado_caixas} | {numero_caixas}')
        return lado_caixas, numero_caixas
    dados_xy = {}
    cont = 1
    for i in imagens_analise:
        mi = i
        r = box(mi)
       # """print('Grade', end=' | ')
       # print('Tamanho do lado da caixa', end=' | ')
       # print('Quantidade de caixas preenchidas')"""
        dados_xy[f'imagem_{cont}'] = [r[0], r[1]]
        cont += 1
        """for i in range(len(divisores(comprimento_matriz(mi)))):
        #    print(f'{i+1}ª', end='    | ')
        #    print(f'{r[0][i]}', end='                        | ')
        #    print(f'{r[1][i]}')"""
    #"""print(dados_xy)"""
    return dados_xy

