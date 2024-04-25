class Parsers():
    def __init__(self,input_string):
        self.input_string=input_string
        self.current_index=0
    def parser(self):
        print('RDS')
        print("Input\t\t\tAction")
        self.S()
        if self.current_index==len(input_string):
            print('Success')
        else:
            print('Unsuccessful')
    def match(self,chara):
        if chara==self.input_string[self.current_index]:
            
            print(f"{self.input_string[self.current_index:]}\t\t\tMatch {chara}")
            self.current_index+=1
    def S(self):
        print(f'{self.input_string[self.current_index:]}\t\t\tS->cA')
        self.match('c')
        self.A()
    def A(self):
        if self.input_string[self.current_index:self.current_index+2]=='ad':
            print(f'{self.input_string[self.current_index:]}\t\t\tA->ad')
            self.match('a')
            self.match('d')
            

        else:
            print(f'{self.input_string[self.current_index:]}\t\t\tBacktrack no match A->ad')

        if self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'a':

            self.match('a')
            print(f'{self.input_string[self.current_index:]}\t\t\tA->a')

        if self.current_index<len(self.input_string):
            self.S()
input_string=input("Enter string")
parse=Parsers(input_string)
parse.parser()

