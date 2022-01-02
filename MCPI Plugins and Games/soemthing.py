import mcpi.minecraft


mc = mcpi.minecraft.Minecraft.create()

x,y,z = mc.player.getPos()

mc.player.setPos(-5.6,-3.0,68.7)