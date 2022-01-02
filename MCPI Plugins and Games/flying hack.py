import mcpi.minecraft
import time

mc = mcpi.minecraft.Minecraft.create()

x,y,z = mc.player.getPos()

while True:
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y-1,z,46)
    time.sleep(0.1)
    mc.setBlock(x,y-1,z,0)
    time.sleep(0.01)
                      
            