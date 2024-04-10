import sqlite3

# 1 criando banco de dados
conexao = sqlite3.connect('titulo.bd')

cursor = conexao.cursor()

# 2 criação de tabela
cursor.execute(
    '''
        CREATE TABLE animes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL,
        ano INTENGER NOT NULL,
        nota REAL NOT NULL
        );

    '''
)
conexao.close()
print("Tabela Foi Criada")