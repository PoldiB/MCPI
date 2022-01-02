"Tic-Tac-Pi"
"Creator Bigjango (FG6)"
"Creit to Wallee/red-exe-engineer for getWinner()"

import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

def getWinner(mat, player):
    "Creator Wallee/red-exe-engineer"
    "https://www.youtube.com/channel/UCzAOB6RwvO5PWjLsuFNJ4MQ"
    winner = False
    for i in range(0, 3):
        if [mat[0+i], mat[1+i], mat[2+i]] == [player, player, player]:
            winner = True
    for i in range(0, 3):
        if [mat[0+i], mat[3+i], mat[6+i]] == [player, player, player]:
            winner = True
    if [mat[0], mat[4], mat[8]] == [player, player, player]:
        winner = True
    if [mat[2], mat[4], mat[6]] == [player, player, player]:
        winner = True
    if winner:
        return(player)
    else:
        return(False)

def findPosinList(obj, blockList):
    for i in range(0, len(blockList)):
        if blockList[i] == obj:
            return(i)
    
def makeX(x, y, z):
    mc.setBlock(x, y, z, 35, 11)
    mc.setBlock(x+1, y+1, z, 35, 11)
    mc.setBlock(x+1, y-1, z, 35, 11)
    mc.setBlock(x-1, y-1, z, 35, 11)
    mc.setBlock(x-1, y+1, z, 35, 11)
    
def makeO(x, y, z):
    mc.setBlock(x+1, y, z, 35, 1)
    mc.setBlock(x-1, y, z, 35, 1)
    mc.setBlock(x, y+1, z, 35, 1)
    mc.setBlock(x, y-1, z, 35, 1)
    
def clearSquares(center, amountx=3, amounty=3, size=3):
    for currentx in range(1, amountx+1):
        for currenty in range(1, amounty+1):
            mc.setBlocks(center.x+(amountx*(size-currentx))-1, center.y+(amounty*(size-currenty))-1, center.z+5, center.x+(amountx*(size-currentx))+1, center.y+(amounty*(size-currenty))+1, center.z+5, 0)

def makeSquares(center, amountx=3, amounty=3, size=3):
    data = 0
    blockList = []
    for currentx in range(1, amountx+1):
        for currenty in range(1, amounty+1):
            if data == 15:
                data = 0
            else:
                data = 15
            mc.setBlocks(center.x+(amountx*(size-currentx))-1, center.y+(amounty*(size-currenty))-1, center.z+5, center.x+(amountx*(size-currentx))+1, center.y+(amounty*(size-currenty))+1, center.z+5, 35, data)
            blockList.append([int(center.x+(amountx*(size-currentx))), int(center.y+(amounty*(size-currenty))), int(center.z+5)])
    return(blockList)

x, y, z = mc.player.getPos()
mc.setBlock(x, y-1, z, 35, 14)
players = []
mc.postToChat('click on the red wool to join')
while len(players) != 2:
    blockEvents = mc.events.pollBlockHits()
    for blockEvent in blockEvents:
        blockX, blockY, blockZ = blockEvent.pos
        if [blockX, blockY, blockZ] == [int(x), int(y-1), int(z)]:
            mc.postToChat(str(len(players)+1) + ' of 2 players have joined')
            players.append(blockEvent.entityId)

blockList = makeSquares(mc.player.getPos())
game = 'on'
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 0
mc.events.clearAll()
mc.postToChat('Player 1\'s turn')
while game == 'on':
    blockEvents = mc.events.pollBlockHits()
    for blockEvent in blockEvents:
        blockX, blockY, blockZ = blockEvent.pos
        if ([blockX, blockY, blockZ] in blockList) and (blockEvent.entityId in players):
            place = findPosinList([blockX, blockY, blockZ], blockList)
            if (blockEvent.entityId == players[0]) and (turn == 0) and (board[place] == 0):
                makeX(blockX, blockY, blockZ)
                turn = 1
                board.pop(place)
                board.insert(place, 'X')
                if getWinner(board, 'X') == False:
                    mc.postToChat('Player 2\'s turn')
                else:
                    mc.postToChat('Player 1 won, good game player 2!!')
                    break
            elif (blockEvent.entityId == players[1]) and (turn == 1) and (board[place] == 0):
                makeO(blockX, blockY, blockZ)
                turn = 0
                board.pop(place)
                board.insert(place, 'O')
                if getWinner(board, 'O') == False:
                    mc.postToChat('Player 1\'s turn')
                else:
                    mc.postToChat('Player 2 won, good game player 1!!')
                    break
            mc.events.clearAll()
   
clearSquares(mc.player.getPos())