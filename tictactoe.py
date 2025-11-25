def check(func):
    def wrap(*args, **kwargs):
        while 1:
            try:
                return func(*args, **kwargs)
            except:
                print("Invalid Input.")
    return wrap

class Player(object):
    def __init__(self, board, piece, number):
        self.board = board
        self.piece = piece
        self.number = number
        
    def play(self, position):
        if self.board.empty(position):
            self.board._set(position, self.piece)
            return True
        print("Invalid play.")
        return False
    
    @check
    def getInput(self):
        piece = int(input("Enter a position, e.g. 1-9: ")) - 1
        assert 0 <= piece
        assert 9 >= piece
        return piece

    def turn(self):
        while 1:
            if self.play(self.getInput()):
                if self.board.won():
                    print("Player", self.number, "won!")
                    return False
                if self.board.tied():
                    print("Tie game!")
                    return False
            return True
                    
            
class Board(object):
    def __init__(self):
        self.posConv = {n: [n//3, n%3] for n in range(9)}
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8], \
                     [0, 3, 6], [1, 4, 7], [2, 5, 8], \
                     [0, 4, 8], [2, 4, 6]]
        
    def _get(self, position):
        x, y = self.posConv[position]
        return self.board[x][y]

    def _set(self, position, piece):
        x, y = self.posConv[position]
        self.board[x][y] = piece

    def empty(self, position):
        try:
            int(self._get(position))
            return True
        except:
            return False

    def won(self):
        for row in self.rows:
            a, b, c = map(lambda x: self._get(x), row)
            if "_" not in [a, b, c]:
                if a == b and b == c:
                    return True
        return False

    def tied(self):
        if all(not self.empty(position) for position in range(9)):
            return True
        return False
                
    def display(self):
        text = '-------\n'
        for row in self.board:
            for col in row:
                text += '|'+col
            text += '|\n-------\n'
        print(text)

if __name__ == "__main__":           
    board = Board()
    player1 = Player(board, "X", 1)
    player2 = Player(board, "O", 2)

    won = False
    while not won:
        for player in [player1, player2]:
            player.board.display()
            if not player.turn():
                won = True
                break
