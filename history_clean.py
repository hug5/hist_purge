import re
import shutil
import os
import time
import toml


#---------------------------------------------------

#// 2024-08-06 Tue 03:57

#---------------------------------------------------


class history_clean():

    def __init__(self):

        self.filename = ""
            # history path/file; from config;
        # self.bhistory = ''
        self.filename_os = ''
            # history path, fully expanded

        self.sort_history = True
            # sort or not sort history
        self.bfile1 = []
            # Original history, but unduplicated
        self.bfile2 = {}
            # Filtered history list
        self.bfile3 = []

        self.file_out = ''
            # final String file to save to disk

        # Filter dictionary:
        self.filter_rules = {
            "include" : {
                "exact" : [],
                "containing" : [],
                "regex" : []
            },
            "exclude" : {
                "exact" : [],
                "containing" : [],
                "regex" : []
            }
        }

        # self.regex_include = []
        # self.regex_exclude = []
        # self.containing_include = []
        # self.containing_exclude = []
        # self.exact_include = []
        # self.exact_exclude = []

        self.start()

        pass


    def print_error_traceback(self, e, msg=None):
        if msg: print(msg)
        print(e.args)
        print(e.with_traceback)


    def write_file(self):
        try:
            # f = open(bhistory, "w")
            # f.write(file_out)
            # with open(self.filename_os, "w") as f:
            # with open("history2.txt", "w") as f:
            with open(self.filename_os, "w") as f:
                f.write(self.file_out)

            # print("done")
            # print(self.file_out)

        except Exception as e:
            self.print_error_traceback(e, "Error Write File")

        else:
            pass
        finally:
            # if 'f' in locals(): f.close()
            pass


    def backup_old_history(self):
        try:
            # current_time = datetime.now()
            # dt_string = current_time.strftime("%Y.%m.%d.%H%M%S")

            t = time.time()
            dt_string = time.strftime("%y%m%d%H%M%S", time.localtime(t))

            src = self.filename_os
#
            dst = src + "-" + dt_string
            shutil.copyfile(src, dst)
        # except:
        except Exception as e:
            self.print_error_traceback(e, "Backup Error")
            # pass
        else:
            pass
        finally:
            pass


    def sort_lines(self):
        # file_out = ''

        if self.sort_history == True:
            self.bfile3 = sorted(self.bfile3)
            # this will change bfile1 from set to list

        # file_out = ''
        # for line in self.bfile3:
        #     # x += 1
        #     # print(x)
        #     file_out += line + "\n"
        #     #file_out += "y"

        self.file_out = "\n".join(self.bfile3)
        # self.file_out = file_out

        self.bfile3 = []   # empty out list
        # self.file_out = file_out


    # Add line to set variable
    # def add_line(self, bline):
    #     # self.bfile1.add(bline)    # set
    #     # self.bfile1.append(bline)   # list
    #     # lll.append(bline)   # list
    #     # bset.append(bline)
    #     # add is a set method; not list method;
    #     # So this should guarantee creation of set;
    #     pass

    def exclude_line(self, bline):
        # for pattern in self.rules_exclude:
            # if re.search(r".*###$", bline) : return True
            # if re.search(r_include, bline) : return True
            # if re.search(pattern, bline):
        #     if re.search(pattern, bline):
        #         print(pattern)
        #         print(bline)
        #         print("exclude rule")
        #         # quit()
        #         return True

        # return False


        for pattern in self.filter_rules['exclude']["exact"]:
            if pattern == bline:
                # print(pattern + " : " + bline)
                # print("✕", end ="")
                return True

        for pattern in self.filter_rules['exclude']["containing"]:
            if bline.find(pattern) >= 0:
                # print(pattern + " : " + bline)
                # print("✖", end ="")
                return True

        for pattern in self.filter_rules['exclude']["regex"]:
            if re.search(pattern, bline):
                # print(pattern + " : " + bline)
                # print("x", end ="")
                return True

        # print("false")
        # print(".", end ="")
        return False



        ###
            # if bline == '': return True
            # elif bline == '!': return True
            # elif bline == '"': return True
            # # res = re.search(r"^#", bline)
            # elif ( re.search(r"^#", bline) ) : return True
            # elif ( re.search(r"^z ", bline) ) : return True
            # elif ( re.search(r"^man ", bline) ) : return True
            # elif ( re.search(r"^cd ", bline) ) : return True
            # elif ( re.search(r"^c ", bline) ) : return True
            # elif ( re.search(r"^hs ", bline) ) : return True
            # elif ( re.search(r"^~", bline) ) : return True
            # elif ( re.search(r"^vi ", bline) ) : return True
            # elif ( re.search(r"^vim ", bline) ) : return True
            # elif ( re.search(r"^\$", bline) ) : return True
            # elif ( re.search(r"^,", bline) ) : return True
            # elif ( re.search(r"^sudo apt search", bline) ) : return True
            # elif ( re.search(r"^sudo apt info", bline) ) : return True
            # elif ( re.search(r"^sudo apt update", bline) ) : return True
            # elif ( re.search(r"^vidir ", bline) ) : return True
            # elif ( re.search(r"^tree ", bline) ) : return True
            # elif ( re.search(r"^rm ", bline) ) : return True
            # elif ( re.search(r"^l ", bline) ) : return True
            # elif ( re.search(r"^ll ", bline) ) : return True
            # elif ( re.search(r"^yt-dlp", bline) ) : return True
            # elif ( re.search(r"^target ", bline) ) : return True
            # elif ( re.search(r"^source ", bline) ) : return True
            # elif ( re.search(r"^\.", bline) ) : return True
            # elif ( re.search(r"^\./", bline) ) : return True
            # elif ( re.search(r"^\?", bline) ) : return True
            # elif ( re.search(r"^:", bline) ) : return True
            # elif ( re.search(r"^.{1}$", bline) ) : return True
            # return False


    def include_line(self, bline) :

        # for pattern in self.rules_include:
        # for pattern in self.regex_include:
        #     # if re.search(r".*###$", bline) : return True
        #     # if re.search(pattern, bline) : return True
        #     # if re.search(pattern, bline):
        #     if re.search(pattern, bline):
        #         # return True
        #         print("include" + bline)
        #         return True
        # return False

        for pattern in self.filter_rules['include']["exact"]:
            if pattern == bline:
                # print(pattern + " : " + bline)
                # print("◌", end ="")
                return True

        for pattern in self.filter_rules['include']["containing"]:
            if bline.find(pattern) >= 0:
                # print(pattern + " : " + bline)
                # print("◍", end ="")
                return True

        for pattern in self.filter_rules['include']["regex"]:
            if re.search(pattern, bline):
                # return True
                # print(pattern + " : " + bline)
                # print("o", end ="")
                return True

        # print("false")
        return False


    # Read file line by line
    def read_lines(self):

        # bfile3 = []

        c = 0
        for line in self.bfile2:

            # print(".", end ="")
            bline = line.strip()
            # print(bline)

            # Check for specific includes;
            if self.include_line(bline) == True:
                # print("adding1" + bline)
                # lll = self.add_line(bline)
                # self.bfile3.append(bline)

                # print("x", end ="")
                self.bfile3 += [bline]
                continue

            # Check for exclude;
            # If true, then skip;
            if self.exclude_line(bline) == True:
                # print("excluding2" + bline)
                # print(".", end ="")
                continue

            # Include everything else
            # lll = self.add_line(bline)
            # self.bfile3.append(bline)
            # print(".", end ="")
            self.bfile3 += [bline]


        # print(".")
        # self.bfile3 = bfile3


    def open_file(self):
        # open file
        # self.global bfile, bhistory
        # global bfile
        self.filename_os= os.path.expanduser(self.filename)
        # bfile = open(bhistory, 'r')
        with open(self.filename_os, 'r') as ofile:
            self.bfile1 = ofile.readlines()

        # make list into set
        self.bfile2 = set(self.bfile1)



    def load_conf(self):

        try:
            with open('config.toml', 'r') as ftoml:
                config = toml.load(ftoml)


            self.filename = config['settings']['history_file']
            self.sort_history = config['settings']['sort_lines']

            # self.filter_rules["include"]["exact"] = config['filter_rules']['exact_include']
            self.filter_rules["include"]["exact"] = config['filter_rules']['exact_include']
            self.filter_rules["exclude"]["exact"] = config['filter_rules']['exact_exclude']

            self.filter_rules["include"]["containing"] = config['filter_rules']['containing_include']
            self.filter_rules["exclude"]["containing"] = config['filter_rules']['containing_exclude']

            self.filter_rules["include"]["regex"] = config['filter_rules']['regex_include']
            self.filter_rules["exclude"]["regex"] = config['filter_rules']['regex_exclude']

            # print(self.filter_rules)
            # quit()
            # self.filter_rules["exclude"]["exact"] = config['filter_rules']['exact_exclude']
            # self.filter_rules["include"]["regex"] = config['filter_rules']['regex_include']
            # self.filter_rules["exclude"]["regex"] = config['filter_rules']['regex_exclude']
            # self.filter_rules["include"]["containing"] = config['filter_rules']['containing_include']
            # self.filter_rules["exclude"]["containing"] = config['filter_rules']['containing_exclude']

            # self.rules_exact_exclude = config['filter_rules']['exact_exclude']
            # self.rules_exact_include = config['filter_rules']['exact_include']
            # self.rules_regex_exclude = config['filter_rules']['regex_exclude']
            # self.rules_regex_include = config['filter_rules']['regex_include']
            # self.rules_containing_exclude = config['filter_rules']['containing_exclude']
            # self.rules_containing_include = config['filter_rules']['containing_include']



        except Exception as e:
            self.print_error_traceback(e, "Config Load Error")


    def start(self):

        start = time.time()

        self.load_conf()
        self.open_file()
        self.read_lines()
        self.sort_lines()
        self.backup_old_history()
        self.write_file()

        print("Done.")
        print( (str(time.time() - start))[:5] + " seconds." )
        # print(file_out)



if __name__ == '__main__':
    history_clean()


#---------------------------------------------------
# Display elapsed time:





#---------------------------------------------------
### Notes
#---------------------------------------------------


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
