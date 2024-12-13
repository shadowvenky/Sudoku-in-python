 

import random
print("\n\n \033[1;32m TECHONOLOGY CLUB \033[1;35m \n")



class Sudoku:
    def __init__(self):
        self.board = self.generate_board()  

    def print_board(self):
        for row in range(len(self.board)):
            if row % 3 == 0 and row != 0:
                print("-" * 21) 
            for col in range(len(self.board[0])):
                if col % 3 == 0 and col != 0:
                    print("|", end=" ")
                if self.board[row][col] == 0:
                    print(".", end=" ") 
                else:
                    print(self.board[row][col], end=" ")
            print()   

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col 
        return None  

    def is_valid(self, num, pos): 
        # Check row 
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False 

        # Check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False 

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False 

        return True  

    def solve(self):
        find = self.find_empty()
        if not find:
            return True 
        else:
            row, col = find 

        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i 

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False  

    def generate_board(self):
        base = 3
        side = base * base   

        # Pattern for a baseline valid solution
        def pattern(r, c):
            return (base * (r % base) + r // base + c) % side   

        # Randomize rows, columns, and numbers (of valid base pattern)
        def shuffle(s):
            return random.sample(s, len(s))    

        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base * base + 1))  

        # Produce a board using randomized baseline pattern
        board = [[nums[pattern(r, c)] for c in cols] for r in rows] 

        # Remove random elements to create a puzzle 
        squares = side * side   
        empties = random.randint(40, 60)  
        for _ in range(empties):  
            x = random.randint(0, side - 1)   
            y = random.randint(0, side - 1)  
            board[x][y] = 0 

        return board 

    def play(self):
        while True:
            self.print_board() 
            print("\n") 
            row = int(input("\033[1;33m Enter row (1-9) :- ")) - 1     # Adjust index by subtracting 1
            col = int(input("\033[1;34m Enter column (1-9) :- ")) - 1    # Adjust index by subtracting 1
            num = int(input("\033[1;36m Enter number (1-9) :- "))
            print("\033[1;35m \n\n")

           
            if self.is_valid(num, (row, col)):                  
                self.board[row][col] = num 
                if not self.find_empty():
                    print("\033[1;31m Congratulations!\033[1;33m You solved the \033[1;32m Sudoku.")
                    break
            else:
                print("\033[1;31m Invalid move! Try again.\033[1;35m\n")
                      


if __name__ == "__main__":
 game = Sudoku() 
game.play()
