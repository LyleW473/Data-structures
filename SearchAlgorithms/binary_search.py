def binary_search(target, nums_list, return_invalid_target_index = False):

    # Returns index of where the target is or where the target should be placed if it is not in the list

    left, right = 0, len(nums_list) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums_list[mid] == target:
            return mid
        
        elif target > nums_list[mid]:
            left = mid + 1

        elif target < nums_list[mid]:
            right = mid - 1

    # Note: Left is always returned because if the target is not in the list:
        # If the target is smaller than all values, then left = 0, right = -1
        # If the target is larger than all values, then left = len(nums_list) (i.e. placed at the end of the list) right = len(nums) - 1

    # Returns -1 if user wants to know where the target should be placed inside the list
    return left if return_invalid_target_index == True else -1

print(binary_search(target= -1, nums_list= [1,3,4,5], return_invalid_target_index = True))
print(binary_search(target= 2, nums_list= [1,3,4,5], return_invalid_target_index = True))
print(binary_search(target= 9, nums_list= [1,3,4,5,8], return_invalid_target_index = True))
print(binary_search(target= 7, nums_list= [1,3,4,5,8], return_invalid_target_index = True))
print(binary_search(target= -1, nums_list= [1,3,4,5,8]))
print(binary_search(target= 9, nums_list= [1,3,4,5,8]))
print(binary_search(target= 7, nums_list= [1,3,4,5,8]))