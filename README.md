# 2116. Check If A Parentheses String Can Be Valid
- ## [Approach 1: Greedy using Stack](https://github.com/madiv9820/12_01_2025--2116_Check_if_a_Parentheses_String_Can_Be_Valid/tree/Approach_01-Greedy_Using_Stacks)
    - ### Intuition:
        1. **Balanced Parentheses**: A valid string of parentheses must have matching pairs of `(` and `)`, with every `(` having a corresponding `)` that follows it.
        2. **Locked vs Unlocked**: Some parentheses are locked (cannot be changed), while others are unlocked (can be either `(` or `)`).
        3. **Flexible Parentheses**: The unlocked parentheses (`locked == '0'`) provide flexibility, allowing them to act as either `(` or `)` based on the needs of the string.
        4. **Stack Utilization**: We use two stacks:
            - One to track unmatched `(` parentheses.
            - Another to track unmatched `)` parentheses (for flexible positions).

    - ### Approach:
        1. **Odd Length Check**: If the length of the string is odd, it's impossible to have a balanced number of opening and closing parentheses, so we return `false` immediately.
        2. **Iterate Through the String**:
            - If a position is unlocked (`locked == '0'`), treat it as flexible and push its index onto a stack.
            - For locked parentheses:
                - If it's a `(`, push its index onto the `openingStack`.
                - If it's a `)`, try to match it with an unmatched `(` from the `openingStack` or a flexible parenthesis from `closingStack`. If no match is found, return `false`.
        3. **Final Check**: After processing the string:
            - Ensure all opening parentheses have been matched with closing parentheses.
            - If any unmatched opening parentheses remain, return `false`.

    - ### Code Implementation:
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
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
            ```

    - ### Time Complexity:
        - **$O(n)$**: We iterate through the string once (to process each character) and perform stack operations (push/pop) which take constant time per operation. Thus, the overall time complexity is linear in terms of the length of the string, where $n$ is the length of the string.

    - ### Space Complexity:
        - **$O(n)$**: The space complexity is determined by the space used to store the indices in the stacks (`openingStack` and `closingStack`). In the worst case, we may need to store all indices if none of the parentheses can be matched early, making the space complexity linear with respect to the size of the input string.

- ## [Approach 2: Greedy Using Constant Space](https://github.com/madiv9820/12_01_2025--2116_Check_if_a_Parentheses_String_Can_Be_Valid/tree/Approach_02-Greedy_Using_Constant_Space)
    - ### Intuition:
        1. **Balanced Parentheses**: A valid string of parentheses must have matching pairs of `(` and `)`, with every `(` having a corresponding `)` that follows it.
        2. **Locked vs Unlocked**: Some parentheses are locked (cannot be changed), while others are unlocked (can be either `(` or `)`).
        3. **Flexible Parentheses**: The unlocked parentheses (`locked == '0'`) provide flexibility, allowing them to act as either `(` or `)` based on the needs of the string.
        4. **Two Pass Strategy**: 
            - **Forward Pass**: Ensure that the parentheses are balanced from left to right, considering unlocked positions as flexible.
            - **Backward Pass**: Ensure that the parentheses are balanced from right to left, also ensuring that flexible positions are considered correctly.

    - ### Approach:
        1. **Odd Length Check**: If the length of the string is odd, it's impossible to have a balanced number of opening and closing parentheses, so return `false` immediately.
        2. **Forward Pass (Left to Right)**:
            - Track unmatched opening and closing parentheses as you iterate through the string.
            - For locked parentheses:
                - If it’s an opening parenthesis `(`, increment the opening parenthesis counter.
                - If it’s a closing parenthesis `)`, try to match it with an unmatched opening parenthesis, or use a flexible position if necessary.
            - For unlocked positions (flexible), treat them as either `(` or `)`, adjusting counters accordingly.
        3. **Backward Pass (Right to Left)**:
            - Similarly, ensure that all parentheses are correctly matched, with flexible positions treated as either `(` or `)` based on the balance.
            - If the balance becomes positive at any point (indicating unmatched opening parentheses), return `false`.
        4. **Final Validation**:
            - After both passes, if there are any unmatched opening parentheses left, return `false`.
            - If the string has been fully balanced, return `true`.
    
    - ### Code Implementation:
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
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
            ```

    - ### Time Complexity:
        - **$O(n)$**: 
            - We iterate through the string twice (once from left to right and once from right to left).
            - Each iteration processes each character of the string, and each stack operation (push/pop) takes constant time, so the overall time complexity is linear in terms of the length of the string, where $n$ is the length of the string.

    - ### Space Complexity:
        - **$O(1)$**:
            - We only use a constant amount of extra space for the counters (`openingParenthesis`, `closingParenthesis`, `currentBalance`).
            - The space used is independent of the input size, making the space complexity constant.