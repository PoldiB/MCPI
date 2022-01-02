import random
import mcpi.minecraft 

mc = mcpi.minecraft.Minecraft.create();

x,y,z = mc.player.getPos()

mc.setBlock(x,y,z,22)