"""

705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

"""

class MyHashSet(object):

    def __init__(self):
        self.set = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.set:
            self.set.append(key)
        self.set.sort()    
        
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.set:
            self.set.pop(self.set.index(key))
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.set:
            return True
        return False
