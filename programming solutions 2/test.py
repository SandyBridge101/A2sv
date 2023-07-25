turns=[]
def flip(arr, idx):
    # Flips the subarray from the beginning up to idx (inclusive)
    turns.append(len(arr[0:idx])+1)
    return arr[:idx+1][::-1] + arr[idx+1:]

def find_max_index(arr, n):
    # Finds the index of the maximum element in the first n elements of the array
    max_index = 0
    for i in range(n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        # Find the index of the maximum element in the first 'curr_size' elements
        max_index = find_max_index(arr, curr_size)

        # If the maximum element is not at the end, flip the array twice to move it to the correct position
        if max_index != curr_size - 1:
            # Flip the subarray to bring the maximum element to the beginning
            arr = flip(arr, max_index)

            # Flip the whole array to move the maximum element to the correct position
            arr = flip(arr, curr_size - 1)

    return arr

# Example usage:
arr = [3,2,4,1]
sorted_arr = pancake_sort(arr)
print("Sorted Array:", sorted_arr,turns)
