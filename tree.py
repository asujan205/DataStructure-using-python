class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    def add_childs(self,child):
        child.parent=self
        self.children.append(child)
def build_tree():
    root=Treenode("sujan")
    laptop1=Treenode("acer")
    laptop2=Treenode("lenevo")
    root.add_childs(laptop1)
    root.add_childs(laptop2)
    laptop2.add_childs(Treenode("kiran"))
    root.print_tree()
if __name__=='__main__':
    root=build_tree()
    print(root)
