#!/usr/bin/env python3
""" class MRUCache that inherits from BaseCaching and is a caching system."""
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

    def remove_head(self):
        """Remove the last node from the list"""
        node_key = self.head.key

        if self.head is None:  # If list is empty
            pass
        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
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

    def length(self):
        """Return lenght of a list"""
        return self.size


class MRUCache(BaseCaching):
    """MRU CACHE ALGORITHM """
    def __init__(self):
        """Initializer"""
        super().__init__()
        self.ll = DLL()   # Double linked list instance

    def put(self, key, item):
        """put an item in to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.ll.remove(key)      # Remove the key
        else:
            if self.ll.length() >= self.MAX_ITEMS:
                node_key = self.ll.remove_head()
                self.ll.append(key, item)  # append the key
                self.cache_data.pop(node_key)
                print('DISCARD: {}'.format(node_key))
        self.ll.append(key, item)   # Bring the item to MRU side in the dll
        self.cache_data[key] = item  # update the value in the dict

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data.get(key)
        self.ll.remove(key)
        self.ll.append(key, item)
        return item
