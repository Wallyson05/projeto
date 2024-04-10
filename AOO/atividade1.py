class Filme:
    # nome = ""
    # ano_lancamento = 0
    # nota = 0
    # duracao_minutos = 0
    # incluso_plano = False
    def __init__(self, nome, ano_lancamento, nota):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.nota = nota
        self.totalNota = 0
        self.avaliador = 0
    
    def __str__(self):
        return f'Filme: {self.nome}'
        
        
    def ficha_tecnica(self):
        print("===================\n")
        print(f"Dados do Filme {self.nome}:")
        print(f"Ano Lançamento: {self.ano_lancamento}")
        print(f"Nota: {self.nota}")
        
    # Avaliar filme
    def avalia(self, nota):
        self.totalNota += nota
        self.avaliador += 1
    
    # Média de avaliação
    def media(self):
        print(f"Média do filme: {self.totalNota / self.avaliador}")

# Primeiro Filme
filme = Filme("Mario", 2023, 9.5)
filme.ficha_tecnica()
filme.avalia(8.5)
filme.avalia(9.0)
filme.media()