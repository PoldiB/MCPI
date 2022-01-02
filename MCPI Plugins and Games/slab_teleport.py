import mcpi.minecraft
import random

mc = mcpi.minecraft.Minecraft.create()


while True:
    x,y,z = mc.player.getPos()
    buf = mc.getBlock(x,y-0.5,z)
    bof = mc.getBlock(x,y-1,z)
    if buf == 44:
        p = random.randrange(-128,128)
        l = random.randrange(-128,128)
        o = mc.getHeight(p,l)
        mc.player.setPos(p,o,l)
    if bof == 44:
        p = random.randrange(-128,128)
        l = random.randrange(-128,128)
        o = mc.getHeight(p,l)
        mc.player.setPos(p,o,l)
        
    