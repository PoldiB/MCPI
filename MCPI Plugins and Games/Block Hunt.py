#!/usr/bin/python
#Welcome to the mess that is my code!
#I'm mostly self-taught, so I'm sorry in advance if I don't follow conventions perfectly.
import random
#Import Minecraft
import mcpi.minecraft
#Import mcpi.block for using words instead of ID's
import mcpi.block as block

import time
#Import math (for sphere function)
global BlockName


t = 10

mc = mcpi.minecraft.Minecraft.create()

blockDict = ['1','1','1','1','1','1','1','1','2','2','2','2','2','2','3','3','3','3','4','4','4','4','4','4','5','5','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','12','12','12','12','12','12','12','12','12','12','12','13','13','13','13','13','13','13','14','14','15','15','15','15','16','16','16','16','16','17','17','17','17','17','17','17','17','18','18','18','18','20','20','20','20','21','22','24','24','24','26','26','26','26','35','35','35','35',,'37','37','37','38','38','38','39','40','41','41','42','42','42','43','43','43','43','44','44','44','44','45','45','45','46','46','47','49','50','50','50','53','53','53','54','54','54','56','56','57','58','58','58','58','58','58','60','60','61','61','61','61','62','62','62','62','64','64','64','64','65','65','65','65','65','67','67','67','67','67','73','73','73','78','78','78','79','79','80','80','81','81','82','82','82','83','83','83','85','85','85','85','89','89','98','98','98','102','102','102','102','0','107']

def getBlock():
    if block == 0:
        BlockName = 'Air'
    if block == 1:
        BlockName = 'Stone'
    if block == 2:
        BlockName = 'Grass'
    if block == 3:
        BlockName = 'Dirt'
    if block == 4:
        BlockName = 'Cobblestone'
    if block == 5:
        BlockName = 'Wood Planks'
    if block == 6:
        BlockName = 'Oak Sapling'
    if block == 7:
        BlockName = 'Bedrock'
    if block == 8:
        BlockName = 'Water Flowing'
    if block == 12:
        BlockName = 'Sand'
    if block == 13:
        BlockName = 'Gravel'
    if block == 14:
        BlockName = 'Gold Ore'
    if block == 15:
        BlockName = 'Iron Ore'
    if block == 16:
        BlockName = 'Coal Ore'
    if block == 17:
        BlockName = 'Wood'
    if block == '18':
        BlockName = 'Leaves'
    if block == 20:
        BlockName = 'Glass'
    if block == 21:
        BlockName = 'Lapis Ore'
    if block == 22:
        BlockName = 'Lapis Block'
    if block == 24:
        BlockName = 'Sandstone'
    if block == 26:
        BlockName = 'Bed'
    if block == '35':
        BlockName = 'White Wool'
    if block == '37':
        BlockName = 'Yellow Flower'
    if block == '38':
        BlockName = 'Flower Blue/Rose'
    if block == '39':
        BlockName = 'Brown Mushroom'
    if block == '40':
        BlockName = 'Red Mushroom'
    if block == '41':
        BlockName = 'Gold Block'
    if block == 42:
        BlockName = 'Iron Block'
    if block == 43:
        BlockName = 'Stone Slab Double'
    if block == 44:
        BlockName = 'Stone Slab'
    if block == 45:
        BlockName = 'Bricks'
    if block == 46:
        BlockName = 'TNT'
    if block == 47:
        BlockName = 'Bookshelf'
    if block == 49:
        BlockName = 'Obsidian'
    if block == 50:
        BlockName = 'Torch'
    if block == 53:
        BlockName = 'Stairs Wood'
    if block == 54:
        BlockName = 'Chest'
    if block == 56:
        BlockName = 'Diamond Ore'
    if block == 57:
        BlockName = 'Diamond Block'
    if block == 58:
        BlockName = 'Crafting Table'
    if block == 60:
        BlockName = 'Farmland'
    if block == 61:
        BlockName = 'Furnace Inactive'
    if block == 62:
        BlockName = 'Furnace Active'
    if block == 64:
        BlockName = 'Door'
    if block == 65:
        BlockName = 'Ladder'
    if block == 67:
        BlockName = 'Cobblestone Stairs'
    if block == 73:
        BlockName = 'Redstone Ore'
    if block == 78:
        BlockName = 'Snow'
    if block == 79:
        BlockName = 'Ice'
    if block == 80:
        BlockName = 'Snow Block'
    if block == 81:
        Blockname = 'Cactus'
    if block == 82:
        BlockName = 'Clay'
    if block == 83:
        BlockName = 'Sugar Cane'
    if block == 85:
        BlockName = 'Fence'
    if block == 89:
        BlockName = 'Glowstone'
    if block == 98:
        BlockName = 'Stone Brick'
    if block == 102:
        BlockName = 'Glass Pane'
    if block == 107:
        BlockName = 'Fence Gate'
    if block == 247:
        BlockName = 'Nether Reactor Core'



def player1():
    for i in range(999999999999999999):
        block = random.choice(blockDict)
        getBlock()
        mc.postToChat('player1:',BlockName)
        while (time.sleep(360)):
            x,y,z = mc.player.getPos()
            Player_Block = mc.getBlock(x,y-1,z)
            if Player_Block == block:
                mc.postToChat('Player1 found there block')
            
    

        
    
player1()    