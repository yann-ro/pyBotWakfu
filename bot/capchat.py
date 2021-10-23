import pyautogui as gui
import time

from bot.config import Config

def find(name,kind,image_confidence, screen=(0,0,1920,1080)):
    """
    """
    image_name = f'image/{kind}/{name}.png'
    image_location = gui.locateCenterOnScreen(image_name,confidence=image_confidence,grayscale=True,region=screen)
    
    return image_location


def click_on(name,kind,type_clic,image_confidence,zone_capture=(0,0,1920,1080)):  
    """
    """
    location = find(name,kind,image_confidence,screen=zone_capture)
    
    if (location == None):
        status = 'search'
        return status
    else:         
        gui.click(location, button=type_clic)
        status = 'pickup'
        return status


def capChat() :
    """
    """
    config = Config()
    gui.click(config.middle)

    if find('chatStart',0.8, screen=config.screen_reduced)!=None:
        gui.press('space')
        print('start')
        
    time.sleep(2)

    while find('chat',0.8, screen=config.screen_reduced)!=None :
        
        chatx, chaty = find('chat','fighter',0.8, screen=config.screen_reduced)
        zone_capchat = (chatx-190, chaty-110, chatx+190, chaty+110)
        zone_mineur = (
            zone_capchat[0]-config.dist_chat_mineur[0],
            zone_capchat[1]-config.dist_chat_mineur[1],
            zone_capchat[2]-config.dist_chat_mineur[0],
            zone_capchat[3]-config.dist_chat_mineur[1])
        print ('chat')

        for i in range(1,9):
            if (find(str(i),'dice',config.coeff_capchat[str(i)],screen=zone_capchat)!=None):
                #mousePosition = find(str(i),0.7,screen=zoneCapChat)
                #gui.moveTo(mousePosition)                                                             
                
                poisiton_de = find(str(i),config.coeff_capchat[str(i)],screen=zone_mineur)
                if (poisiton_de!=None):
                    print('I click on : '+str(i)+' : ')
                    gui.press('w')                
                    time.sleep(1)
                    gui.click(poisiton_de, button='left')
                    time.sleep(1)
                else:
                    pass
                
            else:
                pass