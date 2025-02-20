users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
for keys in users:
    print(users.get(keys))
print(users.get('004', "indefinite"))
##if not users.get('004'):
##    print("'indefinite'")
