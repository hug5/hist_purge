# hist_purge

## Bash history purge, deduplicate, cleanup

  - Clean up the terminal history file.
  - Deduplicate.
  - Preserve wanted entries.
  - Remove unwanted entries.
  - Sort
  - Backup your history

-------------------------------------------------

#### REQUIREMENTS
  - Python >= 3.8
  - Python Pip

#### 1. Install

Download the wheel file from /dist folder and install:
```
$ pip install hist_purge-***.whl
```

#### 2. Copy `hist_purge.toml` configuration file into your home folder
`hist_purge.toml` may be renamed as a hidden file, ie, `.hist_purge.toml`.


#### 3. Configure the `hist_purge.toml` file:

##### 3.1. Specify your history file path:
````
history_source_file = "~/.bash_history"
````
##### 3.2. You may sort lines (true) or not (false):
````
sort_lines = true
````
##### 3.3. Set your filter rules.

Example: 
````
exact_exclude = [  
  "",
  "!",  
  ".",  
  "cp",  
  "c",  
  "clear"  
]

containing_include = [
  "This is important!!"
]

regex_exclude = [  
  "^.{1}$",  
  "^touch ",  
  "^trash",
  "^locate ",
  "^whereis ",
  "^which ",
  "^whois ",
  "^df ",
  "^ffmpeg ",
  "^npm ",
  "^git",
  "^./",
  "^\\?",
  "^:"
]
````
#### 4. Run:
```
$ hist-purge

```
