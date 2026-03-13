class HashMap:
    def __init__(self, n=8):
        self.size = n
        self.count = 0
        self.map = [[] for _ in range(n)]

    def _hash(self, key):
        return hash(key) % self.size #Converts the key into an integer whaterver the type

    def hash_add(self, key, value):
        index = self._hash(key)

        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)
                return

        self.map[index].append((key, value))
        self.count += 1

        if self.count / self.size > 0.7: #If load factor is over 70% we resize
            self.resize()

    def resize(self):
        old_map = self.map
        self.size *= 2 #Double the size of the map
        self.map = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_map:
            for k, v in bucket:
                self.hash_add(k, v)

    def list_all(self):
        for bucket in self.map:
            for k, v in bucket:
                print(k, v)
