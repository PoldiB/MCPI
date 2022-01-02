import mcpi.minecraft
import time
mc = mcpi.minecraft.Minecraft.create()


x,y,z = mc.player.getPos()

mc.setBlocks(x,y,z,x+29,y,z,35,11)