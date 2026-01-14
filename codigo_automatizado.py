# ...existing code...
import time
import webbrowser
import pyautogui
import sys

# Configurações (edite conforme necessário)
URL_GMAIL = "https://mail.google.com"
EMAIL_DESTINATARIO = "destinatario@exemplo.com"
ASSUNTO_EMAIL = "Assunto padrão"
CORPO_EMAIL = "Corpo do email enviado automaticamente."
COMPOSE_COORDS = (105, 74)      # Coordenadas padrão do botão "Compose" (ajuste para sua tela)
COMPOSE_IMAGE = None            # Caminho para uma imagem do botão "Compose" (ex: "compose.png") ou None
USE_START_MENU = False          # Se True, usa menu Iniciar para abrir navegador (antigo método)
BROWSER_NAME = "edge"           # Usado apenas se USE_START_MENU=True
PAUSE_INTERVAL = 0.05
SHORT_WAIT = 2
MEDIUM_WAIT = 6
LONG_WAIT = 12

pyautogui.FAILSAFE = True
pyautogui.PAUSE = PAUSE_INTERVAL

def abrir_gmail(use_start_menu=USE_START_MENU, url=URL_GMAIL):
    """Abre o Gmail no navegador. Por padrão usa o navegador padrão do sistema."""
    if use_start_menu:
        # Abre navegador via menu iniciar (Windows) - método mais frágil, manter apenas se necessário
        pyautogui.press("win")
        time.sleep(1.0)
        pyautogui.write(BROWSER_NAME, interval=0.08)
        time.sleep(1.5)
        pyautogui.press("enter")
        time.sleep(LONG_WAIT)
        pyautogui.hotkey("win", "up")
        time.sleep(1.5)
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.8)
        pyautogui.write(url, interval=0.08)
        pyautogui.press("enter")
    else:
        # Método genérico e mais confiável: abrir URL no navegador padrão
        webbrowser.open(url)
    time.sleep(MEDIUM_WAIT)

def encontrar_e_clicar_compose(coords=COMPOSE_COORDS, image_path=COMPOSE_IMAGE, timeout=10):
    """Tenta localizar o botão Compose por imagem; se falhar usa coordenadas."""
    if image_path:
        start = time.time()
        while time.time() - start < timeout:
            try:
                pos = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            except Exception:
                pos = None
            if pos:
                pyautogui.click(pos)
                return True
            time.sleep(0.8)
    # fallback para coordenadas
    pyautogui.click(coords)
    return True

def enviar_email(destinatario=EMAIL_DESTINATARIO, assunto=ASSUNTO_EMAIL, corpo=CORPO_EMAIL,
                 compose_coords=COMPOSE_COORDS, compose_image=COMPOSE_IMAGE):
    """Compõe e envia um email usando teclas e cliques do sistema."""
    time.sleep(SHORT_WAIT)
    encontrar_e_clicar_compose(compose_coords, compose_image)
    time.sleep(SHORT_WAIT)

    # Preencher destinatário, assunto e corpo usando navegação por TAB
    pyautogui.write(destinatario, interval=0.04)
    time.sleep(0.5)
    pyautogui.press("tab")  # assunto
    time.sleep(0.4)
    pyautogui.write(assunto, interval=0.04)
    time.sleep(0.4)
    pyautogui.press("tab")  # corpo
    time.sleep(0.4)
    pyautogui.write(corpo, interval=0.02)
    time.sleep(0.6)
    pyautogui.hotkey("ctrl", "enter")  # enviar
    time.sleep(SHORT_WAIT)

def main():
    print("Script de automação de envio de email (Gmail)")
    resp = input("Deseja editar destinatário/assunto/corpo antes de enviar? (s/N): ").strip().lower()
    destinatario = EMAIL_DESTINATARIO
    assunto = ASSUNTO_EMAIL
    corpo = CORPO_EMAIL
    if resp == "s":
        d = input(f"Destinatário [{EMAIL_DESTINATARIO}]: ").strip()
        if d: destinatario = d
        s = input(f"Assunto [{ASSUNTO_EMAIL}]: ").strip()
        if s: assunto = s
        c = input(f"Corpo (enter para usar padrão): ").strip()
        if c: corpo = c

    confirm = input("Pronto para abrir o navegador e enviar o email? (s/N): ").strip().lower()
    if confirm != "s":
        print("Operação cancelada.")
        sys.exit(0)

    abrir_gmail()
    enviar_email(destinatario, assunto, corpo)
    print("Operação finalizada.")

if __name__ == "__main__":
    main()