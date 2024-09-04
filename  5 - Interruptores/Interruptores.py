import time
import random

# Função para simular o estado das lâmpadas
def simulate_lamps():
    # Definindo o estado inicial das lâmpadas (apagadas e frias)
    lamps = {
        'Lampada 1': 'desligada',
        'Lampada 2': 'desligada',
        'Lampada 3': 'desligada'
    }
    
    # Definindo aleatoriamente qual lâmpada será ligada por cada interruptor
    lamp_mapping = random.sample(lamps.keys(), len(lamps))
    
    return lamp_mapping

# Função para descobrir qual interruptor controla qual lâmpada
def discover_lamps():
    # Simula a configuração dos interruptores e lâmpadas
    lamp_mapping = simulate_lamps()
    
    print("Simulando interruptores e lâmpadas...")
    time.sleep(2)  # Espera para simular o tempo de reflexão
    
    # Estágio 1: Ligue o Primeiro Interruptor e Deixe-o Ligado por um Tempo
    print("Ligando o primeiro interruptor...")
    time.sleep(3)  # Simula o tempo durante o qual o interruptor está ligado
    
    # Desligue o Primeiro Interruptor e Ligue o Segundo Interruptor
    print("Desligando o primeiro interruptor e ligando o segundo interruptor...")
    time.sleep(2)  # Tempo para simular a mudança
    
    # Vamos "verificar" o estado das lâmpadas
    # Simulando a primeira verificação das lâmpadas após a mudança
    lamp_states = {
        'Lampada 1': 'desligada',
        'Lampada 2': 'desligada',
        'Lampada 3': 'desligada'
    }
    
    # Determinando qual lâmpada está quente (ligada e apagada) e qual está acesa
    for lamp in lamp_states.keys():
        if lamp_mapping[0] == lamp:
            lamp_states[lamp] = 'quente'  # Lâmpada que foi ligada primeiro e depois desligada
        elif lamp_mapping[1] == lamp:
            lamp_states[lamp] = 'acesa'  # Lâmpada que está acesa
    
    # Simulando a leitura das lâmpadas após a verificação
    print("Lâmpadas após a verificação:")
    for lamp, state in lamp_states.items():
        print(f"{lamp}: {state}")
    
    # A saída mostra a correspondência entre interruptores e lâmpadas
    print("\nConclusão:")
    for i, lamp in enumerate(lamp_mapping):
        if lamp_states[lamp] == 'quente':
            print(f"Interruptor 1 controla a {lamp}.")
        elif lamp_states[lamp] == 'acesa':
            print(f"Interruptor 2 controla a {lamp}.")
        else:
            print(f"Interruptor 3 controla a {lamp}.")
    
discover_lamps()
