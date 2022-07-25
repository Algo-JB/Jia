alpa = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croa:
    alpa = alpa.replace(i, '#')

print(len(alpa))