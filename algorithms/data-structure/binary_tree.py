class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def print_tree(node):
    """
    구현해볼것
    """


def preorder(node):
    """
    왼쪽 - 중간 - 오른쪽
    """

    print(node.value, end=" ")
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def inorder(node):
    """
    중간 - 왼쪽 - 오른쪽
    """
    if node.left:
        inorder(node.left)
    print(node.value, end=" ")
    if node.right:
        inorder(node.right)

def postorder(node):
    """
    왼쪽 - 오른쪽 - 중간
    """
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.value, end=" ")
