# linear Search is not that efficient it has O(n) no of iterations which example is given below

from operator import index


def trsnactions(parameter):
    return 

# Binary Search --> Works on the concept of sorted list

def binary_search(nums_list,num_to_find):
    left_index = 0
    right_index = len(nums_list)-1
    middle_index = 0

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2

        middle_number = nums_list[middle_index]

        if middle_number == num_to_find:
            return middle_index
        
        if middle_number < num_to_find:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return -1


# Binary Search using recursive function
def binary_search_using_recursive(nums_list,num_to_find,left_index,right_index):
    if right_index < left_index:
        return -1
    
    middle_index = (left_index+right_index)//2
    
    
    if middle_index >= len(nums_list) or middle_index <0:
        return -1 

    middle_numer = nums_list[middle_index]
    if num_to_find == middle_numer:
        return middle_index

    if middle_numer < num_to_find:
        left_index = middle_index + 1
    else:
        right_index = middle_index - 1
    
    

    return binary_search_using_recursive(nums_list,num_to_find,left_index,right_index)

if __name__ == '__main__':
    nums_list = [12,15,17,19,19,19,21,24,45,67]
    # print(nums_list[:-1],"slicing")
    nums_to_find = 19

    index = binary_search(nums_list,nums_to_find)
    print(index)



# abc 
