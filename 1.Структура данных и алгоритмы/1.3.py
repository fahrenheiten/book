from collections import deque
def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
        # Пример использования
# if __name__ == '__main__':
#     with open('somefaile.txt') as f:
#         for line, prevlines in search(f,'python',5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line,end='')
#             print('-'*20)
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
print(d)
d.append(4)
print(d)
d.pop()
print(d)
d.popleft()
print(d)