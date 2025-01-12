class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        
        # If the length of the string is odd, it's impossible to have valid parentheses
        if n & 1: return False

        # Stacks to store indices of unmatched '(' and ')'
        closingStack, openingStack = [], []
        
        # Iterate through the string to process each character
        for currentIndex in range(n):
            # If the current position is unlocked (locked == '0'), treat it as flexible
            if locked[currentIndex] == '0': 
                closingStack.append(currentIndex)  # Can act as either '(' or ')'
            elif s[currentIndex] == '(':  # If it's a locked '('
                openingStack.append(currentIndex)  # Push the index of '(' onto opening stack
            else:  # If it's a locked ')'
                if openingStack:  # If there’s an unmatched '(' in the opening stack, match it
                    openingStack.pop()  # Pop the matched '(' from opening stack
                elif closingStack:  # If it's flexible, try to match with a previous flexible parenthesis
                    closingStack.pop()  # Pop from closing stack
                else:
                    return False  # If no unmatched '(' or flexible parenthesis available, return False
        
        # After processing the string, check for unmatched parentheses
        while closingStack and openingStack:
            # Both stacks need to match indices such that opening indices are smaller than closing indices
            if openingStack[-1] < closingStack[-1]:  
                closingStack.pop()  # Pop a matching closing parenthesis
                openingStack.pop()  # Pop the matching opening parenthesis
            else:
                return False  # If the indices don’t match (i.e., the order is incorrect), return False
        
        # The string is valid if all opening parentheses have been matched
        return len(openingStack) == 0