import sqlite3

# 1 criando banco de dados
conexao = sqlite3.connect('titulo.bd')

cursor = conexao.cursor()
nome = input("Insira o nome do anime: ")
ano = int(input("Insira o ano do anime: "))
nota = float(input("Insira a nota do anime: "))
# 2 criação de tabela
cursor.execute(
    f'''
            INSERT INTO animes(nome, ano, nota)
            VALUES ('{nome}', {ano}, {nota})
    '''
)
conexao.commit()
conexao.close()
print("Tabela criada")