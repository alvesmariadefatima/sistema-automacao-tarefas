import pyautogui
import time

print("=" * 60)
print("OBTENEDOR DE COORDENADAS DO MOUSE")
print("=" * 60)
print("\nMova o mouse para a posição desejada e as coordenadas")
print("serão exibidas em tempo real.")
print("\nPressione Ctrl+C para interromper o programa.\n")
print("-" * 60)

try:
    while True:
        # Obtém a posição atual do mouse
        x, y = pyautogui.position()
        
        # Limpa a linha anterior e mostra a nova posição
        print(f"Coordenadas do mouse: X = {x}, Y = {y}", end="\r")
        
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\n" + "-" * 60)
    print("Programa interrompido!")
    print("Use as coordenadas obtidas no seu script.")
    print("=" * 60)
