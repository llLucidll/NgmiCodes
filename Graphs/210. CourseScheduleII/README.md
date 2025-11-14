**Approach**



The way I solved this problem is by building on the Course Schedule 1 approach but now I want a result array to hold my path to take all courses.

I make a new set called added() to keep track of all the courses I already have in the path to not add duplicate prereqs in.

I add courses in during the prereq dfs iterate process if they aren't already in added.

We maintain visiting() for keeping track of and ending cycles.


Time: O(V+E)


Space: O(V+E)