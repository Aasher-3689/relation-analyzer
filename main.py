# Import all required functions from separate modules
# analyzers   : contains relation property checking functions
# classifiers : contains relation classification functions
# inputs      : contains user input related functions
from analyzers import *
from classifiers import *
from inputs import *




def main():
    """
    Main function of the Relation Analyzer program.

    This function:
    1. Takes a set and a relation from the user.
    2. Displays all relation properties in a tabular format.
    3. Classifies the relation as Equivalence or Partial Order.
    
    """
    
    A = get_set()
    R = get_relation(A)

    # ------------------ Relation Properties Table ------------------
    print("\nRelation Analysis:")
    print("-" * 45)
    print(f"{'Property':<25} {'Result':<15}")
    print("-" * 45)

    # Check and display basic relation properties
    print(f"{'Reflexive':<25} {'Yes' if is_reflexive(A, R) else 'Not'}")
    print(f"{'Irreflexive':<25} {'Yes' if is_irreflexive(A, R) else 'Not'}")
    print(f"{'Symmetric':<25} {'Yes' if is_symmetric(R) else 'Not'}")
    print(f"{'Asymmetric':<25} {'Yes' if is_asymmetric(R) else 'Not'}")
    print(f"{'Antisymmetric':<25} {'Yes' if is_antisymmetric(R) else 'Not'}")
    print(f"{'Transitive':<25} {'Yes' if is_transitive(R) else 'Not'}")
    print("-" * 45)

    # ------------------ Relation Classification Table ------------------
    print("\nRelation Classification:")
    print("-" * 45)
    print(f"{'Property':<25} {'Result':<15}")
    print("-" * 45)

    # Check and display relation classification
    print(f"{'Equivalence':<25} {'Yes' if is_equivalence(A, R) else 'Not'}")
    print(f"{'Partial Order':<25} {'Yes' if is_partial_order(A, R) else 'Not'}")
    print("-" * 45)

    


# Program execution starts from here
# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
