Approach



1.First we make a new ListNode head. Then we compare the two elements of the two linked lists to decide which one to add to our new LinkedList at each stage,
2.We keep this process going as long as list1 and list2 have nodes.,
3.At the end of the list we check if either list1 or list2 has any nodes left after the while loop,



Time: O(n) We need to parse through the entire list once



Space: O(n) we store both linked lists into a new merged linked list.