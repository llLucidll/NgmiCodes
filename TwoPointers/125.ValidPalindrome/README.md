**Approach**


1. We have to skip past any non alphanumeric characters. For this we can write a function called isalphanum() that can be called to check if the current index is alphanum
    1. We do this by checking if the character lies between a-z or A-Z or 0-9

2. We use a classic two pointer approach and keep a while loop going as long as l < r
3. If we find its not a palindrome at any point we break. If its non alphanumeric, we skip that specific pointer forward.
4. Advance the pointers towards each other if all conditions are fufilled.



Time: O(n) We parse through the entire string


Space: O(1)