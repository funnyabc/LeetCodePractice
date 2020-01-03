class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        """
        if index + 1 > self.size or self.head is None:
            return -1
        runner = self.head
        current_index = 0
        while current_index != index:
            runner = runner.next
            current_index += 1
        return runner.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked 
        list.
        """
        if self.head is None:
            self.head = LinkedListNode(val)
        else:
            new_node = LinkedListNode(val, self.head)
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            self.head = LinkedListNode(val)
        else:
            new_node = LinkedListNode(val)
            runner = self.head
            while runner.next is not None:
                runner = runner.next
            new_node.next = runner.next
            runner.next = new_node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be 
        appended to the end of linked list. If index is greater than the 
        length, the node will not be inserted.
        """
        if index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = LinkedListNode(val)
            runner = self.head
            current_index = 0
            while current_index + 1 != index:
                runner = runner.next
                current_index += 1
            new_node.next = runner.next
            runner.next = new_node
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size or self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            runner = self.head
            current_index = 0
            while current_index + 1 != index:
                runner = runner.next
                current_index += 1
            if index + 1 == self.size:
                runner.next = None
            else:
                runner.next = runner.next.next
        self.size -= 1
