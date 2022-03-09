# Hashtable class/driver

class hashtable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [[] for i in range(capacity)]

    def put(self, key, value):
        index = self.hashCode(key)
        if self.buckets[index] == []:
            self.buckets[index].extend([key, value])
            return True
        return False

    def get(self, key):
        index = self.hashCode(key)
        try:
            return self.buckets[index][1]
        except:
            return None

    def hashCode(self, key):
        hash_key = ''
        for char in str(key):
            hash_key+=str(ord(char))
        return int(hash_key) & (self.capacity-1)

test = hashtable(16)
print(test.put(1, 2))
print(test.get(1))
