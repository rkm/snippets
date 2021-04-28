# Argparse **doc** description

With `RawDescriptionHelpFormatter`, the module docstring is printed exactly
as-is. Without, the docstring is re-flowed to match the terminal width.

```console
$ python3 script.py --help
usage: script.py [-h]

This is a module docstring example. Lorem ipsum dolor sit amet, consectetur
adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat.

optional arguments:
  -h, --help  show this help message and exit
```
