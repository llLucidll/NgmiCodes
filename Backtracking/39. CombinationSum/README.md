### Approach: 


Backtracking with DFS. At each step, try adding each candidate from index i onwards. Pass j (not j+1) as the next index   
because the same number can be reused unlimited times. Prune by returning early when total > target.                                
                                                                                                                                      
Key decisions:                                                                                                                    
  - Loop starts at i to avoid generating permutations of the same combination (e.g., [2,3] and [3,2])                                 
  - Pass j not j+1 to allow reuse of the same element                                                                                 
  - Append/pop (backtrack) around each recursive call                                                                                 
                                                                                                                                      
Time: O(n^(t/m)) where t = target, m = smallest candidate. In the worst case, the recursion tree has depth t/m (keep picking the    
  smallest number until we hit target), and branches n ways at each level. Each leaf also does an O(t/m) copy.                        
                                                                                                                                      
Space: O(t/m) for recursion depth. The result list is extra