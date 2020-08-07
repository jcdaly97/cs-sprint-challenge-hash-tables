# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for f in files:
        s = f.rsplit('/',1)[1]
        if s not in cache:
            cache[s] = []
            cache[s].append(f)
        else:
            cache[s].append(f)
    for q in queries:
        if q in cache:
            for path in cache[q]:
                result.append(path)
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
