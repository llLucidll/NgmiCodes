**Approach**



1. First we initalize a set "seen" to keep track of non duplicate characters
2. Then we parse through our string. Everytime we see a non duplicate character we add it to our set and update "longest"
3. If we see a duplicate character we enter the while loop and keep removing characters from the left until that character is no longer present in our substring.
4. This way we evaluate all potential substrings that can be longest substrings.



Time: O(n) We pass through the entire input once.


Space: O(m) where m is the unique alphabets in the input string (Since we use a set, duplicates will get removed)
