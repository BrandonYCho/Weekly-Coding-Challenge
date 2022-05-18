# Assignment
1) Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.

- EXAMPLE
	- Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
	- Output: 2 -> 1 -> 9. That is, 912.
- FOLLOW UP
	- Suppose the digits are stored in forward order. Repeat the above problem.
	- Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
	- Output: 9 -> 1 -> 2. That is, 912.

2) Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time.

## StackMin.py
- Contains class Stack that allows the user to create Stack objects with basic stack features.
- Noteable methods:
	- push to insert
	- pop to remove top element
	- getMin returns min value of the stack
- Contains test code at the end to demonstrate the class

## SumLists.py
- Contains class Node and class LinkedList that allows the user to create a LinkedList with basic LinkedList features.
- Noteable methods:
	- reverse_list to reverse a LinkedList
	- SumLists to perform the first part of the assignment
	- SumLists_Rev to perform the second part of the assignment
- Contains test code at the end to demonstrate the classes
