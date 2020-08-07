
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    for i in a:
        neg = i*-1
        if neg in cache:
            result.append(abs(i))
        else:
            cache[i] = True
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


"""
i = 0
    while i < len(a):
        print(i)
        if a[i] > 0:
            cache[a[i]] = True
            a.pop(i)
        else:
            i+=1
    for j in a:
        if j < 0:
            v = j*-1
            if v in cache:
                result.append(v)
"""