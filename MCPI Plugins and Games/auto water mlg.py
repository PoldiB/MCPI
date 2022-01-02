import mcpi.minecraft
import time

mc = mcpi.minecraft.Minecraft.create()

x,y,z = mc.player.getPos()

while True:
    x,y,z = mc.player.getPos()
    block = mc.getBlock(x,y-1,z)
    x,y,z = mc.player.getPos()
    if block == 1 or 2 or 3 or 4 or 5 or 7 or 9 or 10 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 20 or 21 or 22 or 24 or 26 or 30 or 35 or 41 or 42 or 43 or 44 or 45 or 46 or 47 or 48 or 49 or 53 or 54 or 56 or 57 or 58 or 60 or 61 or 62 or 64 or 67 or 73 or 78 or 79 or 80 or 81 or 82 or 85 or 89 or 95 or 98 or 102 or 103 or 107 or 246 or 247:      
        mc.setBlock(x,y-1,z,9)
        time.sleep(0.1)
        mc.setBlock(x,y-1,z,0)
        time.sleep(0.01)
        