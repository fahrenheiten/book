import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self,initial = None):
        self._items = sorted(initial) if initial is None else []
    # Требуемые методы последовательности
    def __getitem__(self, item):
        return self._items[item]
    def __len__(self):
        return len(self._items)
    # Метод для добавления элемента в правильное место
    def add(self,item):
        bisect.insort(self._items,item)
items = SortedItems([10,15,52,84])
print(list(items))