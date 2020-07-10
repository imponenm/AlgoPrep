'''
706. Design HashMap
Rating: Easy

Design a HashMap without using any built-in hash table libraries. To be specific, your design should include these functions:
put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Notes:
The reason it's called a hashmap is because you hash the key and use the hash as an index to access in an array.
The index contains a bucket of all the values at the hash in the form of a list of tuples [(key, value),].

Runtimes for each method are O(N/K), where N is the total number of hashes, and K is the number of predefined buckets.
Space complexity is O(M+K), where M is number of unique values in the hashmap, and K is number of predefined buckets
'''


class Bucket:

    def __init__(self):
        self.hashes = []

    def put(self, key, value):
        for i, pair in enumerate(self.hashes):
            if pair[0] == key:
                self.hashes[i] = (key, value)
                break
        else:
            self.hashes.append((key, value))

    def get(self, key):
        for (k, v) in self.hashes:
            if k == key:
                return v
        return -1

    def remove(self, key):
        for i, pair in enumerate(self.hashes):
            if pair[0] == key:
                del self.hashes[i]
                break


class MyHashMap:

    # My initial thought is to use a list of tuples that contain a key and value
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_val = 2017
        self.hash_table = [Bucket() for b in range(self.hash_val)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h = key % self.hash_val
        self.hash_table[h].put(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h = key % self.hash_val
        return self.hash_table[h].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h = key % self.hash_val
        self.hash_table[h].remove(key)

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 2)
obj.put(2, 3)
print(obj.get(1))
obj.remove(1)
print(obj.get(1))
