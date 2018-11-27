
"""my try"""
#name = (input('Enter your name: '))
#names_as_bytes = name.encode("utf-8")


"""print(names_as_bytes)"""

name = input('Enter your name: ')

bytes1 = bytes(name, 'utf-8')
print(bytes1)

for b1 in bytes1:
    print(b1, end=' ')

print()


