class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        print(value)

def reverse_linked_list(head):
    prev = None
    current = head
    print(current)

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        

    return prev

# Helper function to print the linked list

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original linked list:")
    print_linked_list(head)

    reversed_head = reverse_linked_list(head)

    print("Reversed linked list:")
    print_linked_list(reversed_head)
