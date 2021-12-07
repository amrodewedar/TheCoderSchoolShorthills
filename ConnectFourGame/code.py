Board = [['0','1','2','3','4','5','6'],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ']]

# Print the board
def printBoard(board):
  for row in board:
    print()
    for col in row:
      print("[" + col + "]", end = "")
  print()

#Makes sure the move is 0-6
def validMove(move, board):
  if move in board[0]:
    if board[1][int(move)] == ' ':
      return True

#Places the move
def placeMove(x):
  for i in range(6,0,-1):
    if Board[int(i)][int(x)] == ' ':
      return i

def rightCheck(Location, player, status=0):
  row = Location[0]
  col = Location[1]

  if status >= 4:
    return status
  if row >= 7 or col >= 7:
    return status
  if Board[row][col] != player:
    return status
  
  newLocation = (row, col+1)
  return rightCheck(newLocation, player, status+1)
  

#check if you won going rightcheck
def upCheck(Location, player, status=0):
  row = Location[0]
  col = Location[1]

  if status >= 4:
    return status
  if row >= 7 or col >= 7:
    return status
  if Board[row][col] != player:
    return status
  
  newLocation = (row-1, col)
  return upCheck(newLocation, player, status+1)

def uprightCheck(Location, player, status=0):
  row = Location[0]
  col = Location[1]

  if status >= 4:
    return status
  if row >= 7 or col >= 7:
    return status
  if Board[row][col] != player:
    return status
  
  newLocation = (row-1, col+1)
  return uprightCheck(newLocation, player, status+1)

def downrightCheck(Location, player, status=0):
  row = Location[0]
  col = Location[1]

  if status >= 4:
    return status
  if row >= 7 or col >= 7:
    return status
  if Board[row][col] != player:
    return status
  
  newLocation = (row+1, col-1)
  return downrightCheck(newLocation, player, status+1)

def checkWin(player):
  
  for row in range(1, 7): 
    for col in range(0, 7):    
      Location = (row,col)
      
      status = rightCheck(Location, player)
      if status == 4:
        return True
      
      status = upCheck(Location, player)
      if status == 4:
        return True
      
      status = uprightCheck(Location, player)
      if status == 4:
        return True
      
      status = downrightCheck(Location, player)
      if status == 4:
        return True

  return False

#determines which player is up
turnCounter=1
Gameover = False
while Gameover == False:
  printBoard(Board)
  turnCounter += 1
  if turnCounter%2 == 1:
    player = 'X'
  else:
    player = 'O'
  print("Player (", player, ") move", end='. ')
  usermove=input("Enter a move (0-6): ")
  if validMove(usermove,Board):
    
    row = placeMove(usermove)
    
    Board[row][int(usermove)]=player
    printBoard(Board)
  if checkWin(player) == True:
    print(f"{player} You won") 
    Gameover = True
