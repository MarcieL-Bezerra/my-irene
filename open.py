import requests
import json

# Define uma função para obter a resposta da IA
def get_ai_response(pergunta: str, type):
    # Define o contexto e o tom da conversa
    payload = {
        "model": "hermes-3-llama-3.2-3b",
        "messages": [
            {"role": "system", "content": f"Seu nome é Irene, Você é um {type}"},
            {"role": "user", "content": pergunta}
        ],
        "temperature": 0.7,
        "max_tokens": 2048
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("http://localhost:8080/v1/chat/completions", headers=headers, data=json.dumps(payload))
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    type = input("Qual o tipo de assistente você deseja? ")
    while True:
        # Pergunta ao usuário
        pergunta = input("Faça uma pergunta: ")
        # Obtém a resposta da IA
        resposta = get_ai_response(pergunta, type)
        # Imprime a resposta
        print("Resposta da IA:", resposta)


