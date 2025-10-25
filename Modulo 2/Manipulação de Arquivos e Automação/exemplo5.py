import pyautogui
import webbrowser
import time

#passo 1: abrir o youtube com uma musica especifica
url="https://youtu.be/TCkILf3jYdk?si=bZEDRcU4mtlvLCQA"
webbrowser.open(url)

#aguardar o carregamento da pagina 
time.sleep(5) #ajustar de acordo com a velocidade da internet utilizada

#garantir que o video comece (apertar o espaço para o play)
pyautogui.press("space") #toca ou pausa o video