Description


Given an integer array arr of length n and an integer divisor d, return the number of distinct triplets (i, j, k) such that:

1. 0 <= i < j < k < n
2. (arr[i] + arr[j] + arr[k]) % d == 0


Input:  arr = [3, 3, 4, 7, 8], d = 5
Output: 3
Explanation:
The triplets with sums divisible by 5 are:
  - (arr[0], arr[1], arr[2]) = (3,3,4) → sum = 10
  - (arr[0], arr[1], arr[4]) = (3,3,8) → sum = 14
  - (arr[1], arr[2], arr[3]) = (3,4,7) → sum = 14


Input:  arr = [1, 2, 3, 4], d = 3
Output: 1
Explanation:
Only the triplet (1,2,3) has sum = 6, which is divisible by 3.



**Approach** 


1. First we do one pass over the list, converting it down to the remainders when divided by d (mod d)
2. We initialize a list pairCount[]. For d = 4, this list will be 4 units long -> [0,0,0,0] corresponding to 0,1,2,3
3. Then as we go over the numbers in the list we do two things.
    1. First check if this number has a count already within our pairCount[]. If it does, we subtract one from the corresponding pairCount[] and we add +1 to our tripletCount
    2. Secondly we pair this number with every number in the list we have seen so far and the mod_d(pair_sum) is used to update pairCount[]
