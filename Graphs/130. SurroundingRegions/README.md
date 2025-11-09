**Approach**

### General BFS/DFS method.

The trick is to think of only the O's on the edge and then take care of the O's that are adjoinied to one of the O's on the edge (mark them off to prevent cycles/infinite loops). Those cannot be converted. 
Every other O can be converted to an X at the end.