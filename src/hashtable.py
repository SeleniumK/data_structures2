class HashTable(object):
    """Create a hash table."""

    def __init__(self, buckets=1024):
        """Initialize instance of hash table."""
        self.buckets = buckets
        self.init_table()

    def init_table(self):
        """Initialize table in hashtable."""
        self._table = []
        for x in range(self.buckets):
            self._table.append([])

    def get(self, key):
        bn = self._hash(key) % self.buckets
        for k, value in self._table[bn]:
            if k == key:
                return value

    def set(self, key, value):
        bn = self._hash(key) % self.buckets
        self._table[bn].append((key, value))

    def _hash(self, key):
        hsh = 0
        for char in key:
            hsh += ord(char)
        return hsh
