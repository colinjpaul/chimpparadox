#import json


class AutoSave:
    file_n = 'data.json'
    def __init__(self,data):
        self.data = data #make data available to self
            
    def __enter__(self):

        self.fo = open(AutoSave.file_n, 'w') # will find autosave as in column 1
        return AutoSave.file_n
        
    def __exit__(self,x,y,z):
        import json
        json.dump(self.data, self.fo)
        self.fo.close()
        



#========================================


d = {}

with AutoSave(d) as file_name:
    d['uk'] = 44
    d['irl'] = 353
    d['usa'] = 1
    d['de'] = 49

print(file_name)

##
##
##
###dump needs a file; dump3 stringoutput
###print(json.dumps(d))
##
##fo.close()
