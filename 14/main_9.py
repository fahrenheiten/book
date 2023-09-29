# def example():
#     try:
#         int('N/A')
#     except ValueError as e :
#         raise RuntimeError('A parsing error occurred') from e
# example()
def example():
    try:
        example()
    except RuntimeError as e:
        print("It didn't work:", e)
        if e.__cause__:
            print('Cause:', e.__cause__)
example()
