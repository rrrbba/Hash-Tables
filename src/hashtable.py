import hashlib
#  '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    #underscore means don't use method outside of the class
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # return hashlib.sha256(key.encode())
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        #calculate the index with key via the hash

        #make index
        index = self._hash_mod(key)
        #make node that has instance of the index with the self.storage
        node = self.storage[index]

        #if there is nothing at that index in storage
        if not node:
            #set it to the key value pair that's inputed
            self.storage[index] = LinkedPair(key, value)
            return

        #while node is true
        while node:
            #if node.key = a key in list
            if node.key == key:
                #set the value of the node in list to node.value
                node.value = value
                return
            #if there is a node.next
            elif node.next:
                #set node to the next node
                node = node.next
            else:
                #then add it to the end of list
                node.next = LinkedPair(key, value)
                return

        #-----> class solution
        # #find index 
        # index = self._hash_mod(key)
        
        # #check for error
        # if self.storage[index] is not None:
        #     print("Error: key in use")
        # else:
        #     #put it there -> index becomes value
        #     self.storage[index] = value
            


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        #index
        index = self._hash_mod(key)
        #node 
        node = self.storage[index]
        #use for iteration
        prev_node = None

        while node:
            #if there is a key in the list matching the one inputed
            if node.key == key:
                #set the node to none if no previous node
                self.storage[index] = None
                return

            else:
                #move onto to next node and set previous to node
                node, prev_node = node.next, node
        
        else:
            #if there is no key found from the one inputed
            print("Key not found")

        #---> Class solution
        # #index
        # index = self._hash_mod(key)
        
        # #if there is something at the index
        # if self.storage[index] is not None:
        #     # make it none
        #     self.storage[index] = None
        # else:
        #     #key doesn't exist
        #     print("Key not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        #index
        index = self._hash_mod(key)
        #node
        node = self.storage[index]

        #while node is true
        while node:
            #if there is a node with key the of the inputed node key
            if node.key == key:
                #return that node's value
                return node.value
            #else keep going
            else:
                node = node.next
        #if that node doesn't exist, return none
        return None

        #---->class solution
        # index = self._hash_mod(key)

        # return self.storage[index]

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #resize when capacity is hit, make it two times bigger

        #store reference to old storage
        old_storage = self.storage
        #double the capacity by multip self.capacity by 2
        self.capacity = self.capacity * 2
        # reassign self.storage to [None] * capacity
        self.storage = [None] * self.capacity
        # loop over old storage and call insert on ith key and value 
        for node in old_storage:
            #while node is true
            while node:
                #insert key value pair
                self.insert(node.key, node.value)
                #move on
                node = node.next

        #[3,4,_,_] -> [3, 4, None, None]
        


        #------>class solution
        # old_storage = self.storage

        # self.capacity = self.capacity * 2
        # self.storage = [None] * self.capacity

        # for bucket_item in old_storage:
        #     self.insert(bucket_item)






if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print("hello")
    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

#day 1
#create hashtable w/out ll chaining, print errors for collisions

#day 2 
#handle the collisions

#Monday MVP: hashtable.py without LL chaining (print an error on collision)
#key, value is immutable
#Tuesday MVP: Handle the collision with Linked List chaining
#replace errors with ll chaining



# class LinkNode:
#     def __init__(self, key, value):
#         #key
#         #value
#         #next
#         self.key = key
#         self.value = value
#         self.next = None

# class HashTable:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = [None] * capacity #->if it was 2 [None, None]
#         #allocates the memory we need for the hashtable
#         #new Array(2) => [<empty>,<empty>] this is an ex in JS

#     def _hash(self, key):
#         return hash(key) #only returns numbers

#     def _hash_mod(self, key): #references hash function
#         return self._hash(key) % self.capacity #hashes the key and get the modulo of the

#     def insert(self, key, value):
#         #index = self._hashmod(key), calls with key that's input
#         index = self._hash_mod(key) 
#         #curr_pair = self.storage[index]
#         current_pair = self.storage[index]

#         prev_pair = None 
#         '''
#         Capacity == 2
#         Storage = [LL node, None]
#         '''
#         #299-308 logic stays the same for remove
#         #while there is a current pair and the key isn't equal to the input key
#         while current_pair is not None and current_pair.key != key:
#             #move prev reference which is none to current
#             prev_pair = current_pair
#             current_pair = current_pair.next

#         #so there are two keys with the same value
#         if current_pair is not None:
#             #overwrite
#             current_pair.value = value
#         else:
#             #create new LL pait
#             new_pair = LinkNode(key,value)
#             #set new pair next to be head, 
#             new_pair.next = self.storage[index]
#             #reset head to be new pair
#             self.storage[index] = new_pair
            
#         #CASE 1 - none index
#         #if self.storage at index is none
#         #create new LL node with key and value assigning that index

#         #CASE 2 - LL node at index, one value
#         #store ref to curr node
#         #make new LL node
#         #overwrite head of LL by changing new LL node next to curr node

#         #CASE 3 - LL node with more than one value