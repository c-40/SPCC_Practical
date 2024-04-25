class ThreeAddress:
    def __init__(self):
        self.temp=1
    def temp_variable(self):
        temp=f"T{self.temp}"
        self.temp+=1
        return temp
    def transform(self,post):
        stack=[]
        three=[]
        for token in post:
            if token.isalnum():
                stack.append(token)
            else:
                op1=stack.pop()
                op2=stack.pop()
                temp=self.temp_variable()
                three.append(f"{temp}={op1}{token}{op2}")
                stack.append(temp)
        return three
    def infix_to_postfix(self,infix):
        postfix=[]
        stack=[]
        precedance={'*':2,'/':2,'+':1,'-':1,'(':0}
        for token in infix:
            if token.isalnum():
                postfix.append(token)
            elif token=='(':
                stack.append(token)
            elif token==')':
                while stack and stack[-1]!='(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and precedance.get(stack[-1],0) >= precedance[token]:
                    postfix.append(stack.pop())
                stack.append(token)
        postfix.extend(stack[::-1])
        return postfix
input_string='a+b*c'
tre=ThreeAddress()
infix=tre.infix_to_postfix(input_string)
for t in infix:
    print(t,end='')
final=tre.transform(infix)
for t in final:
    print(t)
    