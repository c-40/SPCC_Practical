# import re

# Tokens = [
#     ('IDENTIFIER', r'[a-zA-Z_]\w*'), 
#     ('CONSTANT', r'\d+(\.\d+)?'),     
#     ('LITERAL', r'\".*?\"'),          
#     ('OPERATOR', r'\+|\-|\*|\/|=|==|!=|<|>|<=|>=|&&|\|\|'),  # Added '&&' and '||' to the pattern
#     ('PUNCTUATOR', r'\(|\)|\{|\}|\[|\]|,|;'),            
#     ('WHITESPACE', r'\s+'),          
#     ('NEWLINE', r'\n'),                
# ]

# def lexems(input_string):
#     tokens = []
#     position = 0
#     while position < len(input_string):
#         match = None
#         for token_type, regex_pattern in Tokens:
#             regex = re.compile(regex_pattern)
#             match = regex.match(input_string, position)
#             if match:
#                 value = match.group(0)
#                 if token_type != 'WHITESPACE' and token_type != 'NEWLINE':
#                     tokens.append((token_type, value))
#                 position = match.end()
#                 break  # Exit the loop if a match is found
#         if not match:
#             position += 1  # Move to the next character if no match is found
#     return tokens

# input_string = input('Enter the string:')
# tokens = lexems(input_string)
# for token in tokens:
#     print(token)


import re
Tokens = [
    ('IDENTIFIER', r'[a-zA-Z_]\w*'), 
    ('CONSTANT', r'\d+(\.\d+)?'),     
    ('LITERAL', r'\".*?\"'),          
    ('OPERATOR', r'\+|\-|\*|\/|=|==|!=|<|>|<=|>=|&&|\|\|'),  # Added '&&' and '||' to the pattern
    ('PUNCTUATOR', r'\(|\)|\{|\}|\[|\]|,|;'),            
    ('WHITESPACE', r'\s+'),          
    ('NEWLINE', r'\n'),                
]

def detect(input_string):
    token=[]
    position=0
    while position < len(input_string):
        match=None
        for token_type,regex_pattern in Tokens:
            regex=re.compile(regex_pattern)
            match=regex.match(input_string,position)
            if match:
                values=match.group()
                if token_type!='WHITESPACE' and token_type!='NEWLINE':
                    token.append((token_type,values))
                position=match.end(0)
                break
        
    return token

input_string=input('Expression:')
tokens=detect(input_string)
for token in tokens:
    print(token)
    
        
