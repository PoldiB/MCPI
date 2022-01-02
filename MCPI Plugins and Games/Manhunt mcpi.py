from mcpi import minecraft
import random
import time

mc = minecraft.Minecraft.create()
x = random.randrange(-80, 80)
y = random.randrange(20, 50)
z = random.randrange(-80, 80)
                


mc.setBlocks(x,y,z,x+2,y,z,41)

for i in range(3):
    mc.postToChat((str(x), str(y), str(z)))
    time.sleep(2)

while True:
    cor = input(' Press q or c for coords: ')
    

    
    if cor == 'q':   
        mc.postToChat((str(x), str(y), str(z)))
    
    if cor == 'c':
        print(str(x), str(y), str(z))