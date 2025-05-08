# import os
# import sys

# if os.name == 'nt':  # Windows
#     sys.stdout = open('NUL', 'w')
# else:  # Unix/Linux/Mac
#     sys.stdout = open('/dev/null', 'w')

import pygame
import sounddevice as sd
import numpy as np
import threading
import math
import actions

rodando = True

def desenhar_estrela(janela, cor, x, y, raio, pontas):
    angulo = 2 * math.pi / pontas
    pontos = []
    for i in range(pontas * 2):
        r = raio if i % 2 == 0 else raio / 2
        pontos.append((x + math.cos(i * angulo / 2) * r, y + math.sin(i * angulo / 2) * r))
    pygame.draw.polygon(janela, cor, pontos)

def activate():
    global rodando
    while rodando:
        rodando = actions.active_actions()

# Inicializa o Pygame
pygame.init()

# Cria uma thread para executar a função activate()
thread = threading.Thread(target=activate)
thread.daemon = True  # Isso garante que a thread seja fechada quando o programa principal for fechado
thread.start()

# Define as cores
preto = (0, 0, 0)
prateado = (192, 192, 192)

# Define o tamanho da janela
tamanho_janela = (600, 600)
janela = pygame.display.set_mode(tamanho_janela, pygame.NOFRAME)

# Define o centro da estrela
centro_x = tamanho_janela[0] // 2
centro_y = tamanho_janela[1] // 2

# Imprime a lista de dispositivos de áudio disponíveis
# print("Dispositivos de áudio disponíveis:")
# for i, device in enumerate(sd.query_devices()):
#     print(f"{i}: {device['name']}")

# Encontra o índice do dispositivo "Mixagem estéreo"
devices = sd.query_devices()
mixagem_estereo_index = None
for i, device in enumerate(devices):
    if "mixagem estéreo" in device["name"].lower():
        mixagem_estereo_index = i
        break

if mixagem_estereo_index is None:
    print("Dispositivo 'Mixagem estéreo' não encontrado")
else:
    print(f"Índice do dispositivo 'Mixagem estéreo': {mixagem_estereo_index}")

# Loop principal
with sd.InputStream(device=mixagem_estereo_index) as stream:
    while rodando:
        for evento in pygame.event.get():
            pass  # Não há eventos para processar, pois a janela não tem bordas

        # Lê o áudio
        data = stream.read(1024)[0]
        amplitude = np.abs(np.max(data)) * 200

        # Desenha a estrela
        janela.fill(preto)
        raio = int(amplitude)
        if raio > 200:
            raio = 200
        desenhar_estrela(janela, prateado, centro_x, centro_y, raio * 8, 30)

        # Atualiza a janela
        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Fecha o Pygame
pygame.quit()

# python -m PyInstaller --onefile --windowed --icon=img/logo.ico main.py