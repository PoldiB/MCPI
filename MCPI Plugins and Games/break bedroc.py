import mcpi.minecraft
import time

mc = mcpi.minecraft.Minecraft.create()

x,y,z = mc.player.getPos()



x,y,z = mc.player.getPos()
mc.setBlock(x,y+1,z,46)

