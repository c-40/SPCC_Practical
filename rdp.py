class Parser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_index = 0

    def parse(self):
        print("Input\t\t\tAction")
        print("--------------------------------")
        try:
            self.S()
            if self.current_index == len(self.input_string):
                print("String is successfully parsed.")
            else:
                print("Parsing failed: Unexpected characters after parsing.")
        except ValueError:
            print("Parsing failed: Invalid syntax.")

    def match(self, expected_char):
        if self.current_index < len(self.input_string) and self.input_string[self.current_index] == expected_char:
            print(f"{self.input_string[self.current_index:]}\t\t\tMatched {expected_char}")
            self.current_index += 1
        else:
            raise ValueError

    def S(self):
        print(f"{self.input_string[self.current_index:]}\t\t\tS -> cA")
        self.match('c')
        self.A()
        self.match('d')

    def A(self):
        # Attempt to match 'ab'
        if self.input_string[self.current_index:self.current_index+2] == 'ab':
            print(f"{self.input_string[self.current_index:]}\t\t\tA -> ab")
            self.match('a')
            self.match('b')
        else:
            print('used A->ab , no match backtrack ')
            print("Backtracking")
        # If 'ab' is not matched, try matching 'a'
        if self.input_string[self.current_index] == 'a':
            print(f"{self.input_string[self.current_index:]}\t\t\tA -> a")
            self.match('a')
        else:
            # If neither 'ab' nor 'a' is matched, backtrack
            print(f"{self.input_string[self.current_index:]}\t\t\tBacktrack from A")
            raise ValueError


input_string = "cad"
parser = Parser(input_string)
parser.parse()
