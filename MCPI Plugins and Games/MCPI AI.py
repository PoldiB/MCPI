import mcpi.minecraft
import keyboard
import time

mc = mcpi.minecraft.Minecraft.create()

def run_forward():
    keyboard.press_and_release('w')
    
def run_backward():
    keyboard.press_and_release('s')
    
def run_east():
    keyboard.press_and_release('d')
    
def run_west():
    keyboard.press_and_release('a')
    
def jump():
    keyboard.press_and_release('space')

def sneak():
    keyboard.press_and_release('shift')
    
run_forward()
run_forward()
run_forward()
run_forward()
jump()
