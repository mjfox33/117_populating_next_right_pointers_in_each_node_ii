from dataclasses import dataclass

# Definition for a Node.
@dataclass
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        sentinel = Node(0,next=root)

        while sentinel.next:
            tail = sentinel
            next_node = sentinel.next
            sentinel.next = None
            while next_node:
                if next_node.left:
                    tail.next = next_node.left
                    tail = tail.next
                
                if next_node.right:
                    tail.next = next_node.right
                    tail = tail.next
                next_node = next_node.next
        return root
