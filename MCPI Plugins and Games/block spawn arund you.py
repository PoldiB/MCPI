import mcpi.minecraft
import random
import time

mc = mcpi.minecraft.Minecraft.create()

while True:
    t = random.randrange(1,3)
    r = random.randrange(1,2)
    e = random.randrange(13,)
    x,y,z = mc.player.getPos()
    block = mc.getBlock(x,y-1,z)
    mc.setBlock(x+t,y+r,z+e,block)
    time.sleep(0.01)
    continue
    
    