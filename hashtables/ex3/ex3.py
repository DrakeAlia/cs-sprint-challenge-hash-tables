def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

# Find the intersection between multiple lists of integers.
# Do not use numpy or sets to solve this; use `dict` or hashtables, please

    # Empty list
    result = []
    # Empty dict
    cache = {}

    # Subarray is a single list containing the integers within the list
    for subarray in arrays:
        for num in subarray:
            if num not in cache:
                # num = key, with 0 value
                cache[num] = 1 
            else:
                # Append num to the intersection list
                result.append(num)
                # Creates a new list, removing any potential duplicates from the list
    result = list(dict.fromkeys(result)) 
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
