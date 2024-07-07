import fractal
from carregar_abrir_converter_imagem import carregar_imagem, abrir_imagem, converter_para_matriz
import calculos
import matplotlib.pyplot as plt
imagem = carregar_imagem()[0]
abim = abrir_imagem(imagem)
abim = abim.convert(mode='L')
matriz = converter_para_matriz(abim)
plt.imshow(matriz)
plt.show()
cord = fractal.box(matriz)

print(calculos.dimenção_fractal(cord[0], cord[1]))
