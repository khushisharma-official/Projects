from maze import Maze
from player import Player
import os
import json

class GameEngine:
    def __init__(self):
        self.maze = None
        self.player = None

    def start(self):
        choice = self.show_menu()

        if choice == "1":
            self.new_game()
        elif choice == "2":
            self.load_game()
        else:
            print("Invalid choice. Exiting...")

    def show_menu(self):
        print("\n1. Start New Game")
        print("2. Load Game")
        return input("Enter your choice: ")

    def new_game(self):
        print("\nStarting new game...")
        self.maze = Maze(rows=10, cols=10)
        self.player = Player(start_pos=self.maze.start_pos)
        self.play()

    def load_game(self):
        print("\nAvailable saves:")
        saves = os.listdir("saved_games")
        if not saves:
            print("No saved games found.")
            return self.start()

        for i, save_file in enumerate(saves):
            print(f"{i+1}. {save_file}")

        try:
            choice = int(input("Choose a save to load: ")) - 1
            with open(f"saved_games/{saves[choice]}", "r") as f:
                data = json.load(f)
                self.maze = Maze.from_dict(data["maze"])
                self.player = Player.from_dict(data["player"])
            self.play()
        except Exception as e:
            print("Failed to load save:", e)

    def play(self):
        print("✅ Reached play()")
        print("Maze start position:", self.maze.start_pos)
        print("Player position:", self.player.position)

        move = input("Enter any key to continue: ")
        print("You typed:", move)
        # while True:
        #     # os.system('cls' if os.name == 'nt' else 'clear')
        #     print('\n' * 20)
        #     self.maze.display(self.player.position)

        #     move = input("Move (WASD) or Q to quit: ").lower()

        #     if move == "q":
        #         self.save_game()
        #         print("Game saved. Goodbye!")
        #         break

        #     if move in ['w', 'a', 's', 'd']:
        #         self.player.move(move, self.maze)
        #         if self.player.position == self.maze.end_pos:
        #             print("🎉 Congratulations! You've escaped the maze!")
        #             break
        #     else:
        #         print("Invalid input!")

    def save_game(self):
        if not os.path.exists("saved_games"):
            os.makedirs("saved_games")

        save_data = {
            "maze": self.maze.to_dict(),
            "player": self.player.to_dict()
        }
        name = input("Enter save file name: ")
        with open(f"saved_games/{name}.json", "w") as f:
            json.dump(save_data, f)
