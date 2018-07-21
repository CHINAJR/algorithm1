
class LinearMap:
    def __init__(self):
        self.items = []

    def add(self,k,v):
        self.items.append((k,v))

    def get(self,k):
        for key,val in self.items:
            if key == k:
                return val
        raise KeyError 

class BetterMap:
    def __init__(self,n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self,k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self,k,v):
        m = self.find_map(k)
        m.add(k,v)

    def get(self,k):
        m = self.find_map(k)
        return m.get(k)

class HashMap:
    def __init__(self):
        self.maps = BetterMap(2)#除留余数法
        #为了等概率随机返回key 根据random  产生随机数 原表是a 1  存另一张查找表 1 a
        self.num = 0 

    def add(self,k,v):
        if self.num == len(self.maps.maps):
            self.resize()
        self.maps.add(k,v)
        self.num += 1

    def get(self,k):
        return self.maps.get(k)

    def resize(self):
        new_map = BetterMap(self.num*2)
        for i in self.maps.maps:
            for k,v in i.items:
                new_map.add(k,v)
        self.maps = new_map

if __name__ == '__main__':
    import string
    m = HashMap()
    s = string.ascii_lowercase
    for k,v in enumerate(s):
        m.add(k,v)
    for k in range(len(s)):
        print(k,m.get(k))

