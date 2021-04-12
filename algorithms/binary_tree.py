from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
            else:
                raise ValueError(f"A node with value {new_node.value} already exists.")

    # in order print the elements in strict asc order
    def print_inorder(self, current_node: Node):
        if current_node.left:
            self.print_inorder(current_node.left)
        print(current_node.value)
        if current_node.right:
            self.print_inorder(current_node.right)

    def _print_pretty(self, node: Node, indent: str):
        print(f"{indent}{node.value}")
        if node.left:
            self._print_pretty(node.left, f"{indent}l    ")
        if node.right:
            self._print_pretty(node.right, f"{indent}r    ")

    def print_pretty(self):
        indent = ""
        self._print_pretty(self.head, indent)

    def _find_parent(self, current_node: Node, value) -> Node:
        if current_node is None:
            return None
        if (current_node.left and current_node.left.value == value) or \
           (current_node.right and current_node.right.value == value):
            return current_node
        elif value > current_node.value:
            return self._find_parent(current_node.right, value)
        elif value < current_node.value:
            return self._find_parent(current_node.left, value)

    def find_parent(self, value):
        if self.head.value == value:
            return None
        return self._find_parent(self.head, value)

    def _find(self, node: Node, value: int) -> Node:
        if node is None:
            return None
        elif value == node.value:
            return node
        elif value > node.value:
            return self._find(node.right, value)
        elif value < node.value:
            return self._find(node.left, value)

    def find(self, value: int) -> Node:
        if self.head is None:
            return None
        elif self.head.value == value:
            return self.head
        elif value > self.head.value:
            return self._find(self.head.right, value)
        elif value < self.head.value:
            return self._find(self.head.left, value)

    @staticmethod
    def find_max(node: Node) -> Node:
        while node.right:
            node = node.right
        return node

    def delete(self, value: int):
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)

        if to_delete.left and to_delete.right:  # two children
            max_node = BinaryTree.find_max(to_delete.left)
            max_node_parent = self.find_parent(max_node.value)
            if max_node_parent != to_delete:
                max_node_parent.right = max_node.left
                max_node.left = to_delete.left
            max_node.right = to_delete.right
            if to_delete_parent is None:  # Root
                self.head = max_node
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = max_node
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = max_node
        elif to_delete.left or to_delete.right:  # one child
            if to_delete == self.head:
                self.head = to_delete.left or to_delete.right
            elif to_delete == to_delete_parent.left:
                to_delete_parent.left = to_delete.left or to_delete.right
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.left or to_delete.right
        else:  # No children
            if to_delete == self.head:
                self.head = None
            elif to_delete == to_delete_parent.left:
                to_delete_parent.left = None
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = None
