from mcpi.minecraft import Minecraft
from time import sleep
import os
os.system("clear")
mc = Minecraft.create()
entityIds = mc.getPlayerEntityIds()
while True:
    print("\033[1;32;40mEntity tracker v1.9\033[0;37;40m")
    print("-" * 20)
    for x in entityIds:
        try:
            entityIds = mc.getPlayerEntityIds()
            print("ID :",x,"| Pos:",mc.entity.getPos(x))
        except:
            pass
    sleep(1)
    os.system("clear")