def matrix(v, c, r):
    """
    matrix : Matriz
    v : Valor qualquer
    c : Inteiro
    r : Inteiro

    Essa função retornará uma matriz com o nº
    de linhas r e o nº de colunas c, preenchidos
    com o valor v. /diego
    """

    return [[v]*c for _ in range(r)]


def char_to_int(c):
    """
    char_to_int : Inteiro
    c : Caractere

    Essa função pega como parâmetro um caractere e 
    retorna um inteiro equivalente à sua posição na matriz. /diego
    """
    alpha = 'ABCDEFGHI'

    return alpha.index(c.upper())


def check_input(s):
    """
    s : String
    check_input : Booleano

    Essa função retornará VERDADEIRO caso
    a entrada do usuário tenha a intenção de
    inserir um valor na grade, e FALSO caso
    tenha a intenção de deletar um valor na grade. /marcelo
    """
    if ':' in s:
        return True
    else:
        return False


def take_delete(s):
    """
    s : String
    take_delete : Vetor de inteiros

    Essa função retornará a posição que
    o jogador pretende deletar o valor
    na grade do jogo. /marcelo
    """

    v=[None]*2
    s = s.replace(' ','')
    v[1] = s[1:s.index(',')]
    v[0] = int(s[s.index(',')+1:]) - 1
    return v


def take_play(s):
    """
    take_input : Vetor de inteiros
    s : String

    Essa função pegará uma string de jogada e
    retornará um vetor com as informações contidas
    nela. /jonathan
    """

    s = s.replace(" ","")

    v = [None] * 3
    v[1] = s[0:s.index(',')]
    v[0] = int(s[s.index(',')+1:s.index(':')]) - 1
    v[2] = int(s[s.index(':')+1:])
    
    return v


def is_play_valid(m, v):
    """
    is_play_valid : Booleano
    m : Matriz de inteiros
    v : Vetor de inteiros

    Essa função pegará uma matriz 9x9 e um vetor 1x3,
    e checará se há elementos na linha de valor v[0], coluna
    de valor v[1] ou na região 3x3 que contém a posição indicada
    iguais ao terceiro valor de v. Caso sim, retornará FALSO,
    e caso contrário, retornará VERDADEIRO. /jonathan
    """
    if v[0] > 8 or v[0] < 0:
        return False
    elif v[2] > 9 or v[2] < 1:
        return False
    elif len(v[1]) > 1:
        return False
    elif v[1] not in 'ABCDEFGH':
        return False
    else:
        for s in m[v[0]]:
            if s == v[2]:
                return False

        for i in range(9):
            if m[i][char_to_int(v[1])] == v[2]:
                return False

        r = 3*(v[0]//3)
        c = 3*(char_to_int(v[1])//3)
        
        for i in range(3):
            for j in range(3):
                if m[i + r][j + c] == v[2]:
                    return False
    
    return True


def check_hint(m):
    """
    check_hint : Matriz de booleanos
    m : Matriz de inteiros

    Essa função retornará uma matriz de booleanos,
    onde terá valor VERDADEIRO quando o valor de m[i][j] for
    diferente de None. /jonathan
    """
    
    n = matrix(False, 9, 9)

    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] != None:
                n[i][j] = True
    
    return n


def print_grid(m):
    """
    print_grid : String
    m : Matriz de inteiros

    Esse procedimento irá imprimir a grade
    do sudoku da forma que é pedido
    no arquivo em PDF. /marcelo
    """

    for i in range(9):
        for j in range(9):
           if m[i][j]==None:
               m[i][j]= ' '

    print('    A   B   C    D   E   F    G   H   I')
    print(' ++---+---+---++---+---+---++---+---+---++')
    print(f'1|| {m[0][0]} | {m[0][1]} | {m[0][2]} || {m[0][3]} | {m[0][4]} | {m[0][5]} || {m[0][6]} | {m[0][7]} | {m[0][8]} ||1')
    print(' ++---+---+---++---+---+---++---+---+---++')
    print(f'2|| {m[1][0]} | {m[1][1]} | {m[1][2]} || {m[1][3]} | {m[1][4]} | {m[1][5]} || {m[1][6]} | {m[1][7]} | {m[1][8]} ||2')
    print(' ++---+---+---++---+---+---++---+---+---++')
    print(f'3|| {m[2][0]} | {m[2][1]} | {m[2][2]} || {m[2][3]} | {m[2][4]} | {m[2][5]} || {m[2][6]} | {m[2][7]} | {m[2][8]} ||3')
    print(' ++===+===+===++===+===+===++===+===+===++') 
    print(f'4|| {m[3][0]} | {m[3][1]} | {m[3][2]} || {m[3][3]} | {m[3][4]} | {m[3][5]} || {m[3][6]} | {m[3][7]} | {m[3][8]} ||4')
    print(' ++---+---+---++---+---+---++---+---+---++')
    print(f'5|| {m[4][0]} | {m[4][1]} | {m[4][2]} || {m[4][3]} | {m[4][4]} | {m[4][5]} || {m[4][6]} | {m[4][7]} | {m[4][8]} ||5')
    print(' ++---+---+---++---+---+---++---+---+---++')
    print(f'6|| {m[5][0]} | {m[5][1]} | {m[5][2]} || {m[5][3]} | {m[5][4]} | {m[5][5]} || {m[5][6]} | {m[5][7]} | {m[5][8]} ||6')
    print(' ++===+===+===++===+===+===++===+===+===++')
    print(f'7|| {m[6][0]} | {m[6][1]} | {m[6][2]} || {m[6][3]} | {m[6][4]} | {m[6][5]} || {m[6][6]} | {m[6][7]} | {m[6][8]} ||7')
    print(' ++---+---+---++---+---+---++---+---+---++')
    print(f'8|| {m[7][0]} | {m[7][1]} | {m[7][2]} || {m[7][3]} | {m[7][4]} | {m[7][5]} || {m[7][6]} | {m[7][7]} | {m[7][8]} ||8')
    print(' ++---+---+---++---+---+---++---+---+---++')
    print(f'9|| {m[8][0]} | {m[8][1]} | {m[8][2]} || {m[8][3]} | {m[8][4]} | {m[8][5]} || {m[8][6]} | {m[8][7]} | {m[8][8]} ||9')
    print(' ++---+---+---++---+---+---++---+---+---++')
    print('   A   B   C    D   E   F    G   H   I')


def is_grid_valid(m):
    """
    m : Matriz de inteiros
    is_grid_valid : Booleano

    Essa função retornará VERDADEIRO caso a matriz
    oriunda das dicas estiver de acordo com o jogo,
    e retornará FALSO caso contrário. /diego
    """

    for i in range(9):
        for j in range(9):
            v = m[i][j]
            if v != None:
                for k in range(9):
                    if j != k:
                        if m[i][k] == v:
                            return False
                    if i != k:
                        if m[k][j] == v:
                            return False
                r = 3*(i//3)
                c = 3*(j//3)
                for k in range(3):
                    for l in range(3):
                        if (k + r) != i and (l + c) != j:
                            if m[k + r][l + c] == v:
                                return False
    
    return True


def check_full(m):
    """
    m : Matriz de inteiros
    check_full : Booleano

    Essa função retornará VERDADEIRO caso
    a matriz esteja cheia, e FALSO caso
    contrário. /diego
    """
    c = 0
    for i in range(9):
        for j in range(9):
            if type(m[i][j]) != int:
                c += 1
    if c == 0:
        return True
    else:
        return False


def print_banner():
    print('''
*-------------------------------------------------------------------------------*
|                                                                               |
|    ███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗   ██████╗ ██╗   ██╗    |
|    ██╔════╝██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║   ██╔══██╗╚██╗ ██╔╝    |
|    ███████╗██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║   ██████╔╝ ╚████╔╝     |
|    ╚════██║██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║   ██╔═══╝   ╚██╔╝      |
|    ███████║╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██╗██║        ██║       |
|    ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝        ╚═╝       |
|                                                                               |
|                                                                               |
|                              feito com o <3                                   |
|                                                                               |
*-------------------------------------------------------------------------------*
    ''')
