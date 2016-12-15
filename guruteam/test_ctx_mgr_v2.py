class AutoSave:
    def __init__(self,data,file_n):
        self.data = data #make data available to self
        self.file_n = file_n
        
    def __enter__(self):
        self.fo = open(self.file_n, 'w') # will find autosave as in column 1
        return self.file_n
      
    def __exit__(self,exc_type,exc_obj,exc_tb):  #exc_tb - useful to extract info from
        print(exc_type)
        import json
        json.dump(self.data, self.fo)
        self.fo.close()
        

#========================================


d = {}

with AutoSave(d, 'data2.json'):
    d['uk'] = 44
    #10 / 0 # exit will be called here; otherwise at end
    d['irl'] = 3534567
    d['usa'] = 123456
    d['de'] = 496789


##
##
##
###dump needs a file; dump3 stringoutput
###print(json.dumps(d))
##
##fo.close()
