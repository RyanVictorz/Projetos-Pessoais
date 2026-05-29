# logic.py

from typing import Literal, Dict, Any

# Define um tipo para o estado do jogo para maior clareza
GameState = Dict[str, Any]
GuessResult = Literal['muito_baixo', 'muito_alto', 'correto']

def checar_palpite(numero_secreto: int, palpite: int) -> GuessResult:
    """
    Compara o palpite com o número secreto e retorna o resultado.
    Esta é uma função 100% pura.
    """
    if palpite < numero_secreto:
        return 'muito_baixo'
    elif palpite > numero_secreto:
        return 'muito_alto'
    else:
        return 'correto'

def criar_estado_inicial(numero_secreto: int, tentativas: int) -> GameState:
    """
    Cria o dicionário que representa o estado inicial do jogo.
    Pura, pois apenas cria e retorna uma nova estrutura de dados.
    """
    return {
        "numero_secreto": numero_secreto,
        "tentativas_restantes": tentativas,
        "fim_de_jogo": False
    }

def atualizar_estado(estado: GameState, resultado: GuessResult) -> GameState:
    """
    Recebe o estado atual e o resultado do palpite, e retorna um NOVO estado.
    Isso é crucial: não modificamos o estado antigo (imutabilidade).
    """
    novo_estado = estado.copy() # Cria uma cópia para não alterar o original
    
    if resultado == 'correto':
        novo_estado['fim_de_jogo'] = True
        return novo_estado
    
    # Decrementa as tentativas
    novo_estado['tentativas_restantes'] -= 1
    
    # Verifica se as tentativas acabaram
    if novo_estado['tentativas_restantes'] <= 0:
        novo_estado['fim_de_jogo'] = True
        
    return novo_estado
