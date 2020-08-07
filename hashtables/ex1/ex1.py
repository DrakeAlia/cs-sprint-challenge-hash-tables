def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

# Given a package with a weight limit `limit` and a list `weights` of item
# weights, implement a function `get_indices_of_item_weights` that finds
# two items whose sum of weights equals the weight limit `limit`. Your
# function will return a tuple of integers that has the following form:

# ```
# (zero, one)
# ```

# where each element represents the item weights of the two packages.
# _**The higher valued index should be placed in the `zeroth` index and
# the smaller index should be placed in the `first` index.**_ If such a
# pair doesn’t exist for the given inputs, your function should return
# `None`.
# Your solution should run in linear time.

    cache = {}

    # Fail if input array is shorter than 2 entries (test case 1)
    if length <= 1:
        print("Error: List too short.")
        return None

    for i in range(length):
        current = weights[i]
         # Check if the current weight is in the cache
         # The matching/previously inserted weight index = the value in the cache
        if current in cache:
            # prev weight index = value, so get index of prev
            previous = cache[current]
            # print(cache)
            if i > previous:
                return (i, previous)
            else:
                return (previous, i)
        # Hash table/cache key is the smaller weight needed to reach limit
        # That value is the current weight's index
        cache[limit - weights[i]] = i

    return None

weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights, 5, 21))
