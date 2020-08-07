def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

# For an input list of integers, we wish to know which positive numbers
# have corresponding negative numbers in the list.

# Return value can be in any order.
# Solve this problem with a hash table.

    # Empty list
    result = []
    # Empty hash table
    cache = {}

    for num in a:
        # Add int to ht
        cache[num] = 1
    for num in a:
        # If int * -1 is in the ht and if positive int exists, add int to the result array
        if (num*-1) in cache and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
