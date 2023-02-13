class LargestSubarrayWith0Sum:
    # opening the file
    def readFromFile(self,path):
        return open(path,'r')
    
    def getInputValues(self,file):
        #read the data from the file
        input_list=file.read().split('\n')
        if(len(input_list)==0):
            raise Exception("Empty Input")
        # to store the input from the file
        input_values=[]
        input_values.append(int(input_list[0]))
        temp=[]
        if(len(input_list)==1):
            raise Exception("Invalid Input")
        temp=input_list[1].split(' ')
        #type casting the second row of input to int
        for i in range(len(temp)):
            temp[i]=int(temp[i])
        input_values.append(temp)
        return input_values
    
    def largestSubarryWith0Sum(self,input_values):
        if(input_values[0]==1 and input_values[1][0]!=0):
            return -1
        elif(input_values[0]==1 and input_values[1][0]==0):
            return [0,0]