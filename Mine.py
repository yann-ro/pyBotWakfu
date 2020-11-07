import pyautogui as gui
import time

def find(name, imageConfidence, screen=(0,0,1920,1080)):
    imageName = r'C:\Users\yannr\Info\PyBotWakfu\bankImage\{}.png'.format(name)
    
    imageLocation = gui.locateCenterOnScreen(imageName,confidence=imageConfidence,grayscale=True,region=screen)
    #print(str(imgConfidence)+" : "+str(img_location))
    
    return imageLocation


def click_on(name,typeClic,imageConfidence,zoneCapture=(0,0,1920,1080)):
    
    
    
    location = find(name,imageConfidence,screen=zoneCapture)
    
    #gui.click(location, button=typeClic)
    if (location == None):
        status = 'search'
        #print('not found')
        return status
    else:         
        gui.click(location, button=typeClic)
        status = 'pickup'
        #print('found')
        return status


def mine(minerais):
    
    status = click_on(minerais,'right',0.8)
    time.sleep(0.75)
    
    if status == 'pickup':
        click_on('pioche','left',0.8)
        time.sleep(2)
        
        if find('recolte', 0.9) != None :
            while find('recolte', 0.9) != None :
                time.sleep(0.5)
            
            gui.press('tab')
            time.sleep(0.5)
        status ='search'
    else:
        pass



ore = 'carboneBrak'

while True :
    mine(ore)