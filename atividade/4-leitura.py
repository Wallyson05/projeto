import sqlite3

# 1 criando banco de dados
conexao = sqlite3.connect('titulo.bd')

cursor = conexao.cursor()

# 2 criação de tabela
dados = cursor.execute(
    '''
          SELECT * FROM animes
    '''
)
print(dados.fetchall())