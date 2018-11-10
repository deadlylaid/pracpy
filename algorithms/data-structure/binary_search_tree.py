class BinarySearchTree:

    class _Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right =None

        def __str__(self):
            return "Node 반환<<" + "Key : " + str(self.key) + ",  Value : " + str(self.value) + ">>"

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = self._Node(key, value)
        if not self.root:
            self.root = new_node
        else:
            location = self.root
            while location != None:
                if new_node.key > location.key:
                    if location.right == None:
                        location.right = new_node
                        break;
                    else:
                        location = location.right
                elif new_node.key < location.key:
                    if location.left == None:
                        location.left = new_node
                        break;
                    else:
                        location = location.left

    def delete(self, key):
        location = self.root
        while True:
            if location.key == key:
                break
            elif location.key > key:
                location = location.right
            elif location.key < key:
                location = location.left
            elif location.key == None:
                raise ValueError("해당 키를 갖는 노드는 존재하지 않습니다.")

        change_node = location
        if change_node.left == None and change_node.right == None:
            """
            자식 노드가 없으면 해당 노드만 삭제하고 끝남
            """

        while change_node.left != None and change_node.right != None:
            if change_node.left == None:
                change_node = change_node.right
            else:
                change_node = change_node.left

from IPython import embed; embed()
