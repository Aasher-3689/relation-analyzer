# We need to append parent folder also to get
# function from modules placed there
import os, sys
current_folder = os.path.dirname(__file__)
parent_folder = os.path.dirname(current_folder)
sys.path.append(parent_folder)

# importing relevant functions from analyzers module
from classifiers import (is_equivalence,
                         is_partial_order)





def test_equivalence():
    print("\nTesting Equivalence Relation")
    print("-" * 35)

    A = {1, 2, 3}
    R = {(1, 1), (2, 2), (3, 3), (2, 3), (3, 2)}
    expected = True
    actual = is_equivalence(A, R)
    print(f"{'Test # 1':<20} {'Passed' if expected == actual else 'Failed'}") 

    A = {1, 2, 3}
    R = {(1, 1), (2, 2), (2, 3)}
    expected = False
    actual = is_equivalence(A, R)
    print(f"{'Test # 2':<20} {'Passed' if expected == actual else 'Failed'}") 
    print("-" * 35)




def test_partial_order():
    print("\nTesting Partial Order Relation")
    print("-" * 35)

    A = {1, 2, 3}
    R = {(1, 1), (2, 2), (3, 3), (2, 1)}
    expected = True
    actual = is_partial_order(A, R)
    print(f"{'Test # 1':<20} {'Passed' if expected == actual else 'Failed'}") 

    A = {1, 2, 3}
    R = {(1, 1), (2, 2), (2, 3)}
    expected = False
    actual = is_partial_order(A, R)
    print(f"{'Test # 2':<20} {'Passed' if expected == actual else 'Failed'}") 
    print("-" * 35)




if __name__ == "__main__":
    test_equivalence()
    test_partial_order()
