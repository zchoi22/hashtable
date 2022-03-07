# hashtable
epic hashtable for epic class

Challenge One:
x % n where n is a large prime number is a better hash function than x % n where n is a large number with several factors. For example, if n = 12 (a number with many factors), there will be collisions at 2, 3, 4, and 6 when the data exhibits patterns; because the keys may share a common factor with the bucket number, both the quotient and the remainder can be written as a multiple of this common factor. By using a prime number, collisions are decreased when patterns arise in keys.

Challenge Two:
Though 599 is a prime number, summing char values may not be the best hash function for strings. There is a possibility that two (or more) distinct keys sum to the same amount, and modding it with a prime number (regardless of its size) will not produce a unique index.

Challenge Three:
Java's index-generating function is as follows: index = hashcode(key) & (n-1), where n is the bucket size. Java utilizes the bitwise AND function.

In terms of the hashcode() method, it looks like Java checks the keys type, and converts the key into a string of bytes based on its unique hashing algorithm.
