**Approach**



Bucket Sort Approach



1. First we initialize a hashmap and then we count the frequencies of all the elements in the input
2. Then we initialize an array for our buckets and after we finish counting. Lets say 2 occurs 4 times: Then we set append to to freq[4]
3. Then when we return the result, we start from the back of the frequency array and return in that order.
4. We return the result when the length of our output is k