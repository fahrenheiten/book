import ipaddress
net = ipaddress.ip_network('123.45.67.64/27')
print(net)
for a in net:
    print(a)
print(net[-2])