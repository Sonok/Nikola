class TicTacToe:

    def __init__(self, n: int):
        self.n = n

        self.row_one_list = [0] * n # the ith row tells how many moves from player 1
        self.row_two_list = [0] * n # the ith row tells how many moves from player 2

        self.col_one_list = [0] * n # the ith col tells how many moves from player 1
        self.col_two_list = [0] * n # the ith col tells how many moves from player 2

        self.left_diagonal_one = 0
        self.right_diagonal_one = 0

        self.left_diagonal_two = 0
        self.right_diagonal_two = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            if row == col:
                self.left_diagonal_one += 1
            if row + col == self.n - 1:
                self.right_diagonal_one += 1
            self.row_one_list[row] += 1
            self.col_one_list[col] += 1

            if(self.row_one_list[row] == self.n or self.col_one_list[col] == self.n or 
                self.left_diagonal_one == self.n or self.right_diagonal_one == self.n):
                return 1
        else:

            if row == col:
                self.left_diagonal_two += 1
            if row + col == self.n - 1:
                self.right_diagonal_two += 1
            self.row_two_list[row] += 1
            self.col_two_list[col] += 1

            if(self.row_two_list[row] == self.n or self.col_two_list[col] == self.n or 
                self.left_diagonal_two == self.n or self.right_diagonal_two == self.n):
                return 2
        
        return 0
        


       

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)