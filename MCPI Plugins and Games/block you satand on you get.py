import mcpi.minecraft
import time

mc = mcpi.minecraft.Minecraft.create()


while True:
    x,y,z = mc.player.getPos()

    ta = mc.getBlock(x,y-1,z)

    mc.setBlock(x,y,z,ta)
    time.sleep(1)