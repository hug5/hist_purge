# hist_purge

## Bash history purge, deduplicate, cleanup

• Clean up the terminal history file.
• Deduplicate.
• Preserve wanted entries.
• Remove unwanted entries.


-------------------------------------------------

#### REQUIREMENTS
  - Python >= 3.8

#### Install
```
$ pip install hist_purge-***.wh

```
# Copy `hist_purge.toml` configuration file into your home folder
# `hist_purge.toml` may also be named as a hidden file, ie, `.hist_purge.toml`.


# Configure the toml file:

# Denote your history file:
history_source_file = ".bash_history"

# You may sort lines (true) or not (false):
sort_lines = true

# Set your filter rules.


#### SYNTAX
```
$ hist-purge

```


