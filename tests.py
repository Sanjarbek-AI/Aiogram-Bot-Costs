a = "Sanjarbek"
result = ""
new = list()
for i in a:
    new.append(i)

g = new[0]
for s in range(len(new) - 1):
    new[s] = new[s + 1]

new[-1] = g
for char in new:
    result += char

print(result)
