class Treenode:
    def __init__(self,data):
        self.data=data
        self.childern=[]
        self.parent=None
    def add_childs(self,child):
        child.parent=self
        self.childern.append(child)
def build_tree():
    root=Treenode("sujan")
    laptop=Treenode("acer")
    root.add_childs(laptop)
    return root
if __name__=='__main__':
    root=build_tree()
    print(root)
