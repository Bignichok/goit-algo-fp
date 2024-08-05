class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print('None')

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.print_list()
linkedList.head = reverse_list(linkedList.head)
linkedList.print_list()

def get_middle(head):
    if not head:
        return head
    
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    
    if left.value <= right.value:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)
    return result

def merge_sort(head):
    if not head or not head.next:
        return head
    
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = merge(left, right)
    return sorted_list



linkedList.head = merge_sort(linkedList.head)
linkedList.print_list()

def merge_two_sorted_lists(list_1, list_2):
    dummy = Node()
    tail = dummy

    while list_1 and list_2:
        if list_1.value <= list_2.value:
            tail.next = list_1
            list_1 = list_1.next
        else:
            tail.next = list_2
            list_2 = list_2.next
        tail = tail.next

    if list_1:
        tail.next = list_1
    if list_2:
        tail.next = list_2

    return dummy.next

ll1 = LinkedList()
ll1.append(1)
ll1.append(22)
ll1.append(44)

ll2 = LinkedList()
ll2.append(43)
ll2.append(44)
ll2.append(654)

ll1.print_list()
ll2.print_list()

merged_head = merge_two_sorted_lists(ll1.head, ll2.head)
merged_list = LinkedList()
merged_list.head = merged_head
merged_list.print_list()
