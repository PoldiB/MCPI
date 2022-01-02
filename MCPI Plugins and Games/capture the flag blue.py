import mcpi.minecraft
import time
from pynput.keyboard import Key, Listener
import mcpi.block as mcblock


mc = mcpi.minecraft.Minecraft.create()

respawn = 37.7,1,20.5

mc.postToChat("You are using blue side code")
red_flag = 35,6
blue_wool = 35,11

entityIds = mc.getPlayerEntityIds()
print(entityIds)
player2 = entityIds[1]

def place_flag():
    s,d,f = mc.player.getPos()
    mc.setBlock(s,d,f,35,3)
    reg = mc.getBlock(s,d-2,f)
    if reg == 3:
        mc.setBlock(s,d,f,35,3)
    else:
        mc.postToChat("You can't place Flag here!")
        print("You can't place Flag here!")
        mc.setBlock(s,d,f,0)
        quit
        

def capture_flag():
    h,j,k = mc.player.getPos()
    Block = mc.getBlock(h,j-1,k)
    if Block == red_flag:
        mc.setBlock(h,j-1,k,0)

def taged_with_flag():
        v,b,n = mc.player.getPos()
        mc.setBlock(v,b,n,red_flag)
        
def have_flag():
    s,d,f = mc.player.getPos()
    flagblock = mc.getBlock(s,d,f)
    if flagblock == red_flag:
        check_have_flag = True
    else:
        check_have_flag = False
        
def no_lr():
    q,w,e = mc.player.getPos()
    lr = mc.getBlock(q,w-1,e)
    if lr == 73:
        mc.player.setPos(respawn)
        
        
def tag():
    x,y,z = mc.player.getPos()
    tagblock = x,y-1,z
    if tagblock == blue_wool:
            entityPos = mc.entity.getPos(player2)
            playerPos = mc.player.getPos()
            if entityPos == playerPos:
                if check_have_flag == True:
                    
                    taged_with_flag()
                mc.player.setPos(respawn)

def won():
    if check_have_flag == True:
        f,g,h = mc.player.getPos()
        capfl = mc.getBlock(f,g-1,h)
        if capfl == 41:
            mc.postToChat("You've won!")
            print("You've won!")
        

time.sleep(1)
mc.postToChat('Find a place to place your Flag')
print('Find a place to place your Flag')
time.sleep(1)
mc.postToChat('Make sure to keep in the boundaries')
print('Make sure to keep in the boundaries')
time.sleep(1)
mc.postToChat("In 20 seconds it will be placed")
print("In 20 seconds it will be placed")
time.sleep(10)
print("10 seconds left")
mc.postToChat("10 seconds left")
time.sleep(5)
print("5")
mc.postToChat("5")
time.sleep(1)
print("4")
mc.postToChat("4")
time.sleep(1)
print("3")
mc.postToChat("3")
time.sleep(1)
print("2")
mc.postToChat("2")
time.sleep(1)
print("1")
mc.postToChat('1')
time.sleep(1)
print('Placing')
place_flag()
mc.postToChat("Flag placed")
print("Flag placed")
time.sleep(1)
mc.postToChat("You have 2 minutes to gather stuff")
print("You have 2 minutes to gather stuff")
time.sleep(10)
mc.postToChat('Round begins')
print('Round begins')
while True:
    tag()
    have_flag()
    capture_flag()
    no_lr()
    won()
    continue
     
        
    
    
    
