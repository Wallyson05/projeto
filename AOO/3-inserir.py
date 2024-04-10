import sqlite3

# 1 criando banco de dados
conexao = sqlite3.connect('titulo.bd')

cursor = conexao.cursor()
nome = input("Insira o nome do filme: ")
ano = int(input("Insira o ano do filme: "))
nota = float(input("Insira a nota do filme: "))
# 2 criação de tabela
cursor.execute(
    f'''
            INSERT INTO filmes(nome, ano, nota)
            VALUES ('{nome}', {ano}, {nota})
    '''
)
conexao.commit()
conexao.close()
print("Tabela criada")