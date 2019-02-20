def unique_in_order(iterable):
    result = [] # empty list for the result
    last = None #

    for item in iterable: # going over the array
        if item == last: # if the value is equal to the previous term
            continue    #we do nothing
        else:
            #if current item is different then previous one
            result.append(item) # add the item into results
            last = item #and set previous item to current one

    return result

num = [1,2,2,3,3]
print(unique_in_order(num)) # should be [1,2,3]
aab = 'AAAABBCCDABBB'
print(unique_in_order(aab)) # should be ['A', 'B', 'C', 'D', 'A', 'B']
ab = 'ABCcAD'
print(unique_in_order(ab)) # should be ['A', 'B', 'C', 'c', 'A', 'D']
