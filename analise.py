def verificacao():
    img_falha = []
    while True:
        escolha = input('\nTodas os linfócitos foram identificados  corretamente [S/N]: ').upper().strip()[0]
        while True:
            if escolha in 'SN':
                break
            if escolha not in 'SN':
                escolha = input('A opção foi digitada errada só é aceito "S" para sim e "N" para não! \nTodas as imagens foram cortadas corretamente [S/N]: ').upper().strip()[0]
                if escolha in 'SN':
                    break
        if escolha == 'S':
            break
        if escolha == 'N':
            while True:
                img = input('Informe o número das fotomicrografias que não foram processadas corretamente. \nDigite "P" para PARAR: ').upper().strip()
                if img != 'P':
                    img_falha.append(int(img))
                if img == 'P':

                    break
            break

    return img_falha