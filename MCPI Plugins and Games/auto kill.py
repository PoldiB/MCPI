import mcpi.minecraft
from pynput.keyboard import Key, Listener

mc = mcpi.minecraft.Minecraft.create()
def kill():
    entityIds = mc.getPlayerEntityIds()
    print(entityIds)
    askd = int(input('1,2,3,...'))
    while True:
        result = mc.entity.getTilePos(entityIds[askd])
        mc.camera.setFixed()
        mc.camera.setPos(result.x, result.y+2,result.z)
        
def tp_entity():
    entityIds = mc.getPlayerEntityids()
    print(entityIds)
    askk = int(input('1,2,3,...'))
    while True:
        result = mc.player.getPos()
        mc.camera.setFixed()
        mc.entity.setPos(result.x,result.y-2,result.z)

def on_press(key):
    dkgfkfjkjs=0
    
def on_release(key):
    if key == Key.ctrl_l:
        kill()
    if key == Key.alt_l:
        tp_entity()
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()  
