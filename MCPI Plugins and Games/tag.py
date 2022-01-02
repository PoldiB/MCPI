import mcpi.minecraft
import time
from pynput.keyboard import Key, Listener

mc = mcpi.minecraft.Minecraft.create()

entityIds = mc.getPlayerEntityIds()

mc.postToChat('Minecraft Tag')
time.sleep(2)
mc.postToChat('Player 1 chases Player 2')
time.sleep(2)
mc.postToChat('Run!')
time.sleep(5)
mc.postToChat('Chase!')


while True:    
    ent = entityIds[1]
    pos = mc.player.getTilePos()
    pos1 = mc.entity.getTilePos(ent)
    print(pos1)
    if pos1 == pos:
        mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y-2,pos.z,0)
        mc.postToChat('Caught')
        time.sleep(5)
        
        