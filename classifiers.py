from analyzers import (is_reflexive,
                       is_transitive,
                       is_symmetric,
                       is_antisymmetric)




def is_equivalence(A, R):
    """
    Checks if a relation R on set A is an equivalence relation.

    An equivalence relation is one that is:
    1. Reflexive: Every element is related to itself.
    2. Symmetric: If (a, b) ∈ R, then (b, a) ∈ R.
    3. Transitive: If (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R.

    Parameters:
    A (set): The set of elements.
    R (set): The relation as a set of tuples.

    Returns:
    bool: True if R is an equivalence relation, False otherwise.
    
    """
    
    if is_reflexive(A, R) and is_transitive(R) and is_symmetric(R):
        return True
    else:
        return False




def is_partial_order(A, R):
    """
    Checks if a relation R on set A is a partial order.

    A partial order is a relation that is:
    1. Reflexive: Every element is related to itself.
    2. Antisymmetric: If (a, b) ∈ R and (b, a) ∈ R, then a = b.
    3. Transitive: If (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R.

    Parameters:
    A (set): The set of elements.
    R (set): The relation as a set of tuples.

    Returns:
    bool: True if R is a partial order, False otherwise.
    
    """
    
    if is_reflexive(A, R) and is_transitive(R) and is_antisymmetric(R):
        return True
    else:
        return False
