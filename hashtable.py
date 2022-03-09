# Hashtable class/driver
#Zion Choi :: 3/7/2022

class hashtable:
    #constructor => sets capacity and creates buckets
    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [[] for i in range(capacity)]

    #checks if bucket is empty, and appends key/value pair if empty
    def put(self, key, value):
        index = self.hashCode(key)
        if self.buckets[index] == []:
            self.buckets[index].extend([key, value])
            return True
        return False

    #returns value using key hashing method
    def get(self, key):
        index = self.hashCode(key)
        try:
            return self.buckets[index][1]
        except:
            return None

    #converts key to string, then to ASCII characters, finally uses bit AND function
    def hashCode(self, key):
        hash_key = ''
        for char in str(key):
            hash_key+=str(ord(char))
        return int(hash_key) & (self.capacity-1)

#TEST METHOD
print("==== Creating Hashtable ====")
test = hashtable(16)
print("==== Hashtable Finalized ====")
print("\n==== Testing Put Method ====")
print("Adding key/value pair (1,2): " + str(test.put(1, 2)))
print("Adding key/value pair (1,5): " + str(test.put(1, 5)))
print("Adding key/value pair ('hi',198): " + str(test.put('hi', 198)))
print("\n==== Testing Get Method ====")
print("Retrieving from key = 1: " + str(test.get(1)))
print("Retrieving from key = 1: " + str(test.get('hi')))