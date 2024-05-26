from functools import reduce

def find_largest(arr):
    print(arr)
    return reduce(max, arr)

input_array = [1, 2, 3, 4, 5]
result = find_largest(input_array)
print("Largest element in the array:", result)
