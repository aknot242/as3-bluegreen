# VIP_INFO = [
#     ("192.0.2.10","Test1","App"),
#     ("192.0.2.11","Test2","App"),
#     ("192.0.2.12","Test3","App"),
#     ("192.0.2.13","Test4","App"),
#     ("192.0.2.14","Test5","App"),
#     ("192.0.2.15","Test6","App"),
#     ("192.0.2.16","Test7","App"),
#     ("192.0.2.17","Test8","App"),
#     ("192.0.2.18","Test9","App"),
#     ("192.0.2.19","Test10","App"),
#     ("192.0.2.20","Test11","App"),
#     ("192.0.2.21","Test12","App"),
#     ("192.0.2.22","Test13","App"),
#     ("192.0.2.23","Test14","App"),
#     ("192.0.2.24","Test15","App")
# ]
VIP_INFO = []
address_format = "192.0.2.{octet}"
tenant_format = "test{id}"
for k in range (150):
    VIP_INFO.append((address_format.format(octet = k+10),tenant_format.format(id = k),"App"))
