# 🤖 Automação de Tarefas (script de exemplo)

Projeto simples em Python para automatizar ações na interface (ex.: envio de e-mail via Gmail) usando `pyautogui`.

## Visão geral

Este repositório contém um script demonstrativo, `codigo_automatizado.py`, que automatiza a abertura do Gmail e o envio de um e-mail usando controles do sistema (cliques e teclas). O objetivo é fornecer uma base genérica que qualquer pessoa possa adaptar para automatizar outras tarefas na interface gráfica.

## Arquivos principais

- `codigo_automatizado.py`: script principal de automação. Contém funções para abrir o navegador, localizar/acionar elementos por imagem ou coordenadas, compor e enviar e-mails.
- `obter_coordenadas.py` (opcional): utilitário sugerido para capturar coordenadas da tela (se presente no repositório).

## Requisitos

- Python 3.8+
- Pacotes Python:
  - `pyautogui` — automação de mouse/teclado
  - `pillow` — manipulação de imagens (dependência do pyautogui)
  - `opencv-python` — necessário caso queira usar detecção por imagem com `confidence` (opcional, mas recomendado)

Instalação rápida:

```bash
python -m pip install --upgrade pip
pip install pyautogui pillow opencv-python
```

Observação: no Windows pode ser necessário instalar pacotes adicionais de dependências ou bibliotecas do sistema para o OpenCV.

## Configuração

Edite as constantes no início de `codigo_automatizado.py` conforme seu ambiente:

- `URL_GMAIL`: URL a abrir (padrão: Gmail). Você pode apontar para outra URL se estiver automatizando outra tarefa.
- `EMAIL_DESTINATARIO`, `ASSUNTO_EMAIL`, `CORPO_EMAIL`: valores-padrão para o envio.
- `COMPOSE_COORDS`: coordenadas X,Y do botão/elemento a ser clicado (útil quando a busca por imagem não for confiável).
- `COMPOSE_IMAGE`: caminho para a imagem do botão (PNG) — quando preenchido, o script tenta localizar o elemento por imagem na tela.
- `USE_START_MENU` e `BROWSER_NAME`: modo alternativo de abrir navegador via menu Iniciar (apenas Windows).
- Tempos de espera (`SHORT_WAIT`, `MEDIUM_WAIT`, `LONG_WAIT`) podem ser ajustados se a máquina for lenta/rápida.

Dicas para obter coordenadas e imagens confiáveis:

- Use um utilitário de captura de coordenadas (ex.: `obter_coordenadas.py`) ou a função `pyautogui.position()` em um console Python.
- Para `COMPOSE_IMAGE`, faça screenshots do botão em alta resolução e com o mesmo tema/zoom do navegador.
- Teste a função de localização por imagem com diferentes valores de `confidence` (ex.: 0.7–0.95) e escolha o equilíbrio entre precisão e sensibilidade.

## Uso

1. Configure as constantes no arquivo `codigo_automatizado.py`.
2. Instale dependências conforme descrito acima.
3. Execute o script:

```bash
python codigo_automatizado.py
```

4. O script perguntará se você quer editar destinatário/assunto/corpo antes de enviar e pedirá confirmação antes de abrir o navegador.

Importante: durante a execução o PyAutoGUI controla mouse e teclado — não toque no mouse/teclado até a conclusão ou você pode interromper a automação.

## Segurança e boas práticas

- Não use este script para ações que envolvam dados sensíveis sem proteção (senhas, tokens, etc.).
- Teste em uma conta de e-mail de desenvolvimento antes de usar em produção.
- Ative `pyautogui.FAILSAFE = True` (já configurado no script) — mova o mouse para o canto superior esquerdo para abortar rapidamente.
- Faça backups de dados e evite rodar automações com privilégios elevados desnecessários.

## Troubleshooting

- Problema: botão não encontrado pela imagem — solução: atualize `COMPOSE_IMAGE` com uma captura maior/mais precisa ou use `COMPOSE_COORDS`.
- Problema: script muito rápido/rápido demais — solução: aumente `PAUSE_INTERVAL` e valores de `SHORT_WAIT/MEDIUM_WAIT`.
- Problema: `pyautogui.locateCenterOnScreen` exige `opencv` para o parâmetro `confidence` — instale `opencv-python`.

## Como adaptar para outras tarefas

- Substitua `URL_GMAIL` por qualquer página alvo e ajuste as sequências de teclas/cliques.
- Extraia funções reutilizáveis (ex.: `abrir_url()`, `clicar_por_imagem_ou_coordenada()`, `preencher_formulario()`), e crie novos módulos para cada tipo de fluxo.
- Para automações mais robustas, considere usar APIs (quando disponíveis) ao invés de automação de interface.