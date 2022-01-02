import mcpi.minecraft
from pynput.keyboard import Key, Listener

mc = mcpi.minecraft.Minecraft.create()

def on_press(key):
    t = 0

def on_release(key):
    if key == Key.ctrl_l:
        x,y,z = mc.player.getPos()
        mc.player.setPos(x+10,y,z)
    if key == Key.alt_l:
        x,y,z = mc.player.getPos()
        mc.player.setPos(x,y,z+10)
    if key == Key.caps_lock:
        x,y,z = mc.player.getPos()
        mc.player.setPos(x-10,y,z)
    if key == Key.shift_l:
        x,y,z =  mc.player.getPos()
        mc.player.setPos(x,y,z-10)
    if key == Key.ctrl_r:
        x,y,z = mc.player.getPos()
        mc.player.setPos(x,y+30,z)
        
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()