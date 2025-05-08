import re

def remove_Text(text):
    linhas = text.split('\n')
    codigo = []
    for linha in linhas:
        linha_strip = linha.strip()
        if linha_strip and (any(c in linha_strip for c in ['(', ')', '[', ']', '{', '}', '=', '+', '--', '*', '/', '%', '<', '>']) or 
                            linha_strip.startswith(('import', 'try', 'except', 'with', 'print', 'if', 'else', 'for', 'while', 'def', 'class', 'return'))):
            codigo.append(linha)
    return '\n'.join(codigo)

def salvar_resultado(arquivo_caminho, resultado):
    with open(arquivo_caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write(resultado)
if __name__ == "__main__":
    text = """Aqui está um exemplo simples de um jogo de Pedra, Papel e Tesoura em Python:
import random
def jogo_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    vitorias_jogador = 0
    vitorias_computador = 0
    while True:
        escolha_jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para sair do jogo): ").lower()
        if escolha_jogador == "sair":
            break
        elif escolha_jogador not in opcoes:
            print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
            continue
        escolha_computador = random.choice(opcoes)
        print(f"\nVocê escolheu {escolha_jogador}, o computador escolheu {escolha_computador}.\n")
        if escolha_jogador == escolha_computador:
            print(f"Empate!")
        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
             (escolha_jogador == "tesoura" and escolha_computador == "papel") or \
             (escolha_jogador == "papel" and escolha_computador == "pedra"):
            print("Você ganhou!")
            vitorias_jogador += 1
        else:
            print("O computador ganhou!")
            vitorias_computador += 1
        print(f"\nPlacar: Você {vitorias_jogador} x {vitorias_computador} Computador\n")
    print("Jogo encerrado.")
if __name__ == "__main__":
    jogo_pedra_papel_tesoura()
Esse código permite que o jogador escolha entre pedra, papel e tesoura, e o computador faz uma escolha aleatória. O resultado do jogo é determinado pelas regras padrão do Pedra, Papel e Tesoura:
- Pedra ganha de Tesoura
- Tesoura ganha de Papel
- Papel ganha de Pedra
O jogo continua até que o jogador escolha sair. O placar é exibido após cada rodada."""
    # print(remove_Text(text))
    resultado = remove_Text(text)
    # print(resultado)
    salvar_resultado(resultado)
