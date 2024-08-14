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

Download the wheel file and install:
```
$ pip install hist_purge-***.whl

```
#### 2. Copy `hist_purge.toml` configuration file into your home folder
`hist_purge.toml` may also be named as a hidden file, ie, `.hist_purge.toml`.


#### 3. Configure the toml file:

#### 4. Specify your history file path:
````
history_source_file = "~/.bash_history"
````
#### 5. You may sort lines (true) or not (false):
````
sort_lines = true
````
#### 6. Set your filter rules.

#### 7. Then run:
```
$ hist-purge

```


