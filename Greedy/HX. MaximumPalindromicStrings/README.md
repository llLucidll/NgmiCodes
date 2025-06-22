Description


You are given an array of strings arr of length n, where each arr[i] consists of lowercase English letters. A string is called a palindrome if it reads the same forwards and backwards.

You may perform the following operation any number of times (including zero):

Choose any two strings arr[x] and arr[y] (1-based indices, but you may treat them 0-based in your code) and any two positions i in arr[x] and j in arr[y].

Swap the characters arr[x][i] and arr[y][j].

Return the maximum number of strings in arr that can be made palindromic by applying the above operation any number of times.


Input:  arr = ["pass", "sas", "asps", "df"]
Output: 3
Explanation:
- Initially you have ["pass","sas","asps","df"].
- Swap arr[0][2] with arr[2][0]: 
    "pass" → "paas",  "asps" → "ssps"
  Array becomes ["paas","sas","ssps","df"].
- Swap arr[0][3] with arr[2][2]: 
    "paas" → "paap",  "ssps" → "ssss"
  Array becomes ["paap","sas","ssss","df"].
Now three strings are palindromes: "paap", "sas", "ssss".  
No further swaps can increase this count.


Input:  arr = ["abc", "def", "ghi"]
Output: 0
Explanation:
All characters are distinct across and within strings—no swaps can create a palindrome.


**Approach** 


1. First we count the total number of characters we have and also the lengths of the words in the array
    1. After counting the letters we initalize a count for the total pair letters and total singleton letters
2. Then we sort the lengths array to greedily build palindromes from shortest to longest
3. while building the palindromes we dynamically update the total number of pairs and singletons we have used.
4. if either of them exceed we break the loop
5. Return the number of palindromes we were able to form.

Time: O(nlogn)


Space: O(n)