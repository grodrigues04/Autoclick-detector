import pyautogui as py
import time
from random import randint
import keyboard
import win32api
import win32con
time.sleep(2)
c = 0
clicks = 1  
def detect():
    global largura_monitor,altura_monitor,proporção_de_x,proporção_de_y  #Função que detecta a resolução do monitor
    largura_monitor,altura_monitor = py.size() 
    largura_proporcional = largura_monitor/1920                    #E calcula a proporção da tela para que os clicks funcionem em qualquer resolução
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
#659,129
def jogo():
    while not keyboard.is_pressed('Esc'):
        flag = 0
        j = randint(13,55)
        k = randint(13,55)
        width = 584
        height = 440
        sc = py.screenshot(region=(584,421, 757,555))
        sc.save(f'teste.png')
        for y in range(height,0,-k):    
            for x in range(0,width,j):
                r,g,b = sc.getpixel((x,y))
                #py.moveTo(x+width,y+height)
                if r==39 and g==39 and b==39:
                    fazer_clique(x+width,y+height)
                    print()
                    flag=+1
        if flag == 1:
            break
                
                    

    
jogo()