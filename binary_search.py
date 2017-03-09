class List(object):
    pass

class BinarySearch:
    def __init__(self,a, b):
        self.a = a
        self.b = b
        self.length = len(self.a)
        self.range = a[len(a)-1] - a[0]
        
        
    def search(self,item):
        count_dictionary = {}
        count = 1

        first = self.a[0]        
        last = self.a[len(self.a)-1]
        found = False

        for i in range(1,len(self.a)):
            mid = (first + last)//2
            count = count + 1
            if self.a[i] == item:
                found = True
                count_dictionary["count"] = count
                count_dictionary["index"] = i
        return (count_dictionary)
bin = BinarySearch([2,4,6,8,10],3)
print(bin.search(7))

#  binaryEx = BinarySearch([2,4,6,8,10],2)
# --> [2,4,6,8,10]











