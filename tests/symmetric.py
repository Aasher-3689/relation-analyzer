# We need to append parent folder also to get
# function from modules placed there
import os, sys
current_folder = os.path.dirname(__file__)
parent_folder = os.path.dirname(current_folder)
sys.path.append(parent_folder)

# importing relevant functions from analyzers module
from analyzers import (is_symmetric,
                       is_asymmetric,
                       is_antisymmetric)





def test_symmetric():
    print("\nTesting Symmetric Relation")
    print("-" * 35)

    A = {1, 2, 3}
    R = {(1, 1), (2, 2), (3, 2), (2, 3)}
    expected = True
    actual = is_symmetric(R)
    print(f"{'Test # 1':<20} {'Passed' if expected == actual else 'Failed'}") 

    A = {1, 2, 3}
    R = {(1, 1), (2, 2), (2, 3)}
    expected = False
    actual = is_symmetric(R)
    print(f"{'Test # 2':<20} {'Passed' if expected == actual else 'Failed'}") 
    print("-" * 35)




def test_asymmetric():
    print("\nTesting Asymmetric Relation")
    print("-" * 35)

    A = {1, 2, 3}
    R = {(1, 2), (2, 3), (3, 1)}
    expected = True
    actual = is_asymmetric(R)
    print(f"{'Test # 1':<20} {'Passed' if expected == actual else 'Failed'}") 

    A = {1, 2, 3}
    R = {(1, 1), (3, 2), (2, 3)}
    expected = False
    actual = is_asymmetric(R)
    print(f"{'Test # 2':<20} {'Passed' if expected == actual else 'Failed'}") 
    print("-" * 35)




def test_antisymmetric():
    print("\nTesting Antisymmetric Relation")
    print("-" * 35)

    A = {1, 2, 3}
    R = {(1, 1), (2, 3), (3, 1)}
    expected = True
    actual = is_antisymmetric(R)
    print(f"{'Test # 1':<20} {'Passed' if expected == actual else 'Failed'}") 

    A = {1, 2, 3}
    R = {(1, 1), (3, 2), (2, 3)}
    expected = False
    actual = is_antisymmetric(R)
    print(f"{'Test # 2':<20} {'Passed' if expected == actual else 'Failed'}") 
    print("-" * 35)




if __name__ == "__main__":
    test_symmetric()
    test_asymmetric()
    test_antisymmetric()
