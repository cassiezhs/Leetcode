'''202. Happy Number'''
def is_happy_number(n):
    def sum_of_squared_digits(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(n,10)
            total_sum += digit ** 2
        return total_sum
    
    slow_ptr = n
    fast_ptr = sum_of_squared_digits(n)

    while fast_ptr != 1 and slow_ptr != fast_ptr:
        slow_ptr = sum_of_squared_digits(slow_ptr)
        fast_ptr = sum_of_squared_digits(sum_of_squared_digits(fast_ptr))

    if fast_ptr == 1:
        return True
    return False

'''Linked list cycle'''
def detect_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

'''middle of the linked list'''
def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow