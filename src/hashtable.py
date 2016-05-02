class HashTable(object):
    """Create a hash table."""

    def __init__(self, buckets=1024):
        """Initialize instance of hash table."""
        self.buckets = buckets
        self._table = []
        for x in range(self.buckets):
            self._table.append([])

    def get(self, key):
        """Get a value given a key.

        Raises TypeError if a non string value.
        """
        bn = self._hash(key) % self.buckets
        for k, value in self._table[bn]:
            if k == key:
                return value

    def set(self, key, value):
        """Set a value given a key and value.

        Raises TypeError if a non string value.
        """
        bn = self._hash(key) % self.buckets
        self._table[bn].append((key, value))

    def _hash(self, key):
        """Hash additively."""
        hsh = 0
        for char in key:
            hsh += ord(char)
        return hsh
