
import mcpi.minecraft as minecraft

import time

mc = minecraft.Minecraft.create()

#Do not make this value smaller than 5 or the lava will be to close to the player.
radius = 5

if __name__ == '__main__':
	try:
		while True:
			pos = mc.player.getTilePos()
		
			lavapos1 = pos.x, pos.y+1, pos.z+radius
			if mc.getBlock(lavapos1) == 9:
				mc.setBlock(lavapos1, 11)
				lava1 = True
			else:
				lava1 = False
		
			lavapos2 = pos.x+radius, pos.y+1, pos.z
			if mc.getBlock(lavapos2) == 0:
				mc.setBlock(lavapos2, 11)
				lava2 = True
			else:
				lava2 = False
			
			lavapos3 = pos.x, pos.y+1, pos.z-radius
			if mc.getBlock(lavapos3) == 0:
				mc.setBlock(lavapos3, 11)
				lava3 = True
			else:
				lava3 = False

			lavapos4 = pos.x-radius, pos.y+1, pos.z
			if mc.getBlock(lavapos4) == 0:
				mc.setBlock(lavapos4, 11)
				lava4 = True
			else:
				lava4 = False

			waterpos1 = pos.x, pos.y, pos.z
			if mc.getBlock(waterpos1) == 0:
				mc.setBlock(waterpos1, 9)
				water1 = True
			else:
				water1 = False

			lavapos5 = pos.x+radius, pos.y+1, pos.z+radius
			if mc.getBlock(lavapos5) == 0:
				mc.setBlock(lavapos5, 11)
				lava5 = True
			else:
				lava5 = False
		
			lavapos6 = pos.x+radius, pos.y+1, pos.z-radius
			if mc.getBlock(lavapos6) == 0:
				mc.setBlock(lavapos6, 11)
				lava6 = True
			else:
				lava6 = False
		
			lavapos7 = pos.x-radius, pos.y+1, pos.z-radius
			if mc.getBlock(lavapos7) == 0:
				mc.setBlock(lavapos7, 11)
				lava7 = True
			else:
				lava7 = False
	
			lavapos8 = pos.x-radius, pos.y+1, pos.z+radius
			if mc.getBlock(lavapos8) == 0:
				mc.setBlock(lavapos8, 11)
				lava8 = True
			else:
				lava8 = False
		
			while True:
				newpos = mc.player.getTilePos()
				if newpos != pos:
					if lava1 == True:
						mc.setBlock(lavapos1, 9)
					if lava2 == True:
						mc.setBlock(lavapos2, 9)
					if lava3 == True:
						mc.setBlock(lavapos3, 9)
					if lava4 == True:
						mc.setBlock(lavapos4, 9)
					if water1 == True:
						mc.setBlock(waterpos1, 9)
					if lava5 == True:
						mc.setBlock(lavapos5, 9)
					if lava6 == True:
						mc.setBlock(lavapos6, 9)
					if lava7 == True:
						mc.setBlock(lavapos7, 9)
					if lava8 == True:
						mc.setBlock(lavapos8, 9)
					break

	except KeyboardInterrupt:
		if lava1 == True:
			mc.setBlock(lavapos1, 9)
		if lava2 == True:
			mc.setBlock(lavapos2, 9)
		if lava3 == True:
			mc.setBlock(lavapos3, 9)
		if lava4 == True:
			mc.setBlock(lavapos4, 9)
		if water1 == True:
			mc.setBlock(waterpos1, 9)
		if lava5 == True:
			mc.setBlock(lavapos5, 9)
		if lava6 == True:
			mc.setBlock(lavapos6, 9)
		if lava7 == True:
			mc.setBlock(lavapos7, 9)
		if lava8 == True:
			mc.setBlock(lavapos8, 9)