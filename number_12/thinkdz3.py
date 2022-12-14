s = 195 * "$"

while ("!!!" in s) or ("$$$" in s):
    if ("!!!" in s):
        s = s.replace("$$$", "!", 1)
    elif ("$$$" in s):
        s = s.replace("!!!", "$", 1)

print(s)

# ne rabotaet