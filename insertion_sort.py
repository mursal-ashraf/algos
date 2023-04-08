def insertion_sort(arr):
    """ In place insertion sort
    Space: O(1) all case
    Time:
        Best: O(n) where arr is already sorted
        Avg and Worst: O(n^2)
    """
    for i in range(1, len(arr)):
        # invariant = arr[0: i] is sorted
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key



banks_become_more_digital = True

if(banks_become_more_digital):
    more_software_jobs_in_banks = True