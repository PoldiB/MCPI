import random
import mcpi.minecraft
import time
import mcpi.block

mc = mcpi.minecraft.Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    block = mc.getBlock(x,y-1,z)
    if block == mcpi.block.GRASS.id:
        print("smh")
        mc.postToChat("smh")