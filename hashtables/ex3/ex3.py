cache = {}

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    # Your code here
    for x in arrays[0]:
        cache[x] = 1
    i = 1
    while i < len(arrays) -1:
            for y in arrays[i]:
                if y in cache and cache[y] == i:
                    cache[y] += 1
            i += 1
    for z in arrays[len(arrays)-1]:
                if z in cache and cache[z] == i:
                    result.append(z)
    return result

    """
    for x in arrays[0]:
        cache[x] = 1
    for y in arrays[1]:
        if y in cache:
            cache[y] = True
    for z in arrays[2]:
        if z in cache and cache[z] == True:
            result.append(z)
    """


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
