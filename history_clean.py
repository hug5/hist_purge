import re
import shutil
from datetime import datetime
import os

#// 2024-08-06 Tue 03:57

#----------------------------------------

# Set history file name:
filename = "history.txt"
# filename = "~/.bash_history"



#----------------------------------------

# Add line to set variable
def add_line(bline):
    bset.add(bline)
    # bset.append(bline)
    # add is a set method; not list method;
    # So this should guarantee creation of set;


# regex excludes:
def exclude_line(bline):

    if bline == '': return True
    elif bline == '!': return True
    elif bline == '"': return True
    # res = re.search(r"^#", bline)
    elif ( re.search(r"^#", bline) ) : return True
    elif ( re.search(r"^z ", bline) ) : return True
    elif ( re.search(r"^man ", bline) ) : return True
    elif ( re.search(r"^cd ", bline) ) : return True
    elif ( re.search(r"^c ", bline) ) : return True
    elif ( re.search(r"^hs ", bline) ) : return True
    elif ( re.search(r"^~", bline) ) : return True
    elif ( re.search(r"^vi ", bline) ) : return True
    elif ( re.search(r"^vim ", bline) ) : return True
    elif ( re.search(r"^\$", bline) ) : return True
    elif ( re.search(r"^,", bline) ) : return True
    elif ( re.search(r"^sudo apt search", bline) ) : return True
    elif ( re.search(r"^sudo apt info", bline) ) : return True
    elif ( re.search(r"^sudo apt update", bline) ) : return True
    elif ( re.search(r"^vidir ", bline) ) : return True
    elif ( re.search(r"^tree ", bline) ) : return True
    elif ( re.search(r"^rm ", bline) ) : return True
    elif ( re.search(r"^l ", bline) ) : return True
    elif ( re.search(r"^ll ", bline) ) : return True
    elif ( re.search(r"^yt-dlp", bline) ) : return True
    elif ( re.search(r"^target ", bline) ) : return True
    elif ( re.search(r"^source ", bline) ) : return True
    elif ( re.search(r"^\.", bline) ) : return True
    elif ( re.search(r"^\./", bline) ) : return True
    elif ( re.search(r"^\?", bline) ) : return True
    elif ( re.search(r"^:", bline) ) : return True
    elif ( re.search(r"^.{1}$", bline) ) : return True

    return False


# regex includes:
def include_line(bline) :
    if re.search(r".*###$", bline) : return True


def sort_lines():
    file_out = ''
    # x = 0
    for line in sorted(bset):
        # x += 1
        # print(x)
        file_out += line + "\n"
        #file_out += "y"

    return file_out


def backup_old_history():
    try:
        current_time = datetime.now()
        dt_string = current_time.strftime("%Y.%m.%d.%H%M%S")

        src = bhistory
        dst = bhistory + "-" + dt_string
        shutil.copyfile(src, dst)
    except:
        print("error_backup")
        pass
    else:
        pass
    finally:
        pass


def write_file():
    try:
        f = open(bhistory, "w")
        f.write(file_out)
    except:
        print("error_write_file")
    else:
        pass
    finally:
        if 'f' in locals(): f.close()


# Read file line by line
def read_lines():

    for line in bfile:
        bline = line.strip()

        # Check for specific includes;
        if include_line(bline) == True:
          add_line(bline)
          continue

        # Check for exclude;
        # If true, then skip;
        if exclude_line(bline) == True:
          continue

        # Include everything else
        add_line(bline)


#---------------------------------------------------

import time
start = time.time()
#---------------------------------------------------


bset = set()
file_out = ''
bfile = ''
# bset_temp = set()

# open file
bhistory = os.path.expanduser(filename)
# bfile = open(bhistory, 'r')
with open(bhistory, 'r') as ofile:
    bfile = ofile.readlines()

bfile = set(bfile)
read_lines()
file_out = sort_lines()



#---------------------------------------------------
end = time.time()
print(end - start)



# print(file_out)
# quit()

# backup_old_history()
# write_file()

# quit()






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

# print(res)
# if res:
    # print(res.string)
    # break
# if res: continue

# bset.add(bline)


# -------------------

# readline() : reads single line
# readlines() : read everything into a list object or set; carriage returns are converted to \n; reads a single line of the file
# read() : reads everything as a single string;

# -------------------


# with open(bhistory, 'r') as bfile:
#     for line in bfile:
#     print('Total lines:', num_lines) # 8

# # bfile.close()
#   with open('notes-pycrash.txt') as file_object:
#       contents = file_object.read()
#   print(contents)
#   # No need to close with this syntax
#  # Can do readline(), readlines() and read()
#   # readline seemsto read just 1 line;
#   # readlines reads everything, but carriage returns are converted to \n
#   # read() reads everything;

#     filename = 'programming.txt'
#   with open(filename, 'w') as fo:
#       fo.write("Ixx love programming.\n")
#       fo.write("Do you love programming?\n")
#       # And can add more lines like so above;

# myfile = open("demo.txt", "r")
# myline = myfile.readline()
# while myline:
#     print(myline)
#     myline = myfile.readline()
# myfile.close()


# with open(bhistory, 'r') as ofile:
#     # When use the 'with' syntax, don't have to close file;
#     # bset_temp = set(ofile.readline())
#     # print(ofile.readline())
#     # bfile = ofile.readline() # read one line
#     # bfile = ofile.read() # read all

#     bfile = ofile.readlines()
#     # for myline in mylines
#     #     bfile += myline + "\n"
#     #     myline = ofile.readline()

#     # for line in ofile:
#     #     bset += line.readline