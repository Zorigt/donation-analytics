def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
    if alist[midpoint].id_zipcode_year == item:
        return alist[midpoint]
    else:
        if item < alist[midpoint].id_zipcode_year:
            return binarySearch(alist[:midpoint],item)
        else:
            return binarySearch(alist[midpoint+1:],item)