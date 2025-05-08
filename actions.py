import webbrowser
import os
import speech
import sound
import open
import codecreate

def active_actions():
    try:
        heard = speech.reconhece_voz()
        saindo = "sair"
        mywebbrowser = "navegador"
        criandoSistema = ["crie um código python", "crie um sistema em python", "em python", "com python", "o python"]
        if heard != None and saindo.lower() in heard.lower():
            response = "Certo, até logo."
            sound.texto_para_fala(response)
            return False
        elif heard != None and any(x.lower() in heard.lower() for x in criandoSistema):
            response = "Sim, claro."
            sound.texto_para_fala(response)
            result = open.get_ai_response(heard)
            print("criar pasta")
            create_sistem(result)
            response = "Por favor faça os ajustes necessários."
            sound.texto_para_fala(response)
            return True
        elif heard != None and mywebbrowser.lower() in heard.lower():
            response = "abrindo, navegador web."
            sound.texto_para_fala(response)
            open_browser()
            return True
        elif heard != None:
            response = open.get_ai_response(heard)
            sound.texto_para_fala(response)
            return True
    except speech.VozNaoReconhecida:
        print("Não foi possível entender o que você disse")
        return True        
    except speech.ErroReconhecimentoVoz:
        print("Erro ao solicitar reconhecimento de voz")
        return True        
    except:
        response = "No momento não consigo te responder"
        sound.texto_para_fala(response)
        return True


def open_browser():
    webbrowser.open('http://www.google.com')

def create_sistem(text):
    print("1")
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    print(desktop)
    pasta_nome = "sistema"
    pasta_caminho = os.path.join(desktop, pasta_nome)

    try:
        print(pasta_caminho)
        os.mkdir(pasta_caminho)
        print(f"Pasta '{pasta_nome}' criada com sucesso!")
    except:
        print(f"A pasta '{pasta_nome}' já existe!")

    result = codecreate.remove_Text(text)
    # Nome do arquivo
    arquivo_nome = "main.py"

    # Caminho completo do arquivo
    arquivo_caminho = os.path.join(pasta_caminho, arquivo_nome)

    codecreate.salvar_resultado(arquivo_caminho, result)
    # Criar o arquivo
    
    print(f"Arquivo '{arquivo_nome}' criado com sucesso!")

    # Abrir o arquivo
    os.startfile(arquivo_caminho)