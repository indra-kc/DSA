class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_lists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

# Helper to print linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage
l1 = ListNode(1, ListNode(3, ListNode(5)))  # 1 -> 3 -> 5 -> None
l2 = ListNode(2, ListNode(4, ListNode(6)))  # 2 -> 4 -> 6 -> None

print("Merged List:")
merged_head = merge_lists(l1, l2)
print_list(merged_head)

# output
'''
Merged List:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
'''
