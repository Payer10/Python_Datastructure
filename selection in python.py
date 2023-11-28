def selection_sort(nums):

    for i in range(len(nums)-1):
        min_index = i

        for j in range(i+1,len(nums)):
            if(nums[j] < nums[min_index]):
                min_index = j

        if(min_index != i):
            nums[i],nums[min_index] = nums[min_index],nums[i]

nums = list(map(int,input().split()))
selection_sort(nums)
print(nums)




