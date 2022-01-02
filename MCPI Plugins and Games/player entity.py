import mcpi.minecraft

mc = mcpi.minecraft.Minecraft.create()

entityIds = mc.getPlayerEntityIds()
for entityId in entityIds:
    print (entityIds)