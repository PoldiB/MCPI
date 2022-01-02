from mcpi import minecraft
import random
import time

mc = minecraft.Minecraft.create()

level = input('what level?1,2,3,4,5 or 6: ')

if level == '1':
    while True:
        x,y,z = mc.player.getPos()
        da = random.randrange(0,156)
        mc.setBlock(x,y-1,z,da)
        time.sleep(1)
    
if level == '2':
    while True:
        x,y,z = mc.player.getPos()
        da = random.randrange(0,156)
        mc.setBlock(x,y-1,z,da)
        time.sleep(0.5)
    
if level == '3':
    while True:
        x,y,z = mc.player.getPos()
        da = random.randrange(0,156)
        mc.setBlock(x,y-1,z,da)
        time.sleep(0.4)
    
if level == '4':
    while True:
        x,y,z = mc.player.getPos()
        da = random.randrange(0,156)
        mc.setBlock(x,y-1,z,da)
        time.sleep(0.3)
    
if level == '5':
    time.sleep(60)
    while True:
        x,y,z = mc.player.getPos()
        da = random.randrange(0,156)
        mc.setBlock(x,y-1,z,da)
        time.sleep(0.2)
    
if level == '6':
    time.sleep(60)
    while True:
        x,y,z = mc.player.getPos()
        da = random.randrange(0,156)
        mc.setBlock(x,y-1,z,da)
        time.sleep(0.1)


    
    