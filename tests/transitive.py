# We need to append parent folder also to get
# function from modules placed there
import os, sys
current_folder = os.path.dirname(__file__)
parent_folder = os.path.dirname(current_folder)
sys.path.append(parent_folder)

# importing relevant functions from analyzers module
from analyzers import is_transitive





def test_transitive():
    print("\nTesting Transitive Relation")
    print("-" * 35)

    A = {1, 2, 3}
    R = {(1, 1), (1, 2), (2, 3), (1, 3)}
    expected = True
    actual = is_transitive(R)
    print(f"{'Test # 1':<20} {'Passed' if expected == actual else 'Failed'}") 

    A = {1, 2, 3}
    R = {(1, 1), (2, 1), (1, 3), (2, 2)}
    expected = False
    actual = is_transitive(R)
    print(f"{'Test # 2':<20} {'Passed' if expected == actual else 'Failed'}") 
    print("-" * 35)




if __name__ == "__main__":
    test_transitive()
