import types
class Node:
    pass
class NodeVisitor:
    def visit(self,node):
        stack = [ node ]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last,types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last,Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result
    def _visit(self,node):
        methname = 'visit_' +type(node).__name__
        meth = getattr(self,methname,None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)
    def generic_visit(self,node):
        raise RuntimeError('No {} method'.format(('visit_' + type(node).__name__)))
'''Если вы попробуете поработать с этим классом, то обнаружите, что он попрежнему работает с существующим кодом, который мог использовать рекурсию.
На самом деле вы можете использовать его в качестве прямой замены реализации
класса­посетителя в предыдущем рецепте. Рассмотрим такой код с деревьями выражений:'''

class UnaryOperator(Node):
    def __init__(self,operand):
        self.operand = operand
class BinaryOperator(Node):
    def __init__(self, left,rigth):
        self.left = left
        self.right = rigth
class Add(BinaryOperator):
    pass
class Sub(BinaryOperator):
    pass
class Mul(BinaryOperator):
    pass
class Div(BinaryOperator):
    pass
class Negate(BinaryOperator):
    pass
class Number(Node):
    def __init__(self,value):
        self.value = value
#Пример класса-посетителя, выполняющего выражения
class Evaluator(NodeVisitor):
    def visit_Number(self,node):
        return node.value
    def visit_Add(self, node):
        yield (yield node.left)+(yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left)-(yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left)*(yield node.right)

    def visit_Div(self, node):
        yield (yield node.left)/(yield node.right)

    def visit_Negate(self, node):
        return -node.operand
if __name__ == '__main__':
    # 1 + 2*(3-4) / 5
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(3), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)
    # Выполнить это
    e = Evaluator()
    print(e.visit(t4))
    a = Number(0)
    for n in range(1,10000000):
        a = Add(a,Number(n))
    e = Evaluator()
    print(e.visit(a))