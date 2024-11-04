import random
class RandomizedSet:

    def __init__(self):
        self.vals = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.vals[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False
        idx = self.vals[val]
        self.lst[idx] = self.lst[-1]
        self.vals[self.lst[-1]] = idx
        self.lst.pop()
        del self.vals[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.lst)