import pyautogui as py
import time
import keyboard
import win32api
import win32con
import os
from tkinter import *
time.sleep(2)
c = 0
def interromper():
    if jogo is not None:
        # Cancelar a execução da função
        janela.after_cancel(jogo_id)
        jogo_id = None
jogo_id = None

def detect():
    global largura_monitor,altura_monitor,proporção_de_x,proporção_de_y
    largura_monitor,altura_monitor = py.size()
    largura_proporcional = largura_monitor/1920
    altura_proporcional = altura_monitor/1080

    proporção_de_x = int(584*largura_proporcional)
    proporção_de_y = int(430*altura_proporcional)
def fazer_clique(x, y):          
    global c
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    #os.system('cls')
    c = c +1
    print(f'Clicks totais:{c}')
    jogo()
def jogo():
    while keyboard.is_pressed('q') == False:
        flag = 0
        sc = py.screenshot(region=(proporção_de_x,proporção_de_y, 757,540))
        width, height = sc.size
        for x in range(0,width,8):
            for y in range(0,height,5):
                r,g,b = sc.getpixel((x,y))
                if b == 195 and r == 255 and g == 219:
                    fazer_clique(proporção_de_x+x,proporção_de_y+y)
                    flag = 1
                    time.sleep(0.05)
                    break
        if flag == 1: # essa condição faz o loop voltar desde o início. Isso evita miss click e clicks em alvos que
            break
detect()
janela = Tk()
janela.title("AimBoster AutoClick")
texto_inicial = Label(janela,text="Abra o jogo aimboster no seu monitor principal para funcionar")
texto_inicial.grid(column=0,row=0)
resolução =Label(janela,text=f"Resolução detectada: {largura_monitor}x{altura_monitor}").grid(column=0,row=1)
botao = Button(janela,text="JOGAR",command=jogo)
botao.grid(column=0,row=2)
botao_cancel = Button(janela,text="Parar",command=interromper)
botao_cancel.grid(column=0,row=3)
#criar um botão para detectar a resolução, e dps ela aparece na tela

janela.mainloop()
#c 480
