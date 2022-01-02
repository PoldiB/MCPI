from mcpi import minecraft
import time


mc = minecraft.Minecraft.create()


time.sleep(1)
x,y,z = mc.player.getPos()
    
        

mc.postToChat((str(x), str(y), str(z)))
time.sleep(2)

    


while True:
    cor = input(' Press q or c for coords: ')
    

    
    if cor == 'q':
        x,y,z = mc.player.getPos()
        mc.postToChat((str(x), str(y), str(z)))
    
    if cor == 'c':
        x,y,z = mc.player.getPos()
        print((str(x), str(y), str(z)))