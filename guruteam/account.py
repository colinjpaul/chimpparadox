class SecurityViolation(Exception):
    pass

#remenber you have to have an initiator anytime the calling function has a class
#good practice to do it anyway

class Account:
    num_acs = 0
    
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.trans = []
        Account.num_acs += 1

    #note no self here
    #when python executes this too lines it puts in memory
    #what represents this code.  doesn't execute the code   
    @staticmethod     
    def get_num_acs():
        return Account.num_acs
    
    #this does the same as @staticmethod above
    #get_num_acs = staticmethod(ge_num_acs)

    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        self.trans.append(amount)
        self.balance += amount

    def withdraw(self,amount):
        self.trans.append(-amount)
        self.balance -= amount

    def __len__(self):        return len(self.trans)

    # called explicitly through [] 
    def __getitem__(self,index):
        return self.trans[index]

#in python can directly access the index of a class
# print (b1[0])

#java would first require you call a function
#print (b1.get_item(0))

    def __setitem__(self,index,value):
        raise SecurityViolation('trying to change transactions')









