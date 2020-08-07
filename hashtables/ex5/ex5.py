def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

# Given a list of full paths to files, and a list of filenames to query,
# report all the full paths that match that filename.

    # Empty list
    result = []
    # Empty ht for pathsa
    cache = {}

    # Split the paths on '/', to get the key as the filename
    for x in files:
        # Use rsplit instead to begin splitting from right end of the string
        key = x.rsplit('/', 1)[1] 
        value = x

        # Create new entry in ht if needed
        if key not in cache:
            cache[key] = []
        # Add current path to cache 
        cache[key].append(x)

    # For each filename in queries, check to see if it is a key in the ht
    for y in queries:
        if y in cache:
            # If the file is found, add to the path
            result += cache[y]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
