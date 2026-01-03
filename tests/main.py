# Import all test functions from individual test modules
# Each module contains test cases for a specific relation property
from classification import *
from reflexive import *
from symmetric import *
from transitive import *




def main():
    """
    Main test runner function.

    This function executes all test cases related to:
    - Reflexive and Irreflexive relations
    - Symmetric, Asymmetric, and Antisymmetric relations
    - Equivalence relations
    - Partial order relations

    Each test function prints PASS or FAIL based on the expected output.
    
    """
    
    test_reflexive()
    test_irreflexive()
    test_symmetric()
    test_asymmetric()
    test_antisymmetric()
    test_equivalence()
    test_partial_order()


    

# Entry point of the test runner
# Ensures that tests are executed only when this file is run directly
if __name__ == "__main__":
    main()
