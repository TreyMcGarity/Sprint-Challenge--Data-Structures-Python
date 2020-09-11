class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node = None, prev = None): 
        #not using node parameter
        # set temp var to last added node which will be head
        current = self.head 
        # as long as the temp var has a value (stop at null pointer)
        while current is not None: 
            # store next node
            next_node = current.get_next()
            # set current's next to previous
            current.set_next(prev) 
            # move prev and current one step toward end of list
            prev = current 
            current = next_node
        # set new head to previous node
        self.head = prev

    #for visual in file run
    def print_list(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.get_next()

sll = LinkedList()
sll.add_to_head(1)
sll.add_to_head(2)
sll.add_to_head(3)
sll.print_list()
print("-")
sll.reverse_list()
sll.print_list()