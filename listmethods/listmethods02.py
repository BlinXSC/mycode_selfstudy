#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)

# Adds DNS to the end of both lists
proto.append("dns")
protoa.append("dns")

print(proto)

proto2 = [22, 80, 443, 53] #List of common ports
proto.append(proto2)
print(proto)
protoa.append(proto2)
print(proto)

print(proto.count('http'))

proto.insert(5,"smtp")
print(proto)