# Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly brackets are "balanced."

 
def is_balanced(sequence):
    '''Program to check if parentheses are balanced'''

  
    data_list = []
    for item in range(len(sequence)):

        open_brackets ='{[('
        closing_brackets = '}])'
        dic_brackets = {
            '(':')',
            '{':'}',
            '[':']',
        }
        # Check if the character is an opening bracket
        if sequence[item] in open_brackets:
            data_list.append(sequence[item])
        
        elif sequence[item] in closing_brackets:
            # If it's a closing bracket, check if the stack is non-empty
            # and if the top of the stack is a matching opening bracket
            if data_list and (data_list[-1] in open_brackets and sequence[item] in closing_brackets) and (dic_brackets[data_list[-1]]==sequence[item]):
                # Pop the matching opening bracket
                data_list.pop()
            else:
                # Unmatched closing bracket
                return False


    # If stack is empty, return True (balanced), otherwise False
    return True if not data_list else False


if __name__ == "__main__":
    test_cases = {
        "((()))" : True,           # Balanced
        "{[()]}" : True,           # Balanced
        "({[]})" : True,           # Balanced
        "(()" : False,              # Not balanced 
        "())" : False,              # Not balanced 
        "{[}]" : False,             # Not balanced 
        "" : True,                 # Balanced (empty)
        "abc(def[ghi]j)k": True,   # Balanced 
    }
    
    for test in test_cases:
        assert(is_balanced(test)==test_cases[test])