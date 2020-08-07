def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i,v in enumerate(weights):
        cache[v] = i
    for index, item in enumerate(weights):
        v = limit - item
        if v in cache:
            if item == v:
                return [cache[v], index]
            elif cache[v] > cache[item]:
                return [cache[v], cache[item]]
            else:
                return [cache[item], cache[v]]
    return None
    
    
    
weights_1 = [9]
answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

print(answer_1)
print(answer_2)
print(answer_3)
print(answer_4)