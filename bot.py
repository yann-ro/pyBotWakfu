import pyautogui as gui
import time

import bot.mine as min
import bot.capchat as cap
from bot.config import Config

config = Config()

while True :
    if cap.find('chatStart',0.8, screen=config.screen_reduced)!=None:
        cap.capChat()
        time.sleep(2)
        gui.press('esc')
    else :
        min.mine(config.ore)