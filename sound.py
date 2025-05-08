import pyttsx3

def texto_para_fala(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 190)
    engine.setProperty('voice', 'brazil')  # Define a voz para português brasileiro
    engine.say(texto)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        texto = input("Digite o texto que você deseja converter em fala: ")
        texto_para_fala(texto)