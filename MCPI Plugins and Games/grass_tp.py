import mcpi.minecraft
import random
import time

mc = mcpi.minecraft.Minecraft.create()


while True:
    x,y,z = mc.player.getPos()
    bof = mc.getBlock(x,y-1,z)
    if bof == 2:
        p = random.randrange(-128,128)
        l = random.randrange(-128,128)
        o = mc.getHeight(p,l)
        mc.player.setPos(p,o,l)
        time.sleep(1)

