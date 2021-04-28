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
