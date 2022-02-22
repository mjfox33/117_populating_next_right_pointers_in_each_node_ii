from code_117_populating_next_right_pointers_in_each_node_ii import Solution
from code_117_populating_next_right_pointers_in_each_node_ii import Node

def test_example_1():
    s = Solution()
    n7 = Node(7)
    n3 = Node(3,right=n7)
    n5 = Node(5)
    n4 = Node(4)
    n2 = Node(2,n4,n5)
    n1 = Node(1,n2,n3)
    
    r5 = Node(5, next=n7)
    r4 = Node(4, next=n5)
    r2 = Node(2,r4,r5,next=n3)
    r1 = Node(1,r2,n3)
    assert s.connect(n1) == r1