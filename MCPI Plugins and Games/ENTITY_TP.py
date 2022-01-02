from mcpi.minecraft import Minecraft
mc = Minecraft.create()
entityIds = mc.getPlayerEntityIds()
print(entityIds)
input = input("what player (use numbers: 1,2,3 etc. :")
input = int(input)
input = input - 1
result = mc.entity.getTilePos(entityIds[input])
#print(result)
mc.player.setTilePos(result)