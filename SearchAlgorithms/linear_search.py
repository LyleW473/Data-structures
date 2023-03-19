def linear_search(list_to_search, value_to_find):
    
    if len(list_to_search) == 0:
        print("This list is empty.")
        return None
    
    for index in range(len(list_to_search)):

        if list_to_search[index] == value_to_find:
            print(f"{value_to_find} found at index {index}")
            return index
    
    print(f"{value_to_find} not found in the list.")
    return None

def linear_search_v2(list_to_search, value_to_find):

    return [index for index in range(len(list_to_search)) if list_to_search[index] == value_to_find]

print(linear_search([50, 25, 12, 3, 0], 1002))
print(linear_search_v2([50, 25, 12, 3, 0, 50], 50))
print(linear_search_v2([50, 25, 12, 3, 0, 50], -1))