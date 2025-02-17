import numpy as np

def calcular_sus(respostas):
    """
    Calcula a pontuação SUS para um conjunto de respostas.
    :param respostas: Lista de listas, onde cada sublista contém as 10 respostas de um participante.
    :return: Pontuações individuais e a média SUS
    """
    pontuacoes = []
    
    for resposta in respostas:
        if len(resposta) != 10:
            raise ValueError("Cada participante deve ter exatamente 10 respostas.")
        
        # Ajuste das respostas
        ajuste = [(resposta[i] - 1) if i % 2 == 0 else (5 - resposta[i]) for i in range(10)]
        
        # Soma os valores ajustados e multiplica por 2.5
        score = sum(ajuste) * 2.5
        pontuacoes.append(score)
    
    media_sus = np.mean(pontuacoes)
    return pontuacoes, media_sus

# Exemplo de respostas de participantes (substituir com dados reais)
respostas_exemplo = [
    [5, 1, 4, 2, 5, 1, 3, 2, 5, 3],  # Participante 1
    [3, 3, 4, 2, 3, 3, 4, 2, 3, 3],  # Participante 2
    # Adicione mais listas para os demais participantes
]

# Cálculo da pontuação
pontuacoes, media_sus = calcular_sus(respostas_exemplo)

# Exibir resultados
print("Pontuações individuais SUS:", pontuacoes)
print("Média SUS geral:", round(media_sus, 2))
