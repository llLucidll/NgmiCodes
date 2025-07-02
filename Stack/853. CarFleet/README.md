**Approach**



1. We notice that to check if two cars form a fleet, we just need to check if (target - pos) / s is equal or less between adjacent cars.
2. We sort our cars by descending order of positions so we can see how many fleets end up forming. We do this because if all cars behind the farthest car reaches it, we know there will only end up being one fleet.
3. We start by creating a list with tuples combining information of both the position and the speed of the cars.
4. Then we sort this list by Descending order for the reason discussed above.
5. Finally we parse through this list and append to our stack the value from our formula in step 1.
6. When the length of the stack goes above 1, we compare the top 2 elements of the stack and if they are of equal or the top most is lesser than the 2nd top, we pop the top of the stack. This means the car forms a fleet with the 2nd top car in the stack and as such we pop the redundant car.
7. At the end the number of elements left in our stack is the number of car fleets that will reach the destination



Time: O(nlogn) We sort the inputs by descending order so that is the dominant term in time complexity 


Space: O(n) At worst case, we can store the entire input array as there are n car fleets.