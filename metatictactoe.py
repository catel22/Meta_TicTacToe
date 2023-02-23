def display(board):
   print()
   print(board)
   print()

def playGame(board, player1, player2):
  """
  A game of Tic-Tac-Toe; player1 starts.
  """
  # player1 is next player
  currentPlayer, nextPlayer = player2, player1 

  # run the game
  print('Welcome to Meta-Tic-Tac-Toe!\n')
  display(board)

  # As long as the game isn't over:
  #   display the current board
  #   switch players
  #   get a move from the current player
  while (not board.checkWin(currentPlayer.checker)):
    if board.isFull():
      print("Cat's game.")
      board.reset()
      display(board)
    currentPlayer, nextPlayer = nextPlayer, currentPlayer
    miniboard = board.getValue(currentPlayer.getBoardNum(board))
    move = currentPlayer.nextMove(miniboard)
    miniboard.setValue(move, currentPlayer.checker)
    display(board)

  # print player who won
  if board.checkWin(currentPlayer.checker):
    print(f'{currentPlayer.checker} wins -- Congratulations!')

def main():
    import miniboard
    import bigboard
    import gameplayer

    opponent = ''
    while (opponent != 'y' and opponent != 'n'):
      opponent = input("Would you like to play against a computer? y or n ")
    if opponent=='y':
      playGame(bigboard.Bigboard(), gameplayer.MachinePlayer(miniboard.X), gameplayer.HumanPlayer(miniboard.O))
    else:
      playGame(bigboard.Bigboard(), gameplayer.HumanPlayer(miniboard.X), gameplayer.HumanPlayer(miniboard.O))

main()