# record = ('Dave','dave@example.com','773-343-432','434-43-432')
# name,email,*phone_numbers = record
# print(name)
# print(email)
# print(phone_numbers)
#------------------------------

# records = [
# ('foo', 1, 2),
# ('bar', 'hello'),
# ('foo', 3, 4),
# ]
#
# def do_foo(x,y):
#     return ('foo',x,y)
#
# def do_bar(s):
#     print('bar',s)
#
# for tag,*args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
# ----------------------------
items = [1, 10, 7, 4, 5, 9]
# head,*tail = items
# print(head)
# print(tail)

def sum(items):
    head,*tail = items
    return head + sum(tail) if tail else head
print(sum(items))