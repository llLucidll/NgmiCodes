**Approach**



1. To solve this problem using sliding window, we notice one thing. Lets say we have a window of length 4. The most frequent occuring character in that window is B with freq 3 and A with freq 1. If k = 1 then we know we can swap the A (least frequent character) to make our window valid.

2. We will be using this intuition for the problem. We basically find the most frequent character in our current window and check if its valid to replace all other characters with our current k to make the window valid. 
3. If the window is not valid then we move the left pointer up by 1 and decrement our counter for the old s[l] character.
4. The condition to check if the window is valid is windowLength - maxFrequency > k




Time: O(n) We only require a single pass of the entire string



Space: O(m) where m is the number of unique alphabets in the string