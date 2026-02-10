### Approach 

1. First we set up a hashmap that initializes the count of the t string.
2. Then we use a sliding window. We intiially move the right pointer until we find a valid substring and once we find a valid substring, we minimize by moving the left pointer. Then once we cant minimize anymore we cache this result and move the right pointer again.
3. Return the substring at the end that is our result.