import speech_recognition as sr

class VozNaoReconhecida(Exception):
    pass

class ErroReconhecimentoVoz(Exception):
    pass

def reconhece_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale agora:")
        audio = r.listen(source)
    try:
        print("aguarde...")
        texto = r.recognize_google(audio, language="pt-BR")
        print("Você disse:", texto)
        return texto
    except sr.UnknownValueError:
        raise VozNaoReconhecida("Não foi possível entender o que você disse")
    except sr.RequestError:
        raise ErroReconhecimentoVoz("Erro ao solicitar reconhecimento de voz")
    
    
if __name__ == "__main__":
    print(reconhece_voz())
    # pip install -r requirements.txt