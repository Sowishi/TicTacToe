import os
class Board:
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
        
    def display(self):
        print("{}|{}|{}|".format(self.cells[1],self.cells[2],self.cells[3]))
        print("______")
        print("{}|{}|{}|".format(self.cells[4],self.cells[5],self.cells[6]))
        print("______")
        print("{}|{}|{}|".format(self.cells[7],self.cells[8],self.cells[9]))
        print("______")
        
    def update(self,type,cell):
        self.cells[cell] = type
        
    def reset(self):
        for i in range(len(self.cells)):
            self.cells[i] = " "
      
    def win(self):
        winning = [[1,2,3,],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for row in winning:
            if self.cells[row[0]] == "X" and self.cells[row[1]] == "X" and self.cells[row[2]] == "X":
                print("Player 1 wins")
                return True
            if self.cells[row[0]] == "O" and self.cells[row[1]] == "O" and self.cells[row[2]] == "O":
                print("Player 2 wins")
                return True
    def draw(self):
        draw = True
        for i in range(1,len(self.cells)):
            if self.cells[i] == " ":
                draw = False
        return draw
                    
def refresh():
    os.system("clear")
board = Board()

#Game loop
board.display() 
while True:
    try:
        player1 = int(input("[PLAYER 1] choose a cell: "))
        if player1 == -1:
            break
        if board.cells[player1] != " ":
            while True:
                player1 = int(input("[PLAYER 1] choose a cell: "))
                if board.cells[player1] ==  " ":
                    break  
        refresh()
        board.update("X",player1)
        board.display()
        if board.draw():
            print("draw")
            break
        if board.win():
           break
        player2 = int(input("[PLAYER 2] choose a cell: "))
        if player2 == -1:
            break
        if board.cells[player2] != " ":
            while True:
                 player2 = int(input("[PLAYER 2] choose a cell: "))
                 if board.cells[player2] ==  " ":
                    break     
        refresh()
        board.update("O",player2)
        board.display()
        if board.draw():
            print("draw")
            break
        if board.win():
            break
    except ValueError:
        print("input must be a number")
    except IndexError:
        print("Please enter a number between 1-9")
        
    
    
    