import keyboard
import time
import mcpi.minecraft

mc = mcpi.minecraft.Minecraft.create(address="192.175.165.53",port=4711)

keyboard.press('w')
time.sleep(4)
keyboard.release('w')