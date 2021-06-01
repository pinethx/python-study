list_a = [[10, 20], [30, 40, 70, 110], [50, 60], [80, 90, 100]]
dict_a = {'k': {'a':10, 'b':20}, 'l': {'a':10, 'b':20, 'c':40}, 'm': {'a':10}}

for i in range(len(list_a)):
    for j in range(len(list_a[i])):
        print(list_a[i][j], end=" ")
    print()

print()

firstkey=[]
for i in range(len(dict_a)):
    firstkey.append(list(dict_a.keys())[i])
    print(firstkey[i] + " -> ", end="")
    secondkey=[]
    for j in range(len(dict_a[firstkey[i]])):
        secondkey.append(list(dict_a[firstkey[i]].keys())[j])
        print('{} : {},'.format(secondkey[j], dict_a[firstkey[i]][secondkey[j]]), end=" ")
    print()
print()

for key in dict_a:
    print(key, " ->", end=" ")
    for k in dict_a[key]:
        print('{} : {},'.format(k, dict_a[key][k]), end="")
    print()