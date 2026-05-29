# main.py

import random
from logic import checar_palpite, criar_estado_inicial, atualizar_estado, GameState

def exibir_mensagem(resultado: str, tentativas: int):
    """Função impura para mostrar mensagens ao usuário."""
    mensagens = {
        'muito_baixo': 'Muito baixo!',
        'muito_alto': 'Muito alto!',
        'correto': 'Parabéns, você acertou!'
    }
    if resultado in mensagens:
        print(mensagens[resultado])
    
    if not resultado == 'correto' and tentativas > 0:
        print(f'Você tem {tentativas} tentativas restantes.')

def pedir_palpite_usuario() -> int:
    """Função impura para obter input do usuário."""
    while True:
        try:
            palpite = int(input('Digite seu palpite: '))
            return palpite
        except ValueError:
            print('Por favor, digite um número válido.')

def loop_do_jogo(estado: GameState):
    """
    O loop principal recursivo.
    A cada chamada, ele processa uma rodada e chama a si mesmo com o novo estado.
    """
    # Condição de parada da recursão
    if estado['fim_de_jogo']:
        if estado['tentativas_restantes'] > 0:
             print(f"Você venceu!")
        else:
             print(f"Fim de jogo! O número era {estado['numero_secreto']}.")
        return

    # 1. Obter input do usuário (Impuro)
    palpite = pedir_palpite_usuario()

    # 2. Usar a lógica pura para obter o resultado
    resultado = checar_palpite(estado['numero_secreto'], palpite)

    # 3. Usar a lógica pura para obter o novo estado
    proximo_estado = atualizar_estado(estado, resultado)
    
    # 4. Exibir o resultado (Impuro)
    exibir_mensagem(resultado, proximo_estado['tentativas_restantes'])

    # 5. Chamar o loop novamente com o estado atualizado
    loop_do_jogo(proximo_estado)

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    print("--- Adivinhe o Número (de 1 a 100) ---")
    
    # Ações impuras iniciais
    numero_secreto = random.randint(1, 100)
    tentativas_iniciais = 7
    
    # Cria o estado inicial usando a lógica pura
    estado_inicial = criar_estado_inicial(numero_secreto, tentativas_iniciais)
    
    # Inicia o jogo
    loop_do_jogo(estado_inicial)
