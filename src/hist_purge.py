import re, shutil, time, tomli
# import os
import sys
from pathlib import Path

#---------------------------------------------------
# // 2024-08-06 Tue 03:57
# // 2024-08-08 Thu 23:14
# https://github.com/hug5/hist_purge
#---------------------------------------------------


class hist_purge():

    def __init__(self):

        self.filename = ""
            # history path/file; from config; then expanded;

        self.filename_write = ''
            # by default, is self.filename;
            # but for testing, can be different name;

        self.sort_history = True
            # sort or not sort history

        self.bfile2 = []
            # Original history; then make into set;
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
        print(e)
        # __str__ allows args to be printed directly,
        print("Type: " + str(type(e)))
          # the exception type

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

            self.std_out("Save file.")

            # with open(self.filename_os, "w") as f:
            with open(self.filename_write, "w") as f:
                f.write(self.file_out)

        except Exception as e:
            self.print_error_traceback(e, "Error Write File")

        else:
            pass
        finally:
            pass


    def backup_old_history(self):
        try:

            self.std_out("Backup file.")

            t = time.time()
            dt_string = time.strftime("%y%m%d%H%M%S", time.localtime(t))

            src = str(self.filename)

            # Have to make into string; gets error because using Pathlib;
            # and that's not a string;
            dst = str(src) + "-" + dt_string
            shutil.copyfile(src, dst)


        except Exception as e:
            self.print_error_traceback(e, "Backup Error")

        else:
            pass
        finally:
            pass


    def sort_lines(self):

        if self.sort_history == True:
            self.bfile3 = sorted(self.bfile3)

        self.file_out = "\n".join(self.bfile3)

        # empty out list
        self.bfile3 = []


    def exclude_line(self, bline):

        for pattern in self.filter_rules['exclude']["exact"]:
            if pattern == bline:
                return True

        for pattern in self.filter_rules['exclude']["containing"]:
            if bline.find(pattern) >= 0:
                return True

        for pattern in self.filter_rules['exclude']["regex"]:
            if re.search(pattern, bline):
                return True

        return False


    def include_line(self, bline) :

        for pattern in self.filter_rules['include']["exact"]:
            if pattern == bline:
                return True

        for pattern in self.filter_rules['include']["containing"]:
            if bline.find(pattern) >= 0:
                return True

        for pattern in self.filter_rules['include']["regex"]:
            if re.search(pattern, bline):
                return True

        return False

    def std_out(self, msg, cr = True):
        eol = "\n" if cr == True else ""
            # Python's lame ternary operator

        print(msg, end = eol)
        sys.stdout.flush()


    # Read file line by line
    def read_lines(self):

        self.std_out("Begin purge: ", False)

        ascii_sym = "∘ "
        c = 0
        for line in self.bfile2:

            c += 1
            if c % 2500 == 0:
                self.std_out(ascii_sym, False)

            bline = line.strip()

            # Check for specific includes;
            if self.include_line(bline) == True:
                self.bfile3 += [bline]
                continue

            # Check for exclude;
            # If true, then skip;
            if self.exclude_line(bline) == True:
                continue

            # Include everything else
            self.bfile3 += [bline]

        print(ascii_sym)



    def make_set(self):
        """
        Remove duplicates, but preserve order of new list
        Just doing set([index]) does not preserve order;
        Could just do this to make into set:
          self.bfile2 = set(self.bfile2)
        """

        try:
            b = set(self.bfile2)
            # self.bfile2 is a list; then save to b as set;
            # Sets do not preserve order; sets have no defined order;

            # If NOT sort, then preserve order based on original bfile2
            if not self.sort_history:

                c = []

                for xline in self.bfile2:
                    if xline in b:
                        b.remove(xline)
                        c.append(xline)

                self.bfile2 = c

            # If sort, then don't care; set bfile2 = b;
            # Then later will sort in sort function;
            else:
                self.bfile2 = b


        except Exception as e:
            self.print_error_traceback(e, "Make Set Error")


    def open_history_file(self):

        self.std_out("Open history file.")

        try:
            with open(self.filename, 'r') as ofile:
                self.bfile2 = ofile.readlines()
                # This is loaded as list; later change to set;

        except Exception as e:
            self.print_error_traceback(e, "Open File Error")


    def load_conf(self):
        # os.path.isfile(path)
        # except FileNotFoundError:
        # Exception types:
        # https://www.w3schools.com/python/python_ref_exceptions.asp
        # https://docs.python.org/3/reference/simple_stmts.html#raise
        # https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions

        self.std_out("Load config.")

        # Get user's home directory:
        # user_home = os.path.expanduser("~/")
        user_home = Path.home()
        config_file1 = "hist_purge.toml"
        config_file2 = ".hist_purge.toml"
        config_path = ''  # the found path location of config.toml


        # precedence: ./.hist, ./hist, ~/.hist, ~/hist
        # Current folder has precedence; then home; hidden has precedence over normal;

        try:

            if Path(config_file2).is_file():
                config_path = config_file2
            elif Path(config_file1).is_file():
                config_path = config_file1
            elif Path(user_home / config_file2).is_file():
                config_path = Path(user_home / config_file2)
            elif Path(user_home / config_file1).is_file():
                config_path = Path(user_home / config_file1)
            else:
                raise FileNotFoundError("Could not find " + config_file1 + " conf file")

        except FileNotFoundError as e:
            self.print_error_traceback(e, "No " + config_file1)



        try:
            with open(config_path, 'rb') as ftoml:
                config = tomli.load(ftoml)
              # If bad, should give FileNotFoundError

            self.filename = config['history_source_file']
            if self.filename == '': raise NameError("No history_source_file")

            # rename filename to the os.path name;
            # self.filename = os.path.expanduser(self.filename)
            self.filename = Path(self.filename).expanduser()
            # config['history_source_file'] = filename_os

            # Check for existence of history_write_file key; check if there is a value; if blank or doesn't exist, then default to self.filename;
            if not "history_write_file" in config or config['history_write_file'] == "":
                self.filename_write = self.filename

            # If it does exist, then get the os.path
            else:
                self.filename_write = config['history_write_file']
                # self.filename_write = os.path.expanduser(self.filename_write)
                self.filename_write = Path(self.filename_write).expanduser()



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


    # def swatch(self, x, t='start'):
    def swatch(self, x = 'start'):
        """
        To start, do: x = self.swatch()
        To stop, pass back the variable: self.swatch(x)
        """

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

        print("Done. ", end="")
        self.swatch(x)


def run():
    mug = hist_purge()

    # pass


if __name__ == '__main__':
    mug = hist_purge()
    # mug.start()
    # hist_purge()

