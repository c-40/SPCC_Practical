def constant_folding(code):
    folding_code=[]
    for line in code:
        if '=' in line :
            var,exp=line.split('=')
            var = var.strip()
            
            try:
                 result=eval(exp.strip(),{})
                 folding_code.append(f"{var} = {result}")
                 
            except:
                folding_code.append(line) 
                          
        else:
            folding_code.append(line)
    return folding_code
def constant_propagation(code):
    symbol_table = {}
    optimized_code = []
    for line in code:
        if '=' in line:
            var,expr=line.split('=')
            var=var.strip()
            if all(char.isdigit() for char in expr.strip()):
                symbol_table[var]=expr.strip()
            else:
                for key,value in symbol_table.items():
                    expr = expr.replace(key, value)  # Correcting string mutation
                optimized_code.append(f"{var}={expr.strip()}")
        else:
            optimized_code.append(line)
    return optimized_code


input_line=[]
print("Enter your code line by line. Enter 'done' when finished.")
while True:
    line=input()
    if line.lower()=='done':
        break
    input_line.append(line)    

# result=constant_folding(input_line)
# for line in result:
#     print(line)

result1=constant_propagation(input_line)
for line in result1:
    print(line)