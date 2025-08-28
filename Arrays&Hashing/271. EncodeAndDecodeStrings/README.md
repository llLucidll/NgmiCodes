**Approach**



1. Encoding:
    1. We first append all the lengths of the words in the list. The format is length "," length "," "#" to signify end of lengths
    2. Following this are the words themselves appended on

2. Decode:
    1. First we initalize a sizes array and an empty array for our result
    2. then we add all the sizes from the front of the string to our sizes array
    3. Then we take the string from i: i + sz and append it to our result




Time: O(m) where m is the sum of the lengths of all the strings 



Space: O(m + n) Since we add the numbers for the size of each string to the final result we need to add m extra characters.