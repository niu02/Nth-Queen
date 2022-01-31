n = 8 #number of queens/dimensions of board
qc = 0 #'queen count' the current number of queens on the board

grid = [[0]*n for i in range(n)] #creation of grid to match the n number
    

def print_grid(): #prints the grid
    for l in grid:
        for sq in l:
            if sq == 0:
                print(".", end=" ") #replaces 0s with a .
            elif sq == 1:
                print("Q", end=" ") #replaces 1s with a Q
        print()

def check(grid,y,x):
    for i in range(n): #checking each row for a queen
        if grid[y][i] == 1:
            return False
    for i in range(n): #checking each column
        if grid[i][x] == 1:
            return False
    for i in range(n): #checking diagonals
        for j in range(n):
            if grid[i][j] == 1:
                if abs(i-y) == abs(j-x): 
                    return False
    return True

def solve():
    global qc
    for y in range(n): #going through each row
        for x in range(n): #and each column
            if grid[y][x] == 0 and check(grid,y,x): #if a square is 0 and passes the checks
                if qc != y: #if number of current queens does not match the column number
                    return #return as a queen must be missing somewhere
                grid[y][x] = 1
                qc += 1 #add 1 to queen count if successful placement of a queen
                solve()
                grid[y][x] = 0
                qc -= 1 #remove 1 from queen count if placement unsuccessful       
    if qc == n: #when queen count matches the n number, the puzzle is complete
        print_grid()
        input("More?") #hitting enter provides another solution and will eventually exhaust all possible solutions



    