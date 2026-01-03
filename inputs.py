def get_set():
    """
    Prompts the user to enter elements of a set and returns a Python set.

    Steps:
    1. Ask the user to input elements separated by spaces.
    2. Split the input string into individual elements.
    3. Convert the list of elements into a set to remove duplicates.
    
    Returns:
    set: A set containing the unique elements entered by the user.
    
    """
    
    elements = input("Enter Set Elements (Space Separated): ").strip()
    elements = elements.split()
    A = set(elements)
    return A




def get_relation(A):
    """
    Prompts the user to enter relation pairs for a given set A and returns
    the relation as a set of tuples.

    Steps:
    1. Print the Cartesian product of the set A (using print_cartesian_product function).
    2. Continuously prompt the user to enter relation pairs until valid input is given.
    3. Validate each pair:
       - Must start with '(' and end with ')'
       - Must contain exactly two elements separated by a comma
       - Each element must belong to the set A
    4. Add valid pairs to the relation set and return it.

    Parameters:
    A (set): The set for which the relation is defined.

    Returns:
    set: A set of tuples representing the relation.
    
    """
    
    print_cartesian_product(A)
    while True:
        pairs = input("Enter Relation Pairs like (1,2) (2,3): ").strip()
        pairs = pairs.split()
        R = set()
        ready = True
        
        for pair in pairs:
            if not (pair.startswith("(") and pair.endswith(")")):
                print("Invalid Input\nPlease Follow the Instructed Format")
                ready = False
                break

            pair = pair[1:-1] # brackets remove
            pair = pair.split(",")

            if (len(pair) != 2):
                print("Invalid Input\nMore than 2 pair elements not allowed")
                ready = False
                break

            a = pair[0].strip()
            b = pair[1].strip()
            if not (a in A and b in A):
                print(f"Pair not Found in the Cartesian Product: ({a}, {b})")
                ready = False
                break
            R.add((a, b))

        if ready:
            return R



def print_cartesian_product(A):
    """
    Prints the Cartesian product of a given set A.

    The Cartesian product of a set A with itself consists of all possible
    ordered pairs (a, b) where a and b are elements of A.

    Parameters:
    A (set): The input set whose Cartesian product is to be printed.
    
    """
    
    print("Cartesian Product (A x A):")
    for e1 in A:
        print()
        for e2 in A:
            print(f"({e1}, {e2})", end=" ")
    print("\n")
