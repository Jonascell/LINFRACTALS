import fractal
from calculos import dimenção_fractal
def dados():
    analise = fractal.fractal()
    nome_amostra = input(str('Identidade: ')).upper()
    tipo_amostra = input(str('Informe a condição das amostras: ')).upper()

    dados = {'nome_amostra': nome_amostra, 'tipo_amostra': tipo_amostra, 'valores': analise}

    df = []

    for i in range(1, len(dados['valores']) + 1):
        x = dados['valores'][f'imagem_{i}'][0]
        y = dados['valores'][f'imagem_{i}'][1]
        eixos = dimenção_fractal(x, y)
        df.append(eixos)

    resultado = {'nome_amostra': nome_amostra, 'tipo_amostra': tipo_amostra, 'dimenção_fractal': df}
    return resultado

