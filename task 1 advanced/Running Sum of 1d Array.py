class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #create a new array called "running_sum_arr"
        running_sum_arr = []
        #create a new variable called "current_sum" and initialize the variable to 0
        current_sum = 0
        #Iterate through the array
        for num in nums:
            #add value to "current_sum"
            current_sum+=num
            #insert "current_sum" to "running_sum_arr"
            running_sum_arr.append(current_sum)
        #return "running_sum_arr"
        return running_sum_arr