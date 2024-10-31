#!/usr/bin/env python3
""" class LRUCache that inherits from BaseCaching and is a caching system."""
BaseCaching = __import__('base_caching').BaseCaching

class Node:
    """Doubly Linked List Node"""
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    """Doubly Linked List"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
  
    def append(self, key, value):
        """Append a node to the front of the list"""
        new_node = Node(key, value)

        if self.head is None:  # If list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  # Update the head to the new node
        
        self.size += 1
    def remove_tail(self):
        """Remove the last node from the list"""
        node_key = self.tail.key

        if self.tail is None:  # If list is empty
            pass
        
        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None 
        
        self.size -= 1
        return node_key


    def remove(self, key):
        """Remove a node by its key"""
        if self.head is None:
            print('No node')
            return 
        
        current = self.head
        while current:
            if current.key == key:
                if current == self.head:  # Node is head
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:  # Node is tail
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:  # Node is in the middle
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
                break  # Stop after removing the node
            current = current.next

    def traverse_fw(self):
        """Traverse the list forward and print nodes"""
        if self.head is None:
            print('No node')
            return 
        current = self.head
        while current:
            print(f'{current.key}:{current.value}')
            current = current.next
 
    def length(self):
        """"""
        return self.size

class LRUCache(BaseCaching):
    """"""
    def __init__(self):
        super().__init__()
        self.ll = DLL()   # Double linked list instance 
                     # use this to perform operation with the dll
    def put(self, key, item):
        if key is None or item is None:
            return
        # key exist in cache no issue with cache size since its replacement
        if key in self.cache_data:
            self.ll.remove(key)      # Remove the key and item from its current position
            self.ll.append(key, item)   # Bring the item to MRU side in the dll
        else:
            self.ll.append(key, item)  # append the key and value at the front
            if self.ll.length() > self.MAX_ITEMS: # check the cache size and remove 1 if neccessary
                node_key = self.ll.remove_tail()
                self.cache_data.pop(node_key)
                print('DISCARD: {}'.format(node_key))
        self.cache_data[key] = item # update the value in the dict

             
    def get(self, key):
        """"""
        if key is None or key not in self.cache_data:
            return None
        
        item = self.cache_data.get(key)
        self.ll.remove(key)
        self.ll.append(key, item)

        return item
