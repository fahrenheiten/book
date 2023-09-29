from unittest.mock import patch

# A mocked module 'example' with a function 'func'
class example:
    @staticmethod
    def func(arg):
        print(f"Original func called with {arg}")

x = 10

@patch('example.func')
def test1(mock_func):
    example.func(x)
    mock_func.assert_called_with(x)

with patch('example.func') as mock_func:
    example.func(x)
    mock_func.assert_called_with(x)

test1()
