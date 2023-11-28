def Bubble_sort(nums):
    n=len(nums)
    
    for i in range(0,n):
        
        for j in range(0,n-i-1):
            
            if(nums[j] > nums[j+1]):
                nums[j],nums[j+1] = nums[j+1],nums[j]
    
if __name__ =="__main__":
    nums = [6,1,4,9,2]
    Bubble_sort(nums)
    print(nums)
