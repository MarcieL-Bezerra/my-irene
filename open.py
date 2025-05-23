from openai import OpenAI

# Conecta ao cliente LM Studio
client = OpenAI(base_url="http://localhost:8080/v1", api_key="lm-studio")

# Define uma função para obter a resposta da IA
def get_ai_response(pergunta: str,type):
    # Define o contexto e o tom da conversa
    system_message = {"role": "system", "content": f"Você é um {type}"}
    user_message = {"role": "user", "content": pergunta}

    response = client.chat.completions.create(
        model="lmstudio-community/qwen2.5-7b-instruct",
        messages=[system_message, user_message],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        # Pergunta ao usuário
        pergunta = input("Faça uma pergunta: ")

        # Obtém a resposta da IA
        resposta = get_ai_response(pergunta)

        # Imprime a resposta
        print("Resposta da IA:", resposta)


