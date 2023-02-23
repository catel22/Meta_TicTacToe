Checker = str     # gamepiece

X = Checker('X')
O = Checker('O')
BLANK = Checker(' ')

#Coord format is column, row

class Miniboard:
    '''
    Single tictactoe board
    '''

    def __init__(self):
        '''

        _cells: cooordinate is a tuple, occupied by checker
        '''
        self._cells = {}
        self.reset()
        self._winner = ''

    def getWinner(self):
        return self._winner
    
    def isWon(self):
        #Returns true if somebody has already won the square
        return (self._winner != '')

    def getValue(self, coord):
        '''
        Get the checker value from a given coordinate
        '''
        return (self._cells[coord])
    
    def setValue(self, coord, checker):
        '''
        Set position as checker
        '''
        self._cells[coord] = checker
    
    def isPositionFull(self, coord):
        return (self.getValue((coord[0], coord[1])) is not BLANK)
    
    def isFull(self):
        '''
        Returns True if every cell has a checker.
        '''
        for i in range(3):
                for x in range(3):
                    if (self.getValue((i, x)) is BLANK):
                         return False
        return True
    
    def checkWin(self, checker):
        '''
        Return true if checker has three in a row
        '''
        #Check columns
        for c in range(3):
            row_Count = 0
            for r in range(3):
                 if self.getValue((c, r)) == checker:
                     row_Count += 1
            if (row_Count == 3):
                self._winner = checker
                return True
            
        #Check rows
        for c in range(3):
            col_Count = 0
            for r in range(3):
                 if self.getValue((r, c)) == checker:
                     col_Count += 1
            if (col_Count == 3):
                self._winner = checker
                return True

        #Check diagonals
        if self.getValue((1, 1)) == checker:
            if ((self.getValue((0, 0)) == checker and self.getValue((2, 2)) == checker)
            or (self.getValue((0, 2)) == checker and self.getValue((2, 0)) == checker)):
                self._winner = checker
                return True
        
        return False

    def row(self, n):
        '''
        Return a list of the values in the selected row (input value)

        Raise AssertionError if selected row out of bounds
        '''
        if(n<0 or n>=3):
            raise AssertionError
        return [self._cells[(x, n)] for x in range(3)]

    def _stringRow(self, character, values):
        #assert len(values) == 3
        return f'{character}{character.join(values)}{character}'
    
    def __str__(self):
        '''
        Returns a string representation of the board.
        '''
        results = []
        for x in range(3):
            results.append(self._stringRow('|', self.row(x)))
        return '\n'.join(results)

    def reset(self):
        '''
        Fills in every cell with a blank
        '''
        for c in range(3):
            for r in range(3):
                self.setValue((c, r), BLANK)