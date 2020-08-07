cache = {}

def intersection(arrays, i = 0):
    """
    YOUR CODE HERE
    """
    result = []
    # Your code here
    if i == 0:
        for x in arrays[0]:
            cache[x] = 1
    elif i < len(arrays) - 1:
        for y in arrays[i]:
            if y in cache and cache[y] == i:
                cache[y] += 1
        return intersection(arrays, i+1)
    else:
        for z in arrays[i]:
            if z in cache and cache[z] == i-1:
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
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
