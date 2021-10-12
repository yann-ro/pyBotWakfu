# Bib
import bot.mine as min
import bot.capchat as cap
import datas as dat
import pyautogui as gui

import time

ore = 'cuivre'
d = dat.Datas()

while True :
    if cap.find('chatStart',0.8, screen=d.screenReduced)!=None:
        cap.capChat()
        time.sleep(2)
        gui.press('esc')
    
    else :
        min.mine(ore)