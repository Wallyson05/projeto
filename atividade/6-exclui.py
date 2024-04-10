import sqlite3

# 1 criando banco de dados
conexao = sqlite3.connect('titulo.bd')
cursor = conexao.cursor()

# atualização
id = input("qual é o id do item que deseja deletar? ")
cursor.execute(
    '''
    DELETE FROM animes
    WHERE id = ?

    ''',
    (id,)
)
conexao.commit()
print(f"O ID {id} foi Deletado da Tabela!")