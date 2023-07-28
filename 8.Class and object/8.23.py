import weakref

class Node:
    def __init__(self,value):
        self.value = value
        self._parent = None
        self.children = []
    def __repr__(self):
        return 'Node({!r:})'.format(self.value)
    '''свойство которое управляет родителем с помощью слабой ссылки'''
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent
    @parent.setter
    def parent(self,node):
        self._parent = weakref.ref(node)
    def add_child(self,child):
        self.children.append(child)
        child.parent = self
root = Node('parent')
c1 = Node('child')
root.add_child(c1)
c1.parent
del root
c1.parent

# Класс, созданный, чтобы проиллюстрировать то, что будет при удалении
class Data:
    def __del__(self):
        print('Data.__del__')
# Класс-узел, в котором есть цикл
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []
    def add_children(self,child):
        self.children.append(child)
        child.parent = self
a = Data()
del a
a = Node()
del a
a = Node()
a.add_children(Node())
del a