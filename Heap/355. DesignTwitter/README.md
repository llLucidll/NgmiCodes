### Approach 


1. We keep track of each user's following list and each user's tweets in two separate data structures at initialization


2. Then when we want to get the news feed we do the following iterative process:
    1. We take the most recent tweet from every user we follow, then we heapify once we are done.
    2. After that, we pop the most recent tweet from this collection and put that into feed.
    3. We replace the popped tweet with the most recent tweet from the same user, if that user has no more tweets, then we dont add anything
    4. We continue doing this until either there are no more tweets left to add in or the feed has gotten to size 10.
    5. then we return the feed




Time: O(F + 10logF)   To initially build the heap from step 1, we call heapify once on a list of F items O(F).
Then at worst we pop from the heap 10 times when it has F items O(10logF). So the net complexity can be simplified to O(F)



Space: O(N * T) where N is the number of users on the app and T is the highest number of tweets from a single user.



