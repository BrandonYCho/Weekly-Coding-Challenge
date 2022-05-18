class Node:
    def __init__(self, data=None):
        self.data = data   # node is created with data
        self.next = None    # Link is made null

class LinkedList:
    def __init__(self):      # Create Linked List
        self.head = None  # Link to first node

    def printList(self):
        printnode = self.head
        while printnode is not None:
            print(printnode.data)
            printnode = printnode.next

    def insert_at_front(self, new_data):
        NewNode = Node(new_data)
        NewNode.next = self.head
        self.head = NewNode

    def insert_at_end(self, new_data):
        NewNode = Node(new_data)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode
    
    def insert_between(self, middle_node, new_data):
        if middle_node is None:
            print("The node does not exist")
            return
        NewNode = Node(new_data)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def remove_node(self, remove_val):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == remove_val):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == remove_val:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None
    
    def reverse_list(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

def SumLists(first_list, second_list):
    result_list = LinkedList()
    temp = 0

    first_node = first_list.head
    second_node = second_list.head
    while first_node or second_node or temp:
        if first_node:
            temp += first_node.data
            first_node = first_node.next
        if second_node:
            temp += second_node.data
            second_node = second_node.next
        
        result_list.insert_at_end(temp % 10)
        temp = temp // 10

    return result_list

def SumLists_Rev(first_list, second_list):
    first_list.reverse_list()
    second_list.reverse_list()
    result_list = LinkedList()
    result_list = SumLists(first_list, second_list)
    result_list.reverse_list()
    return result_list

## Testing
## List 1 (7,1,6)
list1 = LinkedList()
list1.head = Node(7)
list1.head.next = Node(1)
list1.insert_at_end(6)
#list1.printList()

## List 2 (5,9,2)
list2 = LinkedList()
list2.head = Node(5)
list2.head.next = Node(9)
list2.insert_at_end(2)
#list2.insert_at_front(8374)
#list2.printList()
#print("Removing node")
#list2.insert_between(list2.head.next, 10)
#list2.printList()

## SumLists
print("SumLists")
print("Input: (7-> 1 -> 6) + (5 -> 9 -> 2)")
print("List 1: ")
list1.printList()
print("List 2: ")
list2.printList()
print("Output: 2 -> 1 -> 9")
list3 = SumLists(list1, list2)
list3.printList()

## FOLLOW UP
## List 4 (6,1,7)
list4 = LinkedList()
list4.head = Node(6)
list4.head.next = Node(1)
list4.insert_at_end(7)

## List 5 (2,9,5)
list5 = LinkedList()
list5.head = Node(2)
list5.head.next = Node(9)
list5.insert_at_end(5)

## SumLists_Rev
print("SumList_Alt")
print("Input: (6 -> 1 -> 7) + (2 -> 9 -> 5)")
print("List 4: ")
list4.printList()
print("List 5: ")
list5.printList()
print("Output: 9 -> 1 -> 2")
list6 = SumLists_Rev(list4, list5)
list6.printList()