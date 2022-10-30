from funcoes import *
from sys import argv

sudoku_grid = matrix(None, 9, 9)  # Inicialização da matriz do jogo /diego
boolean_grid = matrix(False, 9, 9)  # Inicialização da matriz de booleanos /jonathan
is_game_valid = True  # Incialização da variável que diz se a configuração inicial está válida /diego
counter = 0  # Inicialização da variável de contagem das pistas /diego

# Definindo o modo de jogo, com True -> Interativo e False -> Batch /diego
if len(argv) == 2:
    game_mode = True
else:
    game_mode = False

# Pegando os dados do arquivo e colocando da matriz /diego
with open(argv[1]) as cfg:
    for line in cfg:
        if line != '\n':
            cfg_position = take_play(line)
            cfg_position[1] = char_to_int(cfg_position[1])
            sudoku_grid[cfg_position[0]][cfg_position[1]] = cfg_position[2]

boolean_grid = check_hint(sudoku_grid)
is_game_valid = is_grid_valid(sudoku_grid)

# Aumentando o valor da variável counter para cada elemento da matriz que não é uma dica. /diego
for i in range(9):
    for j in range(9):
        if boolean_grid[i][j]:
            counter += 1

# Verificando se a quantidade de dicas está correta. /diego
if not (80 >= counter >= 1):
    is_game_valid = False

# Printando a matriz /marcelo
if game_mode:
    print_banner()
    print_grid(sudoku_grid)
play = ''  # String da jogada /diego

if not is_game_valid:
    print('Configuracao de dicas invalida.')
else:
    if game_mode:
        # Modo interativo

        while True:
            # Verificando se a matriz está cheia
            # (usamos o break já que não existe o 
            # do while no python...) /diego
            if not check_full(sudoku_grid):
                play = input()
                user_option = check_input(play)  # Verificando qual opção que o jogador deseja tomar /marcelo
                if user_option:
                    # Vetor que contém a coluna, a linha e o valor entrados pelo jogador:
                    # A posição 0 contém a linha, a posição 1 contém a coluna,
                    # e a posição 2 contém o valor a ser inserido /jonathan
                    user_data = take_play(play)

                    # Utilizando a função is_play_valid, essa estrutura verificará
                    # se a jogada do jogador é válida /jonathan
                    if is_play_valid(sudoku_grid, user_data):
                        user_data[1] = char_to_int(user_data[1])
                        if not boolean_grid[user_data[0]][user_data[1]]:
                            sudoku_grid[user_data[0]][user_data[1]] = user_data[2]
                            print_grid(sudoku_grid)
                    else:
                        print('Nao eh possivel fazer essa jogada.')
                else:
                    user_delete = take_delete(play)  # Posição que o jogador quer deletar /marcelo
                    # Verificando se a posição é válida /marcelo
                    if (user_delete[0] < 0 or user_delete[0] > 8) or (len(user_delete[1]) > 1):
                        print('Posicao invalida.')
                    else:
                        user_delete[1] = char_to_int(user_delete[1])
                        # Vendo se a célula é uma dica /marcelo
                        if not boolean_grid[user_delete[0]][user_delete[1]]:
                            # Vendo se a célula está vazia /marcelo
                            if type(sudoku_grid[user_delete[0]][user_delete[1]]) == int:
                                sudoku_grid[user_delete[0]][user_delete[1]] = None
                                print_grid(sudoku_grid)
                            else:
                                print('Nao eh possivel deletar uma celula vazia.')
                        else:
                            print("Nao eh possivel deletar uma dica.")
            else:
                break
        print('Parabens! Voce completou o jogo.')
    else:
        # Modo Batch

        # Pegando os dados do arquivo de jogo /diego
        with open(argv[2]) as jog:
            for line in jog:
                if line != '\n':
                    batch_option = check_input(line)
                    if batch_option:
                        batch_play = take_play(line)
                        # Novamente, utilizamos a função is_play_valid para validar a jogada /diego
                        if is_play_valid(sudoku_grid, batch_play):
                            batch_play[1] = char_to_int(batch_play[1])
                            if not boolean_grid[batch_play[0]][batch_play[1]]:
                                sudoku_grid[batch_play[0]][batch_play[1]] = batch_play[2]
                        else:
                            print(f'A jogada ({batch_play[1]},{batch_play[0]+1}) = {batch_play[2]} eh invalida!')
                    else:
                        batch_delete = take_delete(line)
                        if (batch_delete[0] < 0 or batch_delete[0] > 8) or (len(batch_delete[1]) > 1):
                            print(f'A jogada D({batch_delete[1]},{batch_delete[0]+1}) eh invalida!')
                        else:
                            # Vendo se a célula é uma dica /marcelo
                            if not boolean_grid[batch_delete[0]][char_to_int(batch_delete[1])]:
                                # Vendo se a célula está vazia /marcelo
                                if type(sudoku_grid[batch_delete[0]][char_to_int(batch_delete[1])]) == int:
                                    sudoku_grid[batch_delete[0]][char_to_int(batch_delete[1])] = None
                                else:
                                    print(f'A jogada D({batch_delete[1]},{batch_delete[0]+1}) eh invalida!')
                            else:
                                print(f'A jogada D({batch_delete[1]},{batch_delete[0]+1}) eh invalida!')
        if check_full(sudoku_grid):
            print('A grade foi preenchda com sucesso!')
        else:
            print('A grade foi nao foi preenchida!')
