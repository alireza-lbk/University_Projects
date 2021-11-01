#This is key generator of DES algorithm.
from random import randrange
# We have 2**56 or 72,057,594,037,927,936 permutations for valid key.
key_number=randrange(0,72057594037927936)
print("The number of key:%i"%key_number)

binary_mode=bin(key_number)[2:]
print("The binary form of the key:\n%s"%binary_mode)

binary_mode_length=len(binary_mode)
print("The length of binary form:",binary_mode_length)

if binary_mode_length != 56:
    binary_mode = binary_mode+(56-binary_mode_length)*'0'

print("The binary form of the key after zero padding:\n%s"%binary_mode)

print("The length of binary form of the key after zero padding:",len(binary_mode))

array_mode=[]

for i in range(8):
    array_mode.append(binary_mode[i*7:(i*7)+7])

for j in range(8):
    if array_mode[j].count('1')%2==0:
        array_mode[j]=array_mode[j]+'1'
    else:
        array_mode[j]=array_mode[j]+'0'
print("The string form:\n",*array_mode,sep='')
print("The table form:")

for k in array_mode:
    print(*k,sep='  ')
