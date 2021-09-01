import pyautogui
import time

pyautogui.alert('O codigo vai começar. Não use nada do seu computador enquanto o codigo estiver rodando. ')
pyautogui.PAUSE = 0.7

# abrir o google drive no meu computador.
pyautogui.press('winleft')
pyautogui.write('google chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

# entrar na minha area de trabalho.
pyautogui.hotkey('winleft', 'd')

# cliquei no arquivo que eu quero fazer o backup e arrastei ele.
pyautogui.moveTo(1486, 45)
pyautogui.mouseDown()
pyautogui.moveTo(987, 704)

# enquanto arrasto eu clico no google drive.
pyautogui.hotkey('alt', 'tab')
time.sleep(3)

# soltei o arquivo no google drive.
pyautogui.mouseUp()

# esperar 5 segundos.
time.sleep(5)

pyautogui.alert("O codigo acabou de terminar. Já pode usar o computador.!!! ")
