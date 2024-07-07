from tkinter import *
from PIL import ImageTk, Image
from carregar_abrir_converter_imagem import carregar_imagem, abrir_imagem


def imagem_corte(direc):

    valor = []

    def novo_retangulo(e):
        x, y = c.canvasx(e.x), c.canvasy(e.y)
        c.create_rectangle(x, y, x, y, tags="corrente")

    def estende_retangulo(e):
        x2, y2 = c.canvasx(e.x), c.canvasy(e.y)
        coords = c.coords("corrente")
        coords[2] = x2
        coords[3] = y2
        c.coords("corrente", *coords)

    def coordenadas():
        cord = c.coords('corrente')
        valor.append(cord)
        #print(valor)

    def apagar(e):
        c.delete('corrente')

    abrir_img = abrir_imagem(direc)
    medidas = ((abrir_img.size)[0] / 4, (abrir_img.size)[1] / 4)


    c = Canvas(width=medidas[0], height=medidas[1])
    c.pack()

    cortar = Button(text='CORTE',  height=2, width=8, command=coordenadas)
    cortar.pack()

    redimensionar = abrir_img.resize((int(medidas[0]), int(medidas[1])), Image.ANTIALIAS)

    img = ImageTk.PhotoImage(redimensionar)
    c.create_image(0, 0, image=img, anchor=NW)
    c.pack()

    c.bind("<Button-1>", novo_retangulo)
    c.bind("<B1-Motion>", estende_retangulo)
    c.bind("<Double-Button-1>", apagar)

    c.mainloop()
    return valor

