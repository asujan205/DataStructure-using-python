
class HashTable:
    def __init__(self):
        
        self.MAX = 100
        self.arr = [ None for i in range(self.MAX)]

    def get_hash_key(self,key):
            h=0 
        for char in key:
        h+=ord(char)
         return h %self.MAX
    def __setitem__(self,key,value):
        h= self.get_hash_key(key)
        self.arr[h]=value
    def __getitem__(key,value):
        h =get_hash_key(key)
        return self.arr[h]
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None  
    

