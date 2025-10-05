**Approach**


1. DFS:
    1. We keep track of a self.area in our dfs function where everytime dfs is called we up the count
    2. At the end once we find no more connected 1's we set result to the max of (result, self.area)
    3. We iterate this process for all disconnected islands



Time: O(n*m) where n is the number of rows and m is the number of columns 


Space: O(n*m) If the entire grid is an island then we will have the entire grid in our recursion stack at some point 


2. BFS:
    1. The only difference here is that we maintain a queue structure and explore nodes on a first come first serve basis
    2. We add to self.count everytime we add a node to our queue 
    3. Update max_area once we exit the inital bfs call in our for loop



Time: O(n*m) where n is the number of rows and m is the number of columns


Space: O(n*m) If the entire grid is an island then our queue will have the entire grid inside it at some point 