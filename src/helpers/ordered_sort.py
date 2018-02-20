
def orderedInsert(alist, target):

    i = len(alist)
    while ((i > 0) and (target < alist[i-1].id_zipcode_year)):
        i = i - 1

    #alist[i:i] = target
    return i
