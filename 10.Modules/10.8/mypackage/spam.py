# import pkgutil
#
# data = pkgutil.get_data(__package__, 'somedata.dat')
#
# if data is not None:
#     decoded_data = data.decode('utf-8')  # Adjust encoding if needed
#     print(decoded_data)
# else:
#     print("Data not found.")
import pkgutil

if __package__:
    data = pkgutil.get_data(__package__, 'somedata.dat')
else:
    data = None

if data is not None:
    decoded_data = data.decode('utf-8')  # Adjust encoding if needed
    print(decoded_data)
else:
    print("Data not found.")
