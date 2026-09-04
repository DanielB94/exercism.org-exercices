def is_paired(input_string):
    string_list = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in input_string:
        if char in ')}]' and not string_list:
            return False
        elif char in '({[':
            string_list.append(char)
        elif char in pairs:
            if string_list[-1] == pairs[char]:
                string_list.pop()
            else :
                return False
    return not string_list
