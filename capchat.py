import pyautogui as gui
import time
import datas as dat

# Function

def find(name, imageConfidence, screen=(0,0,1920,1080)):
    
    imageName = r'C:\Users\yannr\Info\PyBotWakfu\bankImage\{}.png'.format(name)
    imageLocation = gui.locateCenterOnScreen(imageName,confidence=imageConfidence,grayscale=True,region=screen)
    
    return imageLocation


def click_on(name,typeClic,imageConfidence,zoneCapture=(0,0,1920,1080)):  
    
    location = find(name,imageConfidence,screen=zoneCapture)
    
    if (location == None):
        status = 'search'
        return status
    else:         
        gui.click(location, button=typeClic)
        status = 'pickup'
        return status

def capChat() :
    d = dat.Datas()
    gui.click(d.middle)

    if find('chatStart',0.8, screen=d.screenReduced)!=None:
        gui.press('space')
        print('start')
        
    time.sleep(2)

    while find('chat',0.8, screen=d.screenReduced)!=None :
        
        chatx, chaty = find('chat',0.8, screen=d.screenReduced)
        zoneCapChat = (chatx-190, chaty-110, chatx+190, chaty+110)
        zoneMineur = (zoneCapChat[0]-d.distChatMineur[0],zoneCapChat[1]-d.distChatMineur[1],zoneCapChat[2]-d.distChatMineur[0],zoneCapChat[3]-d.distChatMineur[1])
        print ('chat')

        for i in range(1,9):
            if (find(str(i),d.coeffCapChat[str(i)],screen=zoneCapChat)!=None):
                #mousePosition = find(str(i),0.7,screen=zoneCapChat)
                #gui.moveTo(mousePosition)                                                             
                
                poisitonDe = find(str(i),d.coeffCapChat[str(i)],screen=zoneMineur)
                if (poisitonDe!=None):
                    print('I click on : '+str(i)+' : ')
                    gui.press('w')                
                    time.sleep(1)
                    gui.click(poisitonDe, button='left')
                    time.sleep(1)
                else:
                    pass
                
            else:
                pass


#capChat()

"""
#Test

for k in range (1,9):
#k=4
    for i in range(0,5):
        position = find(str(k),0.6+i*0.05,screen=zoneCapChat)
        gui.click(position)
        print (str(k)+' : '+str(0.6+i*0.05)+' : I click on : '+str(position))
        time.sleep(0.5)
    print(' ')

"""