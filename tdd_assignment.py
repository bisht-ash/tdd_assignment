class LargestSubarrayWith0Sum:
    def readFromFile(self,path):
        return open(path,'r')
    def getInputValues(self,file):
        input_list=file.read().split('\n')
        input_values=[]
        input_values.append(int(input_list[0]))
        temp=input_list[1].split(' ')
        for i in range(len(temp)):
            temp[i]=int(temp[i])
        input_values.append(temp)
        return input_values
