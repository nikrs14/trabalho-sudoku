# Trabalho Sudoku
## Trabalho final da cadeira de Fundamentos de Programação (CK0211)

---

## Como usar
A matriz do sudoku é uma matriz 8x8 com coordenadas que vão de A a H (colunas) e 1 a 8 (linhas). Nos arquivos texto, você terá em cada linha comandos do tipo `{y},{x}:{v}` com y e x sendo as coordenadas da célula a ser preenchida (colunas e linhas), e v o valor (ver exemplo em `arq_01_cfg.txt` ou `arq_01_jog.txt`).

Rodando `python3 sudoku.py {nome do arquivo de configuração}`, você jogará no modo interativo com os valores preenchidos de acordo com o arquivo. Suas jogadas serão da mesma forma das que estão no arquivo de configuração, além de poder deletar células usando o comando `D{y},{x}`. Rodando `python3 sudoku.py {nome do arquivo de configuração} {nome do arquivo de jogo}`, você entra no modo BATCH em que são jogadas em sequência as jogadas do arquivo de jogo.

---

**Trabalho feito em conjunto com mais dois colegas de classe.**

