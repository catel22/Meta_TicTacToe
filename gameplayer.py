from miniboard import X, O, BLANK
import bigboard

class Player:
  '''
  A class that represents a Tic-Tac-Toe Player.
  '''

  def __init__(self, checker):
    self.checker = checker

  def nextMove(self, board):
    '''
    Returns position where player wants to play
    '''
    return [0, 0]

class HumanPlayer(Player):
  '''
  A Player that can get the next move from the command line.
  '''

  def nextMove(self, board):
    '''
    Prompts the user to enter a move. 

    Continues prompting until the move is valid.
    '''
    return (self.getPosition(board))
  
  def getBoardNum(self, board):
    '''
    Prompts the user to enter a column. 

    Continues prompting until the move is valid.
    '''
    while True:
      column = (input(f"{self.checker}'s board column choice: "))
      row = (input(f"{self.checker}'s board row choice: "))
      try:
        column = int(column) - 1
        row = int(row) - 1
        assert (0 <= column < 3), 'Not a valid column choice'
        assert (0 <= row < 3), 'Not a valid row choice'
        assert not board.getValue((column, row)).isWon(), 'Already won!'
      except ValueError:
        print('Invalid input: ')
      except AssertionError as msg:
        print(msg)
      else: 
        return (column, row)
      
  def getPosition(self, board):
    '''
    Prompts the user to enter a column. 

    Continues prompting until the move is valid.
    '''
    while True:
      column = (input(f"{self.checker}'s column choice: "))
      row = (input(f"{self.checker}'s row choice: "))
      try:
        column = int(column) - 1
        row = int(row) - 1
        assert (0 <= column < 3), 'Not a valid column choice'
        assert (0 <= row < 3), 'Not a valid row choice'
        assert not board.isPositionFull((column, row)), 'No room!'
      except ValueError:
        print('Invalid input: ')
      except AssertionError as msg:
        print(msg)
      else: 
        return (column, row)
    

class MachinePlayer(Player):
  '''
  A silly machine who is not the best at meta tic tac toe
  '''

  def __init__(self, checker):
    Player.__init__(self, checker)

  def getBoardNum(self, board):
    for i in range(3):
      for x in range(3):
          if (not board.getValue((i, x)).isWon()):
            return (i, x)
          
  def nextMove(self, board):
    for i in range(3):
      for x in range(3):
          if (board.getValue((i, x)) is BLANK):
            return (i, x)