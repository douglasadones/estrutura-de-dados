def linearSearch(theValues, target):  # Operator 'in''s logic
    n = len(theValues)
    for i in range(n):  # If the target is in the ith element, return True
        if theValues[i] == target:
            return True
    return False


