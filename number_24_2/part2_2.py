f = open("number_24_2/3_1.txt").readline()

ln = 0
mx = 0
cnt = 0

print(max([len(fragment) for fragment in f.split("A") if fragment.count("E") > 2]))
