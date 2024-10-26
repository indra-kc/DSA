def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs and (not stack or stack.pop() != pairs[char]):
            return False
    return not stack

# Example usage
if __name__ == "__main__":
    test_string = "{[()]}"  # Example of valid parentheses
    if is_valid_parentheses(test_string):
        print("The string has valid parentheses.")
    else:
        print("The string does not have valid parentheses.")
