import mcpi.minecraft
from pynput.keyboard import Key, Listener

mc = mcpi.minecraft.Minecraft.create()


entityIds = mc.getPlayerEntityIds()

def on_press(key):
    t = 0
    
def on_release(key):
    if key == Key.ctrl_l:
        mc.camera.setFollow(entityIds[1])
    if key == Key.alt_l:
        mc.camera.setNormal()
    if key == Key.f3:
        mc.camera.setFollow(entityIds[0])
    
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join() 