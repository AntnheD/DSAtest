def reverse_string_using_stack(input_string):
    stack = []  
    for char in input_string:
     
        stack.append(char) 
         

    reversed_string = "" 
    while stack:
        reversed_string += stack.pop() 

    return reversed_string


input_str = "hello"
reversed_output = reverse_string_using_stack(input_str)
print("Input string:", input_str)
print("Reversed output:", reversed_output)
