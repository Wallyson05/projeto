import sqlite3

# 1 criando banco de dados
conexao = sqlite3.connect('titulo.bd')
cursor = conexao.cursor()

# atualização
id = input("qual é o id do item que deseja atualizar? ")
nome = input("Qual o nome desejar inserir? ")
ano = input("Informe a data que deseja inserir: ")
nota = input("Informe a nota que deseja inserir: ")
cursor.execute(
    '''
   UPDATE filmes set nome = ?
    WHERE id = ?
    ''',
    (f"{nome}", id)
)
cursor.execute(
    '''
   UPDATE filmes set ano = ?
    WHERE id = ?
    ''',
    (f"{ano}", id)
)
cursor.execute(
    '''
   UPDATE filmes set nota = ?
    WHERE id = ?
    ''',
    (f"{nota}", id)
)
conexao.commit()