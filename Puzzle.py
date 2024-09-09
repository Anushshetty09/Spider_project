import random

def create_puzzle():
    puzzle = list(range(1, 16)) + [0]  # 0 represents the empty space
    random.shuffle(puzzle)
    return [puzzle[i:i + 4] for i in range(0, len(puzzle), 4)]  # Create 4x4 grid

def display_puzzle(puzzle):
    for row in puzzle:
        print(' '.join(f'{num:2}' if num != 0 else '  ' for num in row))
    print()

def find_empty(puzzle):
    for i, row in enumerate(puzzle):
        if 0 in row:
            return i, row.index(0)

def is_solved(puzzle):
    solution = list(range(1, 16)) + [0]
    return sum(puzzle, []) == solution

def move_tile(puzzle, direction):
    x, y = find_empty(puzzle)
    
    if direction == 'up' and x < 3:
        puzzle[x][y], puzzle[x+1][y] = puzzle[x+1][y], puzzle[x][y]
    elif direction == 'down' and x > 0:
        puzzle[x][y], puzzle[x-1][y] = puzzle[x-1][y], puzzle[x][y]
    elif direction == 'left' and y < 3:
        puzzle[x][y], puzzle[x][y+1] = puzzle[x][y+1], puzzle[x][y]
    elif direction == 'right' and y > 0:
        puzzle[x][y], puzzle[x][y-1] = puzzle[x][y-1], puzzle[x][y]
    else:
        print("Invalid move!")

def puzzle_game():
    puzzle = create_puzzle()
    
    while not is_solved(puzzle):
        display_puzzle(puzzle)
        move = input("Enter move (up/down/left/right): ").lower()
        move_tile(puzzle, move)
    
    display_puzzle(puzzle)
    print("Congratulations! You've solved the puzzle!")

if __name__ == "__main__":
    puzzle_game()
