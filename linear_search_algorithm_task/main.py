# Function to perform linear search
def linear_search(input_list, target):
    index = -1
    for i in range(len(input_list)):
        if input_list[i] == target:
            index = i
            break
    if index == -1:
        return -1
    else:
        return index


# Test the function
input_number = [int(n) for n in input("Enter a list of integers numbers by spaces: ").split()]
target_element = int(input("Enter the number you want to find: "))
result = linear_search(input_number, target_element)
if result != -1:
    print(f"The target element {target_element} is at index {result}.")
else:
    print(f"The target element {target_element} was not found in the list.")
