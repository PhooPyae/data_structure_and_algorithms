def quicksort(nums):
  '''
  Sort item in nums in ascending order
  INPUT:
  nums: [5,1,1,2,0,0]
  OUTPUT: 
  Sorted list:[0,0,1,1,2,5]
  
  '''
  if len(nums)<2:
    return nums
  else:
    pivot=nums[0]
    less= [i for i in nums[1:] if i<=pivot]
    greater= [i for i in nums[1:] if i>pivot]
    return quicksort(less)+[pivot]+quicksort(greater)
if __name__ == '__main__':
  nums=[5,1,1,2,0,0]
  print("Sorted list", quicksort(nums))
    
