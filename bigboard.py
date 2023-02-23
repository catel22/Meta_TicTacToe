import miniboard

class Bigboard:
    def __init__(self):
        '''
        Initializes meta tic-tac-toe board

        _cells: cooordinate is a tuple, occupied by checker
        '''
        self._cells = {}
        self.reset()

    def buildBoard(self):
        '''
        Set each coordinate to a miniboard
        '''
        for c in range(3):
            for r in range(3):
                self._cells[c, r] = miniboard.Miniboard()

    def __str__(self):
        '''
        #Returns a string representation of the board.
        '''
        results = []
        for x in range(3):
                for i in range(3):
                    for n in range(3):
                        results.append(self._cells[i, x]._stringRow('|', self._cells[i, x].row(n)))
                        results.append('  ')
                    results.append('\n')
                results.append('\n')
        return ''.join(results)
    
    def reset(self):
        '''
        Fills in every cell with a blank
        '''
        self.buildBoard()

    def getValue(self, coord):
        '''
        Get the checker value from a given coordinate
        '''
        return (self._cells[coord])
    
    def isFull(self):
        '''
        Returns True if every cell has a checker.
        '''
        for i in range(3):
                for x in range(3):
                    if (not self._cells[i, x].isWon()):
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
                 if self.getValue((c, r)).getWinner() == checker:
                     row_Count += 1
            if (row_Count == 3):
                self._winner = checker
                return True
            
        #Check rows
        for c in range(3):
            col_Count = 0
            for r in range(3):
                 if self.getValue((r, c)).getWinner() == checker:
                     col_Count += 1
            if (col_Count == 3):
                self._winner = checker
                return True

        #Check diagonals
        if self.getValue((1, 1)).getWinner() == checker:
            if ((self.getValue((0, 0)).getWinner() == checker and self.getValue((2, 2)).getWinner() == checker)
            or (self.getValue((0, 2)).getWinner() == checker and self.getValue((2, 0)).getWinner() == checker)):
                self._winner = checker
                return True
        
        return False