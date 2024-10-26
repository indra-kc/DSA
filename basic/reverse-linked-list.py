class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node
    return prev

# Helper to print linked list
def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# Example usage
head = ListNode(1, ListNode(2, ListNode(3)))  # Creates 1 -> 2 -> 3 -> None
print("Original:")
print_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed:")
print_list(reversed_head)

# output
# Original:
# 1 -> 2 -> 3 -> None
# Reversed:
# 3 -> 2 -> 1 -> None

