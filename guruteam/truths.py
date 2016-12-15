class Truths:
    def __init__(self):
        self.truths = [1, 7, 11, 42]

    def __len__(self):
        return len(self.truths)

    def __getitem__(self,index):
        print('getitem')
        return self.truths[index]

    def __setitem__(self,index,value):
        print('setitem')
        self.truths[index] = value


obj = Truths()
print (len(obj))

print(obj[ -2: ])


for truth in obj:
    print(truth)

'''
print (list(obj))
print (tuple(obj))


obj[0] = 100
#this does the same as above
obj.__class__.__setitem__(obj, 0, 100)

print(list(obj))
'''


    



