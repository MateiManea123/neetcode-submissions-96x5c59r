import random

class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.alist = []

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.hmap[val] = len(self.alist)
        self.alist.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False

        lastelem = self.alist[-1]
        self.alist[self.hmap[val]] = lastelem
        self.hmap[lastelem] = self.hmap[val]
        del self.hmap[val]
        self.alist.pop()
        return True
    def getRandom(self) -> int:
        randindex = random.randint(0,len(self.alist)-1)
        return self.alist[randindex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()