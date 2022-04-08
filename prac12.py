#prac12
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique = set()

for i in data:
    unique.add(i.get("V"))
    unique.add(i.get("VI"))
    unique.add(i.get("VII"))
    unique.add(i.get("VIII"))
    unique.remove(None)

print(unique)

#self

d1 = {'1': ['a', 'b'], '2': ['c', 'd']}

ls1 = d1['1']
ls2 = d1['2']

#print(ls1, ls2)

for i in ls1:
    for j in ls2:
        k = i + j
        print(k)