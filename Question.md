# [2116. Check if a Parentheses String Can Be Valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid)

**Type:** Medium <br>
**Topics:** String, Stack, Greedy <br>
**Companies:** Amazon, Google
<hr>

A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is valid if **any** of the following conditions is **true**:
- It is `()`.
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.
- It can be written as `(A)`, where `A` is a valid parentheses string.

You are given a parentheses string `s` and a string `locked`, both of length `n`. `locked` is a binary string consisting only of `'0'`s and `'1'`s. For each index `i` of `locked`,
- If `locked[i]` is `'1'`, you cannot change `s[i]`.
- But if `locked[i]` is `'0'`, you can change `s[i]` to either `'('` or `')'`.

Return `true` *if you can make* `s` *a valid parentheses string*. Otherwise, return `false`.
<hr>

- ### Examples:
    - **Example 1:**<br>
    ![](https://assets.leetcode.com/uploads/2021/11/06/eg1.png)
        ```
        Input: s = "))()))", locked = "010100"
        Output: true
        Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
        We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
        ```
    - **Example 2:** <br>
        ```
        Input: s = "()()", locked = "0000"
        Output: true
        Explanation: We do not need to make any changes because s is already valid.
        ```
    - **Example 3:** <br>
        ```
        Input: s = ")", locked = "0"
        Output: false
        Explanation: locked permits us to change s[0]. 
        Changing s[0] to either '(' or ')' will not make s valid.
        ```
<hr>

- ### Constraints:
    - `n == s.length == locked.length`
    - <code>1 <= n <= 10<sup>5</sup></code>
    - `s[i]` is either `'('` or `')'`.
    - `locked[i]` is either `'0'` or `'1'`.
<hr>

- ### Hints:
    - Can an odd length string ever be valid?
    - From left to right, if a locked ')' is encountered, it must be balanced with either a locked '(' or an unlocked index on its left. If neither exist, what conclusion can be drawn? If both exist, which one is more preferable to use?
    - After the above, we may have locked indices of '(' and additional unlocked indices. How can you balance out the locked '(' now? What if you cannot balance any locked '('?
<hr>