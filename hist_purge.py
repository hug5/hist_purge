import re, shutil, os, time, tomli
import sys

#---------------------------------------------------

# // 2024-08-06 Tue 03:57
# // 2024-08-08 Thu 23:14
#---------------------------------------------------


class history_clean():

    def __init__(self):

        self.filename = ""
            # history path/file; from config;
        # self.bhistory = ''
        # self.filename_os = ''
            # history path, fully expanded

        self.filename_write = ''
            # by default, is self.filename;
            # but for testing, can be different name;

        self.sort_history = True
            # sort or not sort history
        self.bfile2 = {}
            # Original history; then made into set;
        self.bfile3 = []
            # Filtered history list
            # Then optionally sorted;

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

        self.start()

        pass


    def print_error_traceback(self, e, msg=None):

        if msg: print("Error: " + msg)
        print(e)          # __str__ allows args to be printed directly,
        print("Type: " + str(type(e)))    # the exception type

        # Exit
        raise SystemExit

        # if e.args: print(e.args)
        # # print(e.args[1])
        # print(e.args)     # arguments stored in .args
        # print(e.with_traceback)
        # raise
        # raise SystemExit

        # exit()
        # sys.exit() # requires sys module


    def write_file(self):
        try:

            # with open(self.filename_os, "w") as f:
            with open(self.filename_write, "w") as f:
                f.write(self.file_out)

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

            src = self.filename
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


    def exclude_line(self, bline):

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


    def include_line(self, bline) :

        for pattern in self.filter_rules['include']["exact"]:
            if pattern == bline:
                # print(pattern + " : " + bline)
                # print("◌", end ="")
                # sys.stdout.flush()
                return True

        for pattern in self.filter_rules['include']["containing"]:
            if bline.find(pattern) >= 0:
                # print(pattern + " : " + bline)
                # print("◍", end ="")
                # sys.stdout.flush()
                return True

        for pattern in self.filter_rules['include']["regex"]:
            if re.search(pattern, bline):
                # return True
                # print(pattern + " : " + bline)
                # print("o", end ="")
                # sys.stdout.flush()
                return True

        # print("false")
        # print(".", end ="")
        # sys.stdout.flush()
        return False


    # Read file line by line
    def read_lines(self):

        ascii_sym = "∘ "
        c = 0
        for line in self.bfile2:

            c += 1
            if c % 3000 == 0:
                print(ascii_sym, end ="")
                sys.stdout.flush()

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

        print(ascii_sym)

        # print(".")
        # self.bfile3 = bfile3

    def make_set(self):
        """
        Remove duplicates, but preserve order of new list
        Just doing set([index]) does not preserve order;
        Could just do this to make into set:
          self.bfile2 = set(self.bfile2)
        """

        try:
            # a = [1, 2, 20, 6, 210]
            # b = set([6, 20, 1])
            # c = [x for x in a if x not in b]
            # [2, 210]

            # a = self.bfile2
            b = set(self.bfile2)
            # a = [1, 2, 3, 4, 2, 3, 4, 4, 5, 6]
            # b = set([5, 3, 2, 4, 1, 6])


            if not self.sort_history:

                # x3 = [0]
                # self.swatch(x3, "start")

                c = []

                # for x in a:
                for xline in self.bfile2:
                    if xline in b:
                        b.remove(xline)
                        c.append(xline)

                self.bfile2 = c

                # self.swatch(x3, "stop")
                # raise SystemExit

            else:
                self.bfile2 = b


        except Exception as e:
            self.print_error_traceback(e, "Make Set Error")

            # raise SystemExit



    def open_history_file(self):

        try:
            # filename_os = os.path.expanduser(self.filename)
            # bfile = open(bhistory, 'r')
            with open(self.filename, 'r') as ofile:
                self.bfile2 = ofile.readlines()

            # make list into set
            # self.bfile2 = set(self.bfile2)

        except Exception as e:
            self.print_error_traceback(e, "Open File Error")
            # handleException(e)
            # raise



    def load_conf(self):
        # os.path.isfile(path)
        # except FileNotFoundError:
        # Exception types:
        # https://www.w3schools.com/python/python_ref_exceptions.asp
        # https://docs.python.org/3/reference/simple_stmts.html#raise
        # https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions

        # Get user's home directory:
        user_home = os.path.expanduser("~/")
        config_file1 = "hist_purge.toml"
        config_file2 = ".hist_purge.toml"
        config_path = ''  # the found path location of config.toml


        # precedence: ./.hist, ./hist, ~/.hist, ~/hist
        # Current folder has precedence; then home; hidden has precedence over normal;

        try:
            if os.path.isfile(config_file2):
                config_path = config_file2
            elif os.path.isfile(config_file1):
                config_path = config_file1
            elif os.path.isfile(user_home + config_file2):
                config_path = user_home + config_file2
            elif os.path.isfile(user_home + config_file1):
                config_path = user_home + config_file1
            else:
                raise FileNotFoundError("Could not find " + config_file1 + " conf file")

        except FileNotFoundError as e:
            self.print_error_traceback(e, "No " + config_file1)



        # user_config = user_home + ".config"
        # print(user_home + ", " + user_config)
        # raise SystemExit


        try:
            with open(config_path, 'rb') as ftoml:
                config = tomli.load(ftoml)
              # If bad, should give FileNotFoundError

            self.filename = config['history_source_file']
            if self.filename == '': raise NameError("No history_source_file")

            # rename filename to the os.path name;
            self.filename = os.path.expanduser(self.filename)
            # config['history_source_file'] = filename_os

            # Check for existence of history_write_file key; check if there is a value; if blank or doesn't exist, then default to self.filename;
            if not "history_write_file" in config or config['history_write_file'] == "":
                self.filename_write = self.filename

            # If it does exist, then get the os.path
            else:
                self.filename_write = config['history_write_file']
                self.filename_write = os.path.expanduser(self.filename_write)



            # Checking for no key, but not the value of the key; if not false/true, then will error
            if not "sort_lines" in config: config['sort_lines'] = True

            # Anything bad below should raise ValueError or KeyError:
            self.sort_history = config['sort_lines']


            exact_include = []
            exact_exclude = []
            containing_include = []
            containing_exclude = []
            regex_include = []
            regex_exclude = []

            # Filter rules should be option; if not set or keys not set, then set to blank;'
            if "filter_rules" in config:
                if "exact_include" in config['filter_rules']:
                    exact_include = config['filter_rules']['exact_include']
                if "exact_exclude" in config['filter_rules']:
                    exact_exclude = config['filter_rules']['exact_exclude']

                if "containing_include" in config['filter_rules']:
                    containing_include = config['filter_rules']['containing_include']
                if "containing_exclude" in config['filter_rules']:
                    containing_exclude = config['filter_rules']['containing_exclude']

                if "regex_include" in config['filter_rules']:
                    regex_include = config['filter_rules']['regex_include']
                if "regex_exclude" in config['filter_rules']:
                    regex_exclude = config['filter_rules']['regex_exclude']


            self.filter_rules["include"]["exact"] = exact_include
            self.filter_rules["exclude"]["exact"] = exact_exclude

            self.filter_rules["include"]["containing"] = containing_include
            self.filter_rules["exclude"]["containing"] = containing_exclude

            self.filter_rules["include"]["regex"] = regex_include
            self.filter_rules["exclude"]["regex"] = regex_exclude

            # print( toml.dumps(self.filter_rules) )
            # raise SystemExit

        except tomli.TOMLDecodeError as e:
            self.print_error_traceback(e, "Improper toml configuration.")
        except FileNotFoundError as e:
            self.print_error_traceback(e, "No config file.")
        except NameError as e:
            self.print_error_traceback(e)
        except ValueError as e:
            self.print_error_traceback(e, "Bad config key value.")
        except KeyError as e:
            self.print_error_traceback(e, "Missing config key.")
        except Exception as e:
            self.print_error_traceback(e, "Config load error.")
            # Hopefully this catches anything else;

        # print(config)
        # exit()
        # raise SystemExit


    # def swatch(self, x, t='start'):
    def swatch(self, x = 'start'):
        """ To start, do: x = self.swatch()
        To stop, pass back the variable: self.swatch(x) """

        if x == "start":
            return time.time()
        else:
            stop = time.time()
            print(str(stop - x)[:5] + " seconds." )


    def start(self):

        x = self.swatch()

        self.load_conf()
        self.open_history_file()
        self.make_set()
        self.read_lines()
        self.sort_lines()
        self.backup_old_history()
        self.write_file()

        print("Done.")

        self.swatch(x)


def run():
    jug = history_clean()

    # pass


if __name__ == '__main__':
    jug = history_clean()
    # jug.start()
    # history_clean()

# mug
# jug
# clug





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




    # print(config)
    # pprint.pprint(config)  # requires import pprint
    # print(json.dumps(config, indent=2, sort_keys=True))
    # print(json.dumps(config, indent=2))  # requires import json

    # print(toml.dumps(config))  # Native to toml
    # print(config['title'])

    # if "exact_exclude" in config:
    #     print("yes")
    # else:
    #     print("no")

    # raise SystemExit


