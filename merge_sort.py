def merge(list_one: list[int], list_two: list[int]):
    len_one, len_two = len(list_one) -1  , len(list_two)-1
    j, i = 0, 0
    res = []
    # when both pointers go out of range
    while i <= len_one or j <= len_two:
        # if j is out of range or i element is less than j
        if j > len_two or i <= len_one and list_one[i] <= list_two[j]:
            res.append(list_one[i])
            i += 1
        else:
            res.append(list_two[j])
            j += 1
    return res

def merge_sort(lst: list[int]):
    """ Recursive merge sort
    Time: O(n log(n)) all scenarios
    Space: O(n) all scenarios
    """
    lo, hi = 0, len(lst)
    if len(lst) <= 1:
        return lst
    mid = (lo+hi)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)
    


