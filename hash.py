import hashlib

print('hello, Welcome to SHA256 hash!')
myinput = input('\nPlease Type String : ')

this_hash_obj = hashlib.sha256(myinput.encode())
print('\n')
print('SHA256 hash: ', this_hash_obj.hexdigest())
