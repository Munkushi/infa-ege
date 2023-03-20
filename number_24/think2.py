f = open("number_24/think2.txt").readline()

let = ""
mx = 1
ln = 1

for i in range(1, len(f)):
    if f[i] == f[i-1]:
        ln += 1
        if mx < ln:
            mx = ln
            let = f[i]
    else:
        ln = 1

print(let, mx)

