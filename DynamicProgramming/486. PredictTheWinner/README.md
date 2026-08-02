## Approach 


1. Initially I went for a very stupid solution where I assumed greedy for both players and then realized that a large value on one side of the array would break this assumption

2. The solution for this problem utilized mini-max (remember CMPUT 455) and player's 1's score is calculated relative to player 2's optimal score.

3. At each point we can decide to take left or take right, and we calculate both recursively (score - player 2's optimal score)

4. So at the end, we get the best possible score player 1 can achieve, and if this is greater than zero or equal to, then p1 wins.

5. We use @cache here to memoize return values of the function, so that we dont compute the score for pairs we already did for before


Time: O(n^2) this is because for every index i, there is another index j it can be paired with. So there are upto n^2 pairs of two indices the code can compute for.


Space: O(n^2). this is because our memoization cache can hold upto n^2 keys in it at once worst case.
