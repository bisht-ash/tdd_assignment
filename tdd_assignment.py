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
            return 0
        elif(input_values[0]==1 and input_values[1][0]==0):
            return 1
        else:
            map={}
            max_len = 0
            curr_sum = 0
            # Traverse through the given array
            for i in range(len(input_values[1])):
                # Add the current element to the sum
                curr_sum += input_values[1][i]
                if input_values[1][i] == 0 and max_len == 0:
                    max_len = 1
                if curr_sum == 0:
                    max_len = i + 1

                if curr_sum in map:
                    max_len = max(max_len, i - map[curr_sum])
                else:
                    # else put this sum in dictionary
                    map[curr_sum] = i

            return max_len
    
    def solve(self):
        path='input.txt'
        file =self.readFromFile(path)
        input_values=self.getInputValues(file)  
        ans=self.largestSubarryWith0Sum(input_values)
        print(ans);     
       
def main():
    obj=LargestSubarrayWith0Sum()
    obj.solve()
         
            

if __name__=='__main__' :
    main()         