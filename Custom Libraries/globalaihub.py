class globalaihub:
    
    def __init__(self, *numbers):
        self._data = list(numbers)
        #self.length = len(numbers)
        
    def mean(self):
        try:
            # 4.0 == 4 True
            
            if (sum(self._data) / len(self._data)) == int((sum(self._data) / len(self._data))):
                return int(sum(self._data) / len(self._data))
            else:
                return (sum(self._data) / len(self._data))
        
        except:
            return "Error"
            
    @property
    def length(self):
        try:
            finalLen = 0
        
            for i in self._data:
                finalLen += 1
                
            return finalLen
        
        except:
            return "Error"
            
    def return_inp(self):
        try:
            return self._data
        
        except:
            return "Error"
        
# customClass = globalaihub(0,1,2,3,4,5,6,7)
# print(customClass.length)
# print(customClass.return_inp())

# #print(customClass.custom_length())
