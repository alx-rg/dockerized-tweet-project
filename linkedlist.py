#!python


from lib2to3.pgen2.token import EQUAL
from platform import node
from typing import ItemsView
from venv import create
from zipapp import create_archive


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None
        
    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count
  
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        created_node = Node(item)
        # check to see if we're at the head/begin of the linked list
        if self.tail is not None:
            self.tail.next = created_node
        else:
            self.head = created_node
        self.tail = created_node
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        # TODO: Else append node after tail


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        created_node = Node(item)
        # TODO: Prepend node before head, if it exists
        # check to see if linked list exists 
        if self.head is None:
            # if there is no list, add node to head and tail
            self.head = created_node
            self.tail = created_node
        else:
            # linked list exists! only add to head
            # Choose the next item
            created_node.next = self.head 
            # This item becomes the new head of linked list
            self.head = created_node

        

    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # current node is the head of the linked list
        present_node = self.head
        while present_node != None: #while there are items in the linked list
            if item == present_node.data:
                return True
            else:
                present_node = present_node.next
        return False

        # TODO: Loop through all nodes to find item, if present return True otherwise False
    
    def find_if_matches(self, matching_function):
        """Return an item from this linked list if it is present."""
        node = self.head
        while node is not None:
            if matching_function(node.data): 
                return node.data
            node = node.next
        return None 
    
    def replace(self, current_item, new_item):
        """Replace an item in the linked list with a new item"""
        present_node = self.head
        # Start with Head as the current node (begin @ the start/start at the beginning)
        while present_node is not None:
            if present_node.data == current_item:
                present_node.data = new_item
                return
            else:
                present_node = present_node.next



    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        
        if self.head is None:
            raise ValueError('Item not found: {}'.format(item))

        elif self.head is not None: 
        #Note: If there is a head
            previous_node = None
            present_node = self.head
            # Start head @ node you are at presently (begin @ the start/start at the beginning)
            created_node = self.head.next
            
            if present_node.data is not item: 
            # IF the item is not the same as the present node
                while present_node.next is not None and present_node.data is not item:
                    previous_node = present_node
                    present_node = present_node.next
                    created_node = present_node.next
                
                if present_node is self.tail and present_node.data is not item: 
                #IF the present node is the TAIL and the data in the node is not the item
                    raise ValueError('Item not found: {}'.format(item)) 
                    #Return a message that the item could not be found
                
                elif created_node is None: 
                #Else if there are no new nodes
                    previous_node.next = None
                    # the previous node becomes the tail
                    self.tail = previous_node
                    if previous_node is self.head:
                        self.tail = self.head
                
                else: previous_node.next = created_node 
            
            elif created_node is None: 
                self.head = None 
                self.tail = None 
            
            else:
                self.head = created_node
            
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

if __name__ == "__main__":
    my_ll = LinkedList(["A", "B", "C"])
    print(my_ll)

    


