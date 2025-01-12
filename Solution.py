class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        
        # If the length of the string is odd, it's impossible to have valid parentheses
        if n & 1: return False

        # Variables to count the number of unmatched opening and closing parentheses
        closingParenthesis = openingParenthesis = 0
        
        # Forward pass: Left to right through the string
        for currentIndex in range(n):
            # If the current position is unlocked (locked == '0'), treat it as flexible, increment the closing parentheses counter
            if locked[currentIndex] == '0': 
                closingParenthesis += 1  
            elif s[currentIndex] == '(':  # If it's a locked '('
                openingParenthesis += 1  # Increment the opening parentheses counter
            else:  # If it's a locked ')'
                # Try to match a closing parenthesis with an unmatched opening parenthesis
                if openingParenthesis > 0:  
                    openingParenthesis -= 1  # Found a matching '(' for ')'
                # If there's no matching opening parenthesis, check if we can match with a flexible parenthesis
                elif closingParenthesis > 0:  
                    closingParenthesis -= 1  # Match with a flexible parenthesis
                else:
                    return False  # If neither a matching '(' nor flexible parenthesis is found, return False
        
        # Second pass: Right to left through the string
        currentBalance = 0
        for currentIndex in range(n-1, -1, -1):
            # For unlocked positions (locked == '0'), we assume they can either be '(' or ')'
            if locked[currentIndex] == '0':
                currentBalance -= 1  # Assume it's a closing parenthesis
                closingParenthesis -= 1  # Decrease flexible parenthesis count
            elif s[currentIndex] == '(':  # If it's a locked '('
                currentBalance += 1  # Increment balance for opening parenthesis
                openingParenthesis -= 1  # Decrease locked '(' count
            elif s[currentIndex] == ')':  # If it's a locked ')'
                currentBalance -= 1  # Decrease balance for closing parenthesis
            
            # If at any point, balance becomes positive, it indicates unmatched open parentheses
            if currentBalance > 0: return False
            
            # If all opening and closing parentheses have been balanced, break out of the loop
            if closingParenthesis == 0 and openingParenthesis == 0: break

        # Return True if there are no unmatched opening parentheses left
        return openingParenthesis == 0