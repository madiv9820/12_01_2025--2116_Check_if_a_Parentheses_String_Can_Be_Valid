#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool canBeValid(string s, string locked) {
        int n = s.size();
        
        // If the length of the string is odd, it's impossible to have valid parentheses
        if (n % 2 != 0) return false;

        // Stacks to store indices of unmatched '(' and ')'
        stack<int> closingStack, openingStack;
        
        // Iterate through the string to process each character
        for (int currentIndex = 0; currentIndex < n; ++currentIndex) {
            // If the current position is unlocked (locked == '0'), treat it as flexible
            if (locked[currentIndex] == '0') {
                closingStack.push(currentIndex);  // Can act as either '(' or ')'
            }
            else if (s[currentIndex] == '(') {  // If it's a locked '('
                openingStack.push(currentIndex);  // Push the index of '(' onto opening stack
            }
            else {  // If it's a locked ')'
                if (!openingStack.empty()) {  // If there’s an unmatched '(' in the opening stack, match it
                    openingStack.pop();  // Pop the matched '(' from opening stack
                }
                else if (!closingStack.empty()) {  // If it's flexible, try to match with a previous flexible parenthesis
                    closingStack.pop();  // Pop from closing stack
                }
                else {
                    return false;  // If no unmatched '(' or flexible parenthesis available, return false
                }
            }
        }

        // After processing the string, check for unmatched parentheses
        while (!closingStack.empty() && !openingStack.empty()) {
            // Both stacks need to match indices such that opening indices are smaller than closing indices
            if (openingStack.top() < closingStack.top()) {
                closingStack.pop();  // Pop a matching closing parenthesis
                openingStack.pop();  // Pop the matching opening parenthesis
            } else {
                return false;  // If the indices don’t match (i.e., the order is incorrect), return false
            }
        }

        // The string is valid if all opening parentheses have been matched
        return openingStack.empty();
    }
};