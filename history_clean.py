#// 2024-08-06 Tue 03:57

import re


# print("hello")

bfile = open('.bash_history')
bset = set()

# pattern = r'^The'

# bfile.readline()
# print(bfile)

for line in bfile:
    bline = line.strip()
    if bline == '': continue
    if bline == '!': continue
    if bline == '"': continue
    # res = re.search(r"^#", bline)
    if ( re.search(r"^#", bline) ) : continue
    if ( re.search(r"^z ", bline) ) : continue
    if ( re.search(r"^man ", bline) ) : continue
    if ( re.search(r"^cd ", bline) ) : continue
    if ( re.search(r"^c ", bline) ) : continue
    if ( re.search(r"^hs ", bline) ) : continue
    if ( re.search(r"^~", bline) ) : continue
    if ( re.search(r"^vi ", bline) ) : continue
    if ( re.search(r"^vim ", bline) ) : continue
    if ( re.search(r"^\$", bline) ) : continue
    if ( re.search(r"^,", bline) ) : continue

    # print(res)
    # if res:
        # print(res.string)
        # break
    # if res: continue

    bset.add(bline)


# bset = sorted(bset)
# bset.sort()


# x = 0
y = ''
for line in sorted(bset):
    # x += 1
    # y += str(x) + ' : ' + line + "\n"
    y += line + "\n"
    # print(y)

# y += ''

# print(y)

f = open("history.txt", "w")
f.write(y)
f.close()

# fout = open('output.txt', 'W')
# fout.write(line1)

# fout.close()