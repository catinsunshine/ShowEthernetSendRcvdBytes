print()
print('Current data usage:')
with open('wl.txt') as f:
	cont=f.readlines()
	print(cont[-2].strip())
