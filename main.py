"""Simple 2D grid game prototype."""
import random

def main():
    rows, cols = 5, 5
    player = [2, 2]
    goal = [random.randint(0, rows-1), random.randint(0, cols-1)]
    while True:
        for r in range(rows):
            line = ''
            for c in range(cols):
                if [r, c] == player:
                    line += 'P'
                elif [r, c] == goal:
                    line += 'G'
                else:
                    line += '.'
            print(line)
        if player == goal:
            print("You win!")
            break
        move = input("Move (w/a/s/d): ").lower()
        if move == 'w' and player[0] > 0:
            player[0] -= 1
        elif move == 's' and player[0] < rows - 1:
            player[0] += 1
        elif move == 'a' and player[1] > 0:
            player[1] -= 1
        elif move == 'd' and player[1] < cols - 1:
            player[1] += 1
        else:
            print("Invalid or out of bounds.")
        print("\n" * 2)

if __name__ == "__main__":
    main()