from node import Node
from binary_tree import BinaryTree

print("Test Node")
left = Node(5)
head = Node(9)
right = Node(13)

head.left = left
head.right = right

print(head)
print(head.left)
print(head.right)

print("Test Tree")
tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(13))

# print(tree.head)
# print(tree.head.left)
# print(tree.head.right)

tree.print_inorder(tree.head)
tree.print_pretty()
print(tree.find_parent(5))
print(tree.find_parent(9))
print(tree.find_parent(13))
print(tree.find_parent(20))

print(tree.find_max(tree.head))

print("TEST TREE")
tree2 = BinaryTree(Node(60))
nodes = [50, 30, 90, 70, 80, 75, 120, 110]
for value in nodes:
    tree2.add(Node(value))

tree2.delete(60)
tree2.print_pretty()
tree2.print_inorder(tree2.head)