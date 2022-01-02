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

y = random.randrange(-60,yTS)

iTS = random.randrange(1,50)
dTS = random.randrange(1,20)
gTS = random.randrange(1,30)
lTS = random.randrange(1,50)
rTS = random.randrange(1,50)
cTS = random.randrange(1,100)

width_of_cave = random.randrange(2,5)
length_of_cave = random.randrange(2,5)
depth_of_cave = random.randrange(10,60)

for i in range(caves_number):  
    x = random.randrange(-100,100)

    z = random.randrange(-100,100)

    yTS = mc.getHeight(x,z)

    y = random.randrange(-60,yTS)
    
    num_of_iron = random.randrange(1,50)
    num_of_diamonds = random.randrange(1,20)
    num_of_gold = random.randrange(1,30)
    num_of_lapis = random.randrange(1,50)
    num_of_redstone = random.randrange(1,50)
    num_of_coal = random.randrange(1,100)
    
    iTS = random.randrange(1,50)
    dTS = random.randrange(1,20)
    gTS = random.randrange(1,30)
    lTS = random.randrange(1,50)
    rTS = random.randrange(1,50)
    cTS = random.randrange(1,100)
    
    width_of_cave = random.randrange(5,10)
    length_of_cave = random.randrange(5,10)
    depth_of_cave = random.randrange(1,60)
    
    
    
    mc.setBlocks(x,y,z, x + width_of_cave, y + depth_of_cave, z + length_of_cave, 0)
    
    mc.setBlocks
    

    

print(yTS)
print(str(x),str(z))