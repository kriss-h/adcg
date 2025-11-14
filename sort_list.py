
def bubble_sort(my_list):
    """
    Sorts a list in ascending order using the bubble sort algorithm.
    The function modifies the original list and does not return anything.
    """
    # Loop through the list until no more swaps are needed
    while True:
        # Initialize a flag to track whether a swap occurred
        swap_occurred = False
        # Iterate over the list and compare adjacent elements
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                # Swap the elements if they are in the wrong order
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                # Set the swap occurred flag to True
                swap_occurred = True
        # If no swaps were made, then the list is sorted and we can break out of the loop
        if not swap_occurred:
            break
    return None
