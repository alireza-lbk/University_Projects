while True:
    received_key=input("Please enter the key:")
    if len(received_key)==64:
        print("The key is saved.")
        break
    else:
        print("The entered key is not valid.Please enter it again.")
#Checking the odd parity
for i in range(8):
    if received_key[i*8:(i*8)+8].count('1')%2==0:
        print("Invalid Key")
        exit()
    else:
        continue
print("The received key is valid.")
