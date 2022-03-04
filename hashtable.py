#!python

from multiprocessing.sharedctypes import Value
from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        - 0(n) 
        - """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) Why and under what conditions?"""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) since it loops through every item in each of the buckets"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) Why and under what conditions?"""
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        bucket_index = self._bucket_index(key)
        key_bucket = self.buckets[bucket_index]
        contains_key = key_bucket.find_if_matches(lambda item: item[0] == key)
        return contains_key is not None
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket_index = self._bucket_index(key)
        key_bucket = self.buckets[bucket_index]
        value_from_key = key_bucket.find_if_matches(lambda item: item[0] == key)
        if value_from_key is not None:
            return value_from_key[1]
        else:
            raise KeyError(f'The Key Was Not Found: {key}')
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        bucket_index = self._bucket_index(key)
        key_bucket = self.buckets[bucket_index]
        value_from_key = key_bucket.find_if_matches(lambda item: item[0] == key)
        if value_from_key is not None:
            key_bucket.delete(value_from_key)
        key_bucket.append((key, value))
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        bucket_index = self._bucket_index(key)
        key_bucket = self.buckets[bucket_index]
        value_from_key = key_bucket.find_if_matches(lambda item: item[0] == key)
        if value_from_key is not None:
            key_bucket.delete(value_from_key)
        else:
            raise KeyError(f'The Key Was Not Found: {key}')
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

if __name__ == '__main__':
    ht = HashTable()
    print('hash table: {}'.format(ht))
