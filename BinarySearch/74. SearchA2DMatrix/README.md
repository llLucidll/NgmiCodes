**Approach**



1. To achieve the required time complexity we need to do two binary searches. One vertically and one horizontally.
2. Both searches use the primary concept of binary search to single out subarrays in the horizontal case or arrays (rows) in the vertical case. As such no further explanation is required.



Time: O(log(m*n)) where m is the number of rows and n is the number of columns




Space: O(1) nothing extra is stored into memory