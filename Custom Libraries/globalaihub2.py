class globalaihub2(list):

    def __init__(self, *numbers):

        for i in numbers:
            if not isinstance(i, (int, float)):
                raise TypeError(f"Expecting an int/float.")
            else:
                print(i)


        super().__init__(numbers)
        #self._data = list(numbers)
        #self.length = len(numbers)


    def mean(self):
        try:
            # 4.0 == 4 True

            if (sum(self) / len(self)) == int((sum(self) / len(self))):
                return int(sum(self) / len(self))
            else:
                return (sum(self) / len(self))

        except:
            return "Error"

    @property
    def length(self):
        try:
            finalLen = 0

            for i in self:
                finalLen += 1

            return finalLen

        except:
            return "Error"

    def return_inp(self):
        try:
            return self

        except:
            return "Error"

# customClass = globalaihub2(0,1,2,3,4,5,6,7)
# print(customClass.length)
# print(customClass.return_inp())
