def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps were made in this pass
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap arr[j] and arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in this pass, the list is already sorted
        if not swapped:
            break
        
        # Print the current state of the list after this pass
        print(f"Pass {i+1}: {arr}")

# Input list
input_list = [64, 34, 25, 12, 22, 11, 90]

# Print the initial list
print("Initial list: ", input_list)

# Call the bubble_sort function
bubble_sort(input_list)

# Print the sorted list
print("Sorted list: ", input_list)
