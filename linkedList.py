class node:
    def __init__(self, data=None):
        #Store the value for the node in self.value.
        self.data = data
        # Leave the node initially without a next value
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        print(total)
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
    
    def get(self, index):
        if index >= self.length():
            print("ERROR: Index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_idx == index:
               return cur_node.data
            cur_idx += 1
    
    def erase(self,index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range")
            return
        cur_idx = 0
        cur_node = self.head
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4) 

my_list.erase(1)
my_list.display()
print(f"element at 2nd index:  {my_list.get(2)}" )

'''21. Merge Two Sorted Lists'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d = ListNode()
        cur = d

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list.next
        
        cur.next = list1 if list1 else list2
        return d.next

'''19. Remove Nth Node From End of List'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        right = head
        left = head

        for i in range(n):
            right = right.next
        # Special cases, removing the head node
        if not right:
            return head.next
        
        while right.next:
            right = right.next
            left = left.next
        
        #skip the nth element
        left.next = left.next.next
        return head
    
'''erase(self, index) is index-based and removes a node at a given position from the start.
remove_nth_last_node(head, n) is position-from-end-based and removes a node relative to the end of the list.
'''

'''203 Remove Linked List Elements'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head and head.val == val:
            head = head.next
        cur_node = head
        while cur_node and cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return head
        