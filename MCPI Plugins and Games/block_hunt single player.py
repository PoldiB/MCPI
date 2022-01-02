import random
import mcpi.minecraft
import time
import mcpi.block

mc = mcpi.minecraft.Minecraft.create()

blockDict = [
    'mcpi.block.AIR.id',
    'mcpi.block.STONE.id',
    'mcpi.block.GRASS.id',
    'mcpi.block.DIRT.id',
    'mcpi.block.COBBLESTONE.id',
    'mcpi.block.WOOD_PLANKS.id',
    'mcpi.block.SAPLING.id',
    'mcpi.block.BEDROCK.id',
    'mcpi.block.WATER_FLOWING.id',
    'mcpi.block.SAND.id',
    'mcpi.block.GRAVEL.id',
    'mcpi.block.GOLD_ORE.id',
    'mcpi.block.IRON_ORE.id',
    'mcpi.block.COAL_ORE.id',
    'mcpi.block.WOOD.id',
    'mcpi.block.LEAVES.id',
    'mcpi.block.GLASS.id',
    'mcpi.block.LAPIS_LAZULI_ORE.id',
    'mcpi.block.LAPIS_LAZULI_BLOCK.id',
    'mcpi.block.SANDSTONE.id',
    'mcpi.block.BED.id',
    'mcpi.block.WOOL.id',
    'mcpi.block.FLOWER_YELLOW.id',
    'mcpi.block.FLOWER_CYAN.id',
    'mcpi.block.MUSHROOM_BROWN.id',
    'mcpi.block.MUSHROOM_RED.id',
    'mcpi.block.GOLD_BLOCK.id',
    'mcpi.block.IRON_BLOCK.id',
    'mcpi.block.STONE_SLAB_DOUBLE.id',
    'mcpi.block.STONE_SLAB.id',
    'mcpi.block.BRICK_BLOCK.id',
    'mcpi.block.TNT.id',
    'mcpi.block.BOOKSHELF.id',
    'mcpi.block.OBSDIDIAN.id',
    'mcpi.block.TORCH.id',
    'mcpi.block.STAIRS_WOOD.id',
    'mcpi.block.CHEST.id',
    'mcpi.block.DIAMOND_ORE.id',
    'mcpi.block.DIAMOND_BLOCK.id',
    'mcpi.block.CRAFTING_TABLE.id',
    'mcpi.block.STAIRS_WOOD.id',
    'mcpi.block.FARMLAND.id',
    'mcpi.block.FURNACE_INACTIVE.id',
    'mcpi.block.FURNACE_ACTIVE.id',
    'mcpi.block.DOOR_WOOD.id',
    'mcpi.block.LADDER.id',
    'mcpi.block.STAIRS_COBBLESTONE.id',
    'mcpi.block.REDSTONE_ORE.id',
    'mcpi.block.SNOW.id',
    'mcpi.block.ICE.id',
    'mcpi.block.SNOW_BLOCK.id',
    'mcpi.block.CACTUS.id',
    'mcpi.block.CLAY.id',
    'mcpi.block.SUGAR_CANE.id',
    'mcpi.block.FENCE.id',
    'mcpi.block.GLOWSTONE_BLOCK.id',
    'mcpi.block.STONE_BRICK.id',
    'mcpi.block.GLASS_PANE.id',
    'mcpi.block.MELON.id',
    'mcpi.block.FENCE_GATE.id',
    'mcpi.block.NETHER_REACTOR_CORE.id'
    ]


for i in range (99999999999999999999999999999999):
    P1_Block = random.choice(blockDict)
    mc.postToChat(P1_Block)
    print(P1_Block)
    while (time.sleep(360)):
        x,y,z = mc.player.getPos()
        P1_blockUnderfeet = mc.getBlock(x,y-1,z)
        if P1_blockUnderfeet == mcpi.block.GRASS.id:
            mc.postToChat("Player1 found their mcpi.block")
            break
            

