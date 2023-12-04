

# global snow production wrong, 
# got a map, 
# the elves used stars to mark the top fifty locations that are likely to be having problems
# i need to check all fifty stars by december 25th
# 

#the calibration value can be found by combining
#the first digit and the last digit (in that order) to form a single two-digit number.

# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".



numbers_in_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4, 
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine" : 9,
    "zero": 0,
    #edge cases
    "eigh": 8,
    "nin": 9,
    "tw": 2,
    "on": 1,
    "thre": 3,
    "fou": 4,
    "fiv": 5,
    "seve": 7,
    "ight": 8,

}

class Combiner:
    def __init__(self,input_file):
        self.lines = [] #str
        self.digits = []
        self.input_file = input_file
        self.load_input()
        self.combine()
        print("<<<<<")
        print(self.total_sum())
         
    def load_input(self):
        with open(self.input_file) as f:
            for line in f:
                line = line.strip()
                self.lines.append(line)
    
    def replace_words_with_numbers(self,line : str):
        replaced_word = ""
        original_line = line
        for word in numbers_in_words:
            if word in original_line:
                line = line.replace(word, str(numbers_in_words[word]))
                #insert last character of word into line
        return line

    def combine(self):
        for line in self.lines:
            original_line = line
            # line = self.duplicate_characters(line)
            line = self.replace_words_with_numbers(line)
            digits = [char for char in line if char.isdigit()]
            if len(digits) >= 2:
                self.digits.append(digits[0] + digits[-1])
            elif len(digits) == 1:
                self.digits.append(digits[0] * 2)
            print(original_line, line, self.digits[-1])
                
    def total_sum(self):
        return sum([int(x) for x in self.digits])



if __name__ == "__main__":
    file = "Day 1/input.txt"
    main = Combiner(file)