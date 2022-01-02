import mcpi.minecraft
import random
import time

mc = mcpi.minecraft.Minecraft.create()
x,y,z = mc.player.getPos()

bl = random.randrange(0,300)
mc.setBlock(x,y,z, 1)
