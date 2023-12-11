# Python Snippets

## Tools

- pre-commit
- https://github.com/asottile/covdefaults

## Testing CLI entry point with argparse

Allows argv to be overridden by tests or other scripts which import main. Falls
back to the standard CLI parameters if argv is not provided.

Script:

```py
def main(argv: Optional[Sequence[str]] = None) -> int:

    parser = argparse.ArgumentParser()
    parser.add_argument("first")

    args = parser.parse_args(argv)

    # ...
```

Example tests:

```py
def test_main() -> None:
    args = ("foo", "bar")
    assert main(args) == 0, "Expected foo to return 0"
```

## Argparse **doc** description

With `RawDescriptionHelpFormatter`, the module docstring is printed exactly
as-is. Without, the docstring is re-flowed to match the terminal width.

Script:

```py
#!/usr/bin/env bash
"""This is a module docstring example. Lorem ipsum dolor sit amet, consectetur
adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat.
"""
import argparse


def main() -> int:

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    args = parser.parse_args()  # noqa: F841

    return 0


if __name__ == "__main__":
    exit(main())
```

Output:

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
