import time
from player import HumanPlayer, RandomComputerPlayer



class TicTacToe:
    def __init__(self):
          self.board=[" " for _ in range (9)] # using single list to iterate for 3x3 board
          self.current_winner= None # keeps track of the winner
    def print_board(self):
          for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
              print(" | "+ " | ".join(row)+" | ")

    @staticmethod
    def print_board_nums():
           #giving indices
           number_board=[[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
           for row in number_board:
               print(" | "+" | ".join(row)+" | ")


    def available_moves(self):
         #return []
        moves=[]
        for (i,spot) in enumerate(self.board):
            if spot==" ":
                moves.append(i)
        return moves
        
    def empty_squares(self):
         return ' 'in self.board
    
    def num_empty_squares(self):
         return self.board.count(' ')
    
    def make_move(self,square,sign):
        if self.board[square]==' ':
           self.board[square]=sign
           if self.winner(square,sign):
              self.current_winner=sign
           return True
        return False
    

    def winner(self,square,sign):
        #possibilities of winning 
        row_ind= square//3
        row=self.board[row_ind*3 : (row_ind +1)*3]
        if all([spot==sign for spot in row]):
           return True
        
        col_ind=square % 3
        column=[self.board[col_ind+i*3] for i in range(3)]
        if all([spot==sign for spot in column]):
            return True
        
        #diagonal when square is an even number(0,2,4,6,8)
        if square%2==0:
            diagonal1=[self.board[i] for i in [0,4,8]]
            if all([spot==sign for spot in diagonal1]):
               return True
            diagonal2=[self.board[i] for i in [0,4,8]]
            if all([spot==sign for spot in diagonal2]):
               return True
            
        #if all checks fails
        return False

def play(game,x_player,o_player,print_game=True):
    #returning the winner and returning none if its a tie
    if print_game:
       game.print_board_nums()
    sign='X'
    while game.empty_squares():
        if sign=='O':
            square=o_player.get_move(game)
        else:
             square=x_player.get_move(game)
        
        #making a move
        if game.make_move(square,sign):
            if print_game:
                print(sign+f' makes a move to square{square}\n') 
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                   print(sign +' is the winner  !!\n WOOH WOOH!!')
                return sign
            #alternating signs
            sign='O' if sign=='X' else 'X'
        #tiny break
        time.sleep(0.8)
        
    if print_game:
       print("Its a tie. WoW \n Moye MOye :)")


if __name__=='__main__':
    x_player=HumanPlayer('X')
    o_player=RandomComputerPlayer('O')
    t=TicTacToe()
    play(t,x_player,o_player,print_game=True)
