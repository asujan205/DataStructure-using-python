from distutils.command.build import build


class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data ==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
    
        else:
            if self.right:
                self.left.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
if __name__ == '__main__':
    numbers=[1,2,3,4,34,78,32,90,17,30]
    numbers_tree=build_tree(numbers)

