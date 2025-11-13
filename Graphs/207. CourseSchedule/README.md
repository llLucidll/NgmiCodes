**Approach**



## we use classic DFS 

1. first we premap all the courses to its prereqs.
2. we use a set to keep track of anything that's in our current DFS path.
3. We go through all the courses in numCourses and check for a cycle and if its true we return False 


Time: O(V + E) where V is the number of courses and E is the number of prereqs


Space: O(V + E) Our overhead stack can contain all the courses and its prereqs at once.