#Crie um programa que use um comando com o Pyautogui
#para abrir a calculadora do Windows e faça um calculo de 8
#+ 2 e apresente o resultado.

import pyautogui
import time

time.sleep(1)
pyautogui.hotkey("win","r")
pyautogui.sleep(1)
pyautogui.typewrite("calc")
pyautogui.press("enter")
time.sleep(1)

pyautogui.typewrite("8+2")
pyautogui.press("enter")
time.sleep(1)

pyautogui.typewrite("8-2")
pyautogui.press("enter")
time.sleep(1)

pyautogui.typewrite("8*2")
pyautogui.press("enter")
time.sleep(1)