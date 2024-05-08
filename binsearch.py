def binsearch(item, lst:list):
    lst.sort()
    fIndex = 0
    lIndex = len(lst)-1
    while True:
        midIndex = round((lIndex + fIndex)/2)
        if (item > lst[-1]) or (item < lst[0]):
            return False
        elif item == lst[midIndex]:
            return midIndex
        
        elif item > lst[midIndex]:
            fIndex = midIndex
            continue
        elif item < lst[midIndex]:
            lIndex = midIndex
            continue
