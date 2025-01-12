#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool canBeValid(string s, string locked) {
        int n = s.size();
        
        // If the length of the string is odd, it's impossible to have valid parentheses
        if (n % 2 != 0) return false;

        // Variables to count the number of unmatched opening and closing parentheses
        int closingParenthesis = 0, openingParenthesis = 0;
        
        // Forward pass: Left to right through the string
        for (int currentIndex = 0; currentIndex < n; ++currentIndex) {
            // If the current position is unlocked (locked == '0'), treat it as flexible
            if (locked[currentIndex] == '0') {
                closingParenthesis++;  // Increment the closing parentheses counter
            }
            else if (s[currentIndex] == '(') {  // If it's a locked '('
                openingParenthesis++;  // Increment the opening parentheses counter
            }
            else {  // If it's a locked ')'
                // Try to match a closing parenthesis with an unmatched opening parenthesis
                if (openingParenthesis > 0) {
                    openingParenthesis--;  // Found a matching '(' for ')'
                }
                // If there's no matching opening parenthesis, check if we can match with a flexible parenthesis
                else if (closingParenthesis > 0) {
                    closingParenthesis--;  // Match with a flexible parenthesis
                }
                else {
                    return false;  // If neither a matching '(' nor flexible parenthesis is found, return false
                }
            }
        }

        // Second pass: Right to left through the string
        int currentBalance = 0;
        for (int currentIndex = n - 1; currentIndex >= 0; --currentIndex) {
            // For unlocked positions (locked == '0'), we assume they can either be '(' or ')'
            if (locked[currentIndex] == '0') {
                currentBalance--;  // Assume it's a closing parenthesis
                closingParenthesis--;  // Decrease flexible parenthesis count
            }
            else if (s[currentIndex] == '(') {  // If it's a locked '('
                currentBalance++;  // Increment balance for opening parenthesis
                openingParenthesis--;  // Decrease locked '(' count
            }
            else if (s[currentIndex] == ')') {  // If it's a locked ')'
                currentBalance--;  // Decrease balance for closing parenthesis
            }

            // If at any point, balance becomes positive, it indicates unmatched open parentheses
            if (currentBalance > 0) return false;

            // If all opening and closing parentheses have been balanced, break out of the loop
            if (closingParenthesis == 0 && openingParenthesis == 0) break;
        }

        // Return True if there are no unmatched opening parentheses left
        return openingParenthesis == 0;
    }
};