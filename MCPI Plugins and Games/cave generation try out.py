
#Import Minecraft
import mcpi.minecraft
#Import mcpi.block for using words instead of ID's
import mcpi.block as block
#Import math (for sphere function)
import math
#Import random (for replace & replacenear functions)
import random
#Detect key presses. If you don't have this, do: pip3 install pynput
from pynput.keyboard import Key, Listener

worldType = 0
#Will equal 1, void, 2, small superflat, 3, large superflat.
ID = 0
#Most functions need to know which block you want.
func = 1
#What function is currently toggled. See change_function() for more information.
delete = 0

#Less typing for me :)
mc = mcpi.minecraft.Minecraft.create()
def spherical_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))


def sphere(radius, x1, y1, z1, ID, data):
    #x1, y1, and z1 are the center coordinates
    #Teleport player upward so that they aren't trablock.ed in the sphere
    #This MAY through up an error. Python sometimes thinks that I'm
    #calling a tuple, not a function.
    px, py, pz = mc.player.getPos()
    diameter = radius * 2
    #First item in tuple is the start point, second is end point
    xcoords = (x1 - radius, x1 + radius)
    ycoords = (y1 - radius, y1 + radius)
    zcoords = (z1 - radius, z1 + radius)
    #More or less we are checking every point in a cuboid with the given radius, and checking each block.
    #We calculate if the block is within the sphere with the Pythagorean Theorum, and if it is, set it to the
    #given block with the given data
    for x2 in range(xcoords[0], xcoords[1]):     
        for y2 in range(ycoords[0], ycoords[1]):
            for z2 in range(zcoords[0], zcoords[1]):
                if spherical_distance(x1, y1, z1, x2, y2, z2) <= radius:
                    mc.setBlock(x2, y2, z2, ID, data)

def replace(oldIDList, newIDList, oldDataList, newDataList, x1, y1, z1, x2, y2, z2):
    #Don't you just love that feeling when you have 10 parameters to pass in?
    xhigh = max(x1, x2)
    xlow = min(x1, x2)
    yhigh = max(y1, y2)
    ylow = min(y1, y2)
    zhigh = max(z1, z2)
    zlow = min(z1, z2)
    blocksChangedCount = 0
    for x in range(xhigh - xlow + 1):
        for y in range(yhigh - ylow + 1):
            for z in range(zhigh - zlow + 1):
                block = mc.getBlockWithData(xlow + x, ylow + y, zlow + z)
                coords = (xlow + x, ylow + y, zlow + z)
                print("Block at: " + str(coords))
                print("ID: " + str(block.id) + " Data: " + str(block.data))
                if block.id in oldIDList:
                    if oldDataList[oldIDList.index(block.id)] == block.data:
                        blocksChangedCount += 1
                        lengthNewIDList = len(newIDList)
                        if lengthNewIDList > 1: 
                            newID = newIDList[random.randint(0, len(newIDList) - 1)]
                            mc.setBlock(xlow + x, ylow + y, zlow + z, newID, newDataList[newIDList.index(newID)])
                        else:
                            mc.setBlock(xlow + x, ylow + y, zlow + z, newIDList[0], newDataList[0])
    print("Operation complete. " + str(blocksChangedCount) + " blocks were affected.")

def getPos1():
    global x, y, z
    x,y,z = mc.player.getTilePos() #Formerly getpos(), but getTilePos() is more accurate.
    print("Pos 1 is set to (" + str(x) + ", " + str(y) + ", " + str(z) + ")")

def getPos2():
    global x, y, z
    x, y, z = mc.player.getTilePos()
    print("Pos 2 is set to (" + str(x) + ", " + str(y) + ", " + str(z) + ")")

def on_press(key):
    #print('{0}'.format(key))
    #uncomment above to see key presses in shell (It's super annoying)
    #Something has to be in this function, and it can't not exist, so
    #y always = 0 :P
    yt = 0

def on_release(key):
    global delete
    if key == Key.up:
        #I don't want anyone to accidentally delete their world, so press the button 3 times to change
        #Note that you can hit right control to save your world
        delete += 1
        if delete == 1:
            print("Press 2 more times to toggle world")
        elif delete == 2:
            print("Press 1 more time to toggle world")
        else:
            toggle_world()
            delete = 0
    if key == Key.left:
        getPos1()
    if key == Key.right:
        getPos2()
    if key == Key.down:
        setblock_query()
    if key == Key.shift_r:
        change_function()
    if key == Key.ctrl_r:
        print("World saved. Press the right Alt key to load it.")
        mc.saveCheckpoint()
    if key == Key.alt_r:
        print("Your save has been loaded.")
        mc.restoreCheckpoint()

import mcpi.minecraft
import time
import random

global y
global x
global z
global yTS
global iTS
global dTS
global gTS
global lTS
global rTS
global cTS
global num_of_iron
global num_of_gold
global num_of_diamonds
global num_of_coal
global width_of_cave
global length_of_cave
global depth_of_cave


mc = mcpi.minecraft.Minecraft.create()

caves_number = random.randrange(1,500)

x = random.randrange(-100,100)

z = random.randrange(-100,100)

yTS = mc.getHeight(x,z)

y = random.randrange(-60,10)


width_of_cave = random.randrange(2,5)
length_of_cave = random.randrange(2,5)
depth_of_cave = random.randrange(10,60)

for i in range(caves_number):  
    x = random.randrange(-100,100)

    z = random.randrange(-100,100)

    yTS = mc.getHeight(x,z)

    y = random.randrange(-60,yTS)

    
    width_of_cave = random.randrange(5,10)
    length_of_cave = random.randrange(5,10)
    depth_of_cave = random.randrange(1,60)
    
    
    
    mc.setBlocks(x,y,z, x + width_of_cave, y + depth_of_cave, z + length_of_cave, 0)
    
    sphere
