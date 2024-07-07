import dados_amostra
from time import sleep
resultados = []

def tabela_1(resultados):
    for i in resultados:
        print(f"\n{'-' * 24} "
              f"\n{'|'} {i[0]:^20} {'|'}"
              f"\n{'-' * 24} "
              f"\n{'|'} {i[1]:^20} {'|'}")
        print('-' * 24)
        for e in i[2]:
            print(f'{"|"} {e:^20} {"|"}', end='\n')

def tabela_2(resultados):
    print(f"\n{'-' * 44} "
          f"\n{'|'} {resultados[0][0]:^40} {'|'}"
          f"\n{'-' * 44} "
          f"\n{'|'} {resultados[0][1]:^18} "
          f"{'|'} {resultados[1][1]:^19} {'|'}")
    print('-' * 44)
    for i in range(len(resultados[0][2])):
        print(f'{"|"} {resultados[0][2][i]:^18} '
              f'{"|"} {resultados[1][2][i]:^19} {"|"}', end='\n')

def tabela_3(resultados):
    print(f"\n{'-' * 64} "
          f"\n{'|'} {resultados[0][0]:^60} {'|'}"
          f"\n{'-' * 64} "
          f"\n{'|'} {resultados[0][1]:^18} "
          f"{'|'} {resultados[1][1]:^18} "
          f"{'|'} {resultados[2][1]:^18} {'|'}")
    print('-' * 64)
    for i in range(len(resultados[0][2])):
        print(f'{"|"} {resultados[0][2][i]:^18} '
              f'{"|"} {resultados[1][2][i]:^18} '
              f'{"|"} {resultados[2][2][i]:^18} {"|"}', end='\n')

while True:
    dados = dados_amostra.dados()
    resultados.append([dados['nome_amostra'],
                       (dados['tipo_amostra']),
                       dados['dimenção_fractal']])

    sair = input('\nDeseja sair? [S/N]: ').upper().strip()

    if sair == 'S':
        break
    else:
        continuar = input('Deseja acrescentar amostra? [S/N]: ').upper().strip()
        if continuar == 'S':
            print('\n')
        else:
            break

if len(resultados) == 1:
    tabela_1(resultados)
    while True:
        esc = input('\nConcluir Análise? [S/N]: ').upper().strip()
        if esc == 'S':
            print('ENCERRANDO' , end='')
            sleep(1)
            for i in range(3):
                print('.', end='')
                sleep(1)
            break

elif len(resultados) == 2:
    tabela_2(resultados)
    while True:
        esc = input('\nConcluir Análise? [S/N]: ').upper().strip()
        if esc == 'S':
            print('ENCERRANDO' , end='')
            sleep(1)
            for i in range(3):
                print('.', end='')
                sleep(1)
            break

elif len(resultados) == 3:
    tabela_3(resultados)
    while True:
        esc = input('\nConcluir Análise? [S/N]: ').upper().strip()
        if esc == 'S':
            print('ENCERRANDO' , end='')
            sleep(1)
            for i in range(3):
                print('.', end='')
                sleep(1)
            break


