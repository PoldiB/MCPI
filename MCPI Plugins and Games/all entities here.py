import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

playerPosition = mc.player.getPos()

playerIds = mc.getPlayerEntityIds()
playerId = min(playerIds)
entityId = 0

print ('Player ID: ' + str(playerId))
mc.postToChat('Player ID: ' + str(playerId))

mc.postToChat("All entities will appear in your position in 1 secoond.")
time.sleep(1)

while True: 
	try:
		entityId = entityId + 1
		if entityId < playerId:
			mc.entity.setPos(entityId, playerPosition.x, playerPosition.y, playerPosition.z)
		else:
			break

	except Exception:
		continue