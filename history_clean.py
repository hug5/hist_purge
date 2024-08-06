import re
import shutil
from datetime import datetime
import os

#// 2024-08-06 Tue 03:57

#----------------------------------------


# print("hello")
# bhistory = os.path.expanduser("~/.bash_history")
# bhistory = os.path.expanduser(".bash_history")
bhistory = os.path.expanduser("history.txt")

bfile = open(bhistory)
bset = set()

# pattern = r'^The'

# bfile.readline()
# print(bfile)

def addLine(bline):
    bset.add(bline)


for line in bfile:
    bline = line.strip()

    if ( re.search(r".*###$", bline) ) :
        addLine(bline)
        continue

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
    if ( re.search(r"^sudo apt search", bline) ) : continue
    if ( re.search(r"^sudo apt info", bline) ) : continue
    if ( re.search(r"^sudo apt update", bline) ) : continue
    if ( re.search(r"^vidir ", bline) ) : continue
    if ( re.search(r"^tree ", bline) ) : continue
    if ( re.search(r"^rm ", bline) ) : continue
    if ( re.search(r"^l ", bline) ) : continue
    if ( re.search(r"^ll ", bline) ) : continue
    if ( re.search(r"^yt-dlp", bline) ) : continue
    if ( re.search(r"^target ", bline) ) : continue
    if ( re.search(r"^source ", bline) ) : continue
    if ( re.search(r"^\.", bline) ) : continue
    if ( re.search(r"^\./", bline) ) : continue
    if ( re.search(r"^\?", bline) ) : continue
    if ( re.search(r"^:", bline) ) : continue
    if ( re.search(r"^.{1}$", bline) ) : continue


    addLine(bline)

    # print(res)
    # if res:
        # print(res.string)
        # break
    # if res: continue

    # bset.add(bline)


file_out = ''
for line in sorted(bset):
    file_out += line + "\n"

# print(file_out)

# quit()

current_time = datetime.now()
dt_string = current_time.strftime("%Y.%m.%d.%H%M%S")



try:
    src = bhistory
    # src = "sssssssxxx"
    dst = bhistory + "-" + dt_string
    shutil.copyfile(src, dst)

    f = open(bhistory, "w")
    # f = open("''", "w")
    f.write(file_out)
except:
    print("error")
    pass
else:
    pass
finally:
    if 'f' in locals(): f.close()









#------------------------------------------------

# yr = current_time.year
# mo = current_time.month
# d = current_time.day
# h = current_time.hour
# m = current_time.minute
# s = current_time.second

# dd/mm/YY H:M:S
# dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
# dt_string = current_time.strftime("%Y.%m.%d.%H%M%S")
