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

bset = set()
file_out = ''

# Add line to set variable
def add_line(bline):
    bset.add(bline)


# open file
bhistory = os.path.expanduser(filename)
bfile = open(bhistory)

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


def sort_lines():
    file_out = ''
    for line in sorted(bset):
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



#---------------------------------------------------

read_lines()
file_out = sort_lines()

backup_old_history()
write_file()


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