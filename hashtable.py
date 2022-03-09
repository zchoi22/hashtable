# Hashtable class/driver
#Zion Choi :: 3/7/2022
from random import randint
import matplotlib.pyplot as plt
import math

class hashtable:
    #constructor => sets capacity and creates buckets
    def __init__(self, capacity, ec):
        self.capacity = capacity +1
        self.buckets = [[] for i in range(self.capacity)]
        self.ec = ec

    #checks if bucket is empty, and appends key/value pair if empty
    def put(self, key, value):
        index = self.hashCode(key)
        if self.buckets[index] == []:
            self.buckets[index].extend([key, value, 1])
            return True
        self.buckets[index][2]+=1
        return False

    #returns value using key hashing method
    def get(self, key):
        index = self.hashCode(key)
        try:
            return self.buckets[index][1]
        except:
            return None

    #using matplotlib, shows the number of keys that led to a specific index
    #from the hashing method
    def get_distribution(self):
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        buckets = [i for i in range(self.capacity-1)]
        for bucket in self.buckets:
            if bucket == []:
                bucket.extend([0,0,0])
        num_hashed = [self.buckets[i][2] for i in range(self.capacity-1)]
        ax.bar(buckets, num_hashed)
        print(self.get_collisions())
        plt.show()

    #returns number of collisions
    def get_collisions(self):
        collisions = 0
        for bucket in self.buckets:
            if bucket[2] > 1:
                collisions+=(bucket[2]-1)
        return collisions

    #converts key to string, then to ASCII characters, finally uses BIT and
    #added setting for second hashcode for extra credit
    def hashCode(self, key):
        hash_key = ''
        for char in str(key):
            hash_key+=str(ord(char))
        if self.ec:
            return int(hash_key) & (self.capacity-1)
        else:
            return int(hash_key) % (self.capacity - 1)

if __name__ == '__main__':
    #TEST METHOD
    print("==== Creating Hashtable ====")
    test = hashtable(16, False)
    print("==== Hashtable Finalized ====")
    print("\n==== Testing Put Method ====")
    print("Adding key/value pair (1,2): " + str(test.put(1, 2)))
    print("Adding key/value pair (1,5): " + str(test.put(1, 5)))
    print("Adding key/value pair ('hi',198): " + str(test.put('hi', 198)))
    print("\n==== Testing Get Method ====")
    print("Retrieving from key = 1: " + str(test.get(1)))
    print("Retrieving from key = 1: " + str(test.get('hi')))

    #EXTRA CREDIT
    print("\n\n==== Extra Credit =====")
    print("==== Creating Hashtables ====")
    ec = hashtable(31873, False)
    ec_newHash = hashtable(21873, True)

    #shows the distribution plotted as well as number of collisions
    count = 0
    index = 0
    percentages = [10, 25, 50, 75, 90, 95, 100]
    for i in range(1000):
        count+=1
        temp = randint(0,100000)
        ec.put(temp, 1)
        ec_newHash.put(temp, 1)
        percent_done = math.floor(count/1000*100)
        if math.floor(count/1000*100) in percentages:
            try:
                print("===== " + str(percentages[index]) + "% Done =====")
                index+=1
            except:
                pass

    print("\n===== Fetching Distributions =====")
    ec.get_distribution()
    ec_newHash.get_distribution()