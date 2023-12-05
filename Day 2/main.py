from enum import Enum


class RGB(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


rgb_in_words = {
    "red": RGB.RED,
    "green": RGB.GREEN,
    "blue": RGB.BLUE
}

class Game:
    def __init__(self,i) -> None:
        self.index = i
        self.r = 0
        self.g = 0
        self.b = 0
        self.is_possible = False

    def play_highest_set(self,color : RGB,amount : int):
        if color == RGB.RED and self.r > amount:
            return
        elif color == RGB.GREEN and self.g > amount:
            return
        elif color == RGB.BLUE and self.b > amount:
            return
        
        if color == RGB.RED:
            self.r = amount
        elif color == RGB.GREEN:
            self.g = amount
        elif color == RGB.BLUE:
            self.b = amount
        else:
            pass
    def total_power(self):
        return self.r * self.g * self.b
    
    def play_lowest_set(self,color : RGB,amount : int):
        if color == RGB.RED and self.r < amount:
            return
        elif color == RGB.GREEN and self.g < amount:
            return
        elif color == RGB.BLUE and self.b < amount:
            return
        
        if color == RGB.RED:
            self.r = amount
        elif color == RGB.GREEN:
            self.g = amount
        elif color == RGB.BLUE:
            self.b = amount
        else:
            pass

    def __str__(self) -> str:
        return f"Game {self.index}: {self.r},{self.g},{self.b} - {self.is_possible} - {self.total_power()}"

    def is_not_possible_with(self,r,g,b):
        if self.r > r or self.g > g or self.b > b:
            self.is_possible = False
        else:
            self.is_possible = True
        return self.is_possible

class CubeFinder:
    def __init__(self,input_file) -> None:
        self.lines = []
        self.games = []
        self.possible_games = []
        self.input_file = input_file
        self.load_input()
        for game in self.games:
            possible = game.is_not_possible_with(12,13,14)
            print(game)
            if possible:
                self.possible_games.append(game)
        id_sum = 0
        for game in self.games:
            id_sum += game.total_power()
        print(id_sum)

    def load_input(self):
            current_game = 0
            with open(self.input_file) as f:
                for line in f:
                    current_game += 1
                    # line = line.strip()
                    line = line.strip("\n")
                    game = line.split(":")[1]
                    sets = game.split(";")
                    game = Game(current_game)
                    for i in range(len(sets)):
                        cubes = sets[i].split(",")
                        for cube in cubes:
                            amount_color = cube.strip().split(" ")
                            amount = int(amount_color[0])
                            color = rgb_in_words[amount_color[1]]
                            game.play_highest_set(color,amount)
                    
                    self.games.append(game)







if __name__ == "__main__":
    file = "Day 2/input.txt"
    main = CubeFinder(file)