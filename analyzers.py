def is_reflexive(A, R):
    """
    Checks if a relation R on set A is reflexive.

    A relation R is reflexive if every element in A is related to itself,
    i.e., (a, a) ∈ R for all a ∈ A.

    Parameters:
    A (set): The set of elements.
    R (set): The relation as a set of tuples.

    Returns:
    bool: True if R is reflexive, False otherwise.
    
    """
    
    result = True
    for a in A:
        if (a, a) not in R:
            result = False
            break
    return result




def is_irreflexive(A, R):
    """
    Checks if a relation R on set A is irreflexive.

    A relation R is irreflexive if no element in A is related to itself,
    i.e., (a, a) ∉ R for all a ∈ A.

    Parameters:
    A (set): The set of elements.
    R (set): The relation as a set of tuples.

    Returns:
    bool: True if R is irreflexive, False otherwise.
    
    """
    
    result = True
    for a in A:
        if (a, a) in R:
            result = False
            break
    return result

def is_symmetric(R):
    """
    Checks if a relation R is symmetric.

    A relation R is symmetric if for every (a, b) ∈ R, (b, a) ∈ R.

    Parameters:
    R (set): The relation as a set of tuples.

    Returns:
    bool: True if R is symmetric, False otherwise.
    
    """
    
    result = True
    for (a, b) in R:
        if (b, a) not in R:
            result = False
            break
    return result

def is_asymmetric(R):
    """
    Checks if a relation R is asymmetric.

    A relation R is asymmetric if for every (a, b) ∈ R, (b, a) ∉ R.

    Parameters:
    R (set): The relation as a set of tuples.

    Returns:
    bool: True if R is asymmetric, False otherwise.
    
    """
    
    result = True
    for (a, b) in R:
        if (b, a) in R:
            result = False
            break
    return result

def is_antisymmetric(R):
    """
    Checks if a relation R is antisymmetric.

    A relation R is antisymmetric if for all (a, b) ∈ R, 
    (b, a) ∉ R if a not equal to b.

    Parameters:
    R (set): The relation as a set of tuples.

    Returns:
    bool: True if R is antisymmetric, False otherwise.
    
    """
    
    result = True
    for (a, b) in R:
        if a != b and (b, a) in R:
            result = False
            break
    return result

def is_transitive(R):
    """
    Checks if a relation R is transitive.

    A relation R is transitive if for all (a, b) and (b, c) in R,
    (a, c) is also in R.

    Parameters:
    R (set): The relation as a set of tuples.

    Returns:
    bool: True if R is transitive, False otherwise.
    
    """
    
    result = True
    for (a, b) in R:
        for (c, d) in R:
            if b == c and (a, d) not in R:
                result = False
                break
    return result
