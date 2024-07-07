import calculadora
def dimenção_fractal(x, y):
    xy = []
    x2 = []
    y2 = []
    for i in range(len(x)):
        xy.append(x[i] * y[i])
        x2.append(x[i] ** 2)
        y2.append(y[i] ** 2)
    soma_y = sum(y)
    soma_x = sum(x)
    soma_xy = sum(xy)
    soma_x2 = sum(x2)
    soma_y2 = sum(y2)
    soma_amostra = len(x)

    a = ((soma_x * soma_y) - (soma_amostra * soma_xy)) / ((soma_x ** 2) - (soma_amostra * soma_x2))
    b = ((soma_xy * soma_x) - (soma_x2 * soma_y)) / ((soma_x ** 2) - (soma_amostra * soma_x2))
    c1 = (soma_x ** 2) / soma_amostra
    c2 = (soma_y ** 2) / soma_amostra
    tf = calculadora.produtos_notaveis_soma_diferença(soma_x2, c1, soma_y2, c2)
    r2 = ((soma_xy - (soma_x * (soma_y / soma_amostra))) ** 2) / tf


    """print(f'O valor de a é: {a}')
    print(f'O valor de b é: {b}')
    print(f'O coéficiente de determinação r² = {r2}')
    print(f'A equação da reta é f(x) = {a}x + {b}')
    equação = f'f(x) = {a}x + {b}'"""

    """y.clear()
    for v in x:
        y.append(a * v + b)

    if plotar == True:
        plt.plot(x, y)
        plt.title(f'Human papillomavirus type 32 \n{equação}')
        plt.show()"""

    return a * -1
