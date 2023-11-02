def sortedLinearSearch(theValues, item):
    n = len(theValues)
    for i in range(n):  # If the target is in the ith element, return True
        if theValues[i] == item:
            return True
        elif theValues[i] > item:  # Because it's sorted.
            return False
    return False


def findSmallest(theValues):
    n = len(theValues)
    smallest = theValues[0]
    for i in range(1, n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    return smallest

