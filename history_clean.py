import re
import shutil
import os
import time


#---------------------------------------------------

#// 2024-08-06 Tue 03:57

#---------------------------------------------------
start = time.time()

#---------------------------------------------------
# Global variables

# Set history file name:
filename = "history.txt"
# filename = "~/.bash_history"

bset = set()
bfile = ''
bhistory = ''


#---------------------------------------------------


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
    file2 = ''
    # x = 0
    for line in sorted(bset):
        # x += 1
        # print(x)
        file2 += line + "\n"
        #file2 += "y"

    return file2


def backup_old_history():
    try:
        # current_time = datetime.now()
        # dt_string = current_time.strftime("%Y.%m.%d.%H%M%S")

        t = time.time()
        dt_string = time.strftime("%y%m%d%H%M%S", time.localtime(t))

        src = bhistory

        dst = bhistory + "-" + dt_string
        shutil.copyfile(src, dst)
    # except:
    except Exception as e:
        print_error_traceback(e, "Backup Error")
        # pass
    else:
        pass
    finally:
        pass

def print_error_traceback(e, msg=None):
    if msg: print(msg)
    print(e.args)
    print(e.with_traceback)

def write_file():
    try:
        # f = open(bhistory, "w")
        # f.write(file_out)
        with open(bhistory, "w") as f:
            f.write(file_out)
    except:
        print("error_write_file")
    else:
        pass
    finally:
        # if 'f' in locals(): f.close()
        pass

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

def open_file():
    # open file
    # global bfile, bhistory
    global bfile
    bhistory = os.path.expanduser(filename)
    # bfile = open(bhistory, 'r')
    with open(bhistory, 'r') as ofile:
        bfile = ofile.readlines()
    bfile = set(bfile)


#---------------------------------------------------

open_file()
read_lines()
file_out = sort_lines()
backup_old_history()
# write_file()

# print(file_out)


#---------------------------------------------------
# Display elapsed time:

print( (str(time.time() - start))[:5] + " secs" )

#---------------------------------------------------

# write_file()


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


# import time

# from datetime import datetime as dt
# print( time.time() )
# print ( dt.timestamp(dt.now()) )

# t = time.time()

# local = time.strftime('%y-%m-%d %H:%M %Z', time.localtime(t))
# local2 = time.strftime('%y-%m-%d %H:%M:%S %Z')
# #'2019-05-27 12:03 CEST'

# gm = time.strftime('%Y-%m-%d %H:%M %Z', time.gmtime(t))
# #'2019-05-27 10:03 GMT'

# print(local)
# print(local2)
# print(gm)
