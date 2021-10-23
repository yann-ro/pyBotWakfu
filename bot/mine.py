import pyautogui as gui
import time
from config import Config

def find(name, image_confidence, screen=(0,0,1920,1080)):
    
    image_name = f'/image/{name}.png'
    image_location = gui.locateCenterOnScreen(image_name,confidence=image_confidence,grayscale=True,region=screen)
    
    return image_location


def click_on(name,type_clic,image_confidence,zone_capture=(0,0,1920,1080)):
    
    
    
    location = find(name,image_confidence,screen=zone_capture)
    
    #gui.click(location, button=type_clic)
    if (location == None):
        status = 'search'
        #print('not found')
        return status
    else:         
        gui.click(location, button=type_clic)
        status = 'pickup'
        #print('found')
        return status


def mine(minerais):
    
    config = Config()

    for i in config.screen_sizes:
        status = click_on(minerais,'right',0.8,config.screen_sizes[str(i)])
        if status == 'pickup':
            break
    
    time.sleep(0.75)
    
    if status == 'pickup':
        click_on('pioche','left',0.8)
        time.sleep(3)
        
        if find('recolte', 0.9) != None :
            while find('recolte', 0.9) != None :
                time.sleep(0.5)
            
            gui.press('w')
            time.sleep(1)
        status ='search'
    else:
        pass