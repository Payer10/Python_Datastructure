def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        item=nums[i]
        j=i-1
        while j>=0 and nums[j] > item:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = item

if __name__ == "__main__":
    nums = [6,1,4,9,2]
    insertion_sort(nums)
    print(nums)
