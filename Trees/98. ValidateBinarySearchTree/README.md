### Approach                                                                                                                            
                                                                                                                                      
1. DFS:                                                                                                                             
    a. Pass down (low, high) bounds, starting with (-inf, inf)                                                                        
    b. At each node, check low < node.val < high                                                                                      
    c. Recurse left with (low, node.val) and right with (node.val, high)       
2. BFS:                                                                                                                             
    a. Queue stores tuples of (node, low, high), starting with (root, -inf, inf)
    b. For each node, check low < node.val < high                                                                                     
    c. Enqueue left child with (low, node.val) and right child with (node.val, high)                                                  
                                                                                                                                      
Time: O(n) — visit every node once                                                                                                  

                                                                               
Space: O(n) — queue/recursion stack holds up to O(n) nodes in the worst case