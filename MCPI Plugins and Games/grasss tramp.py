import mcpi.minecraft
import time

mc = mcpi.minecraft.Minecraft.create()

x,y,z = mc.player.getPos()

d = 10

while True:
    cd = input("-")
    x,y,z = mc.player.getPos()
    yu = mc.getBlock(x,y-1,z)
    if yu == 4:
        mc.player.setPos(x,y+80,z)
        d = d*2
    if cd == 'q':
        break
        time.sleep(5)
        continue